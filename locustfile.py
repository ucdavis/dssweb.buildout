import os
import sys
import random
from lxml import etree
from locust import HttpLocust, TaskSet, task

IMG_DIR = os.path.join(os.path.dirname(__file__), 'locust_images')
SITE_ID = 'test-site'
USER = 'admin'
PASS = 'aLv7Eb6ju9aV7O'

ALL_IMAGES = []
VIEW_URLS = ('', '/view', '/@@images/image/thumb', '/@@images/image/mini',
             '/@@images/image/preview', '/@@images/image/large',
             '/@@images/image/icon')


def select_image():
    files = os.listdir(IMG_DIR)
    fname = random.choice(files)
    path = os.path.join(IMG_DIR, fname)
    return fname, open(path, 'r')


class ImageCreator(TaskSet):
    created_images = []

    def login(self):
        with self.client.post("/" + SITE_ID + "/login_form", {
                "__ac_name": USER,
                "__ac_password": PASS,
                "came_from": "",
                "next": "",
                "target": "",
                "form.submitted": "1",
                "js_enabled": "0",
                "cookies_enabled": "1",
                "login_name": USER,
                "pwd_empty": "0",
                "submit": "Log in"},
                              catch_response=True) as resp:
            if 'You are now logged in' not in resp.content:
                resp.failure('Could not login')

    def logout(self):
        self.client.get('/' + SITE_ID + '/logout')

    def _add_image(self, img_id, title, img_file):
        with self.client.post(
                "/" + SITE_ID +
                "/portal_factory/Image/image.{}/atct_edit".format(
                    title
                ), data={
                    'id': img_id,
                    'title': title,
                    'description': 'Some Description',
                    'description_text_format': 'text/plain',
                    'form.button.save': 'Save',
                    'form.submitted': '1',
                    'last_referer': '/' + SITE_ID + '/'
                }, files={'image_file': img_file},
                catch_response=True) as resp:
            if resp.status_code != 200:
                resp.raise_for_status()
            if 'Changes saved.' not in resp.content:
                html = etree.HTML(resp.content)
                errors = html.xpath('//div[@class="fieldErrorBox"]/text()')
                errors = '; '.join(e for e in errors if e)
                resp.failure(errors)
                return
        return resp.url.split('/')[-2]

    @task
    def add_image(self):
        self.login()
        number = random.randint(1, sys.maxint)
        fname, img_file = select_image()
        img_id = '{}-{}.jpg'.format(fname, number)
        title = fname
        with img_file as img:
            new_id = self._add_image(img_id, title, img)
        if new_id:
            ALL_IMAGES.append(new_id)
        self.logout()
        self.interrupt(True)


class SiteBrowser(TaskSet):
    tasks = {ImageCreator: 1}

    login = ImageCreator.login.im_func
    logout = ImageCreator.logout.im_func

    @task(15)
    def view_image(self):
        if ALL_IMAGES:
            img_id = random.choice(ALL_IMAGES)
            more = random.choice(VIEW_URLS)
            self.client.get('/' + SITE_ID + '/images/' + img_id + more)
        else:
            self.client.get("/" + SITE_ID + '/')

    @task(2)
    def index(self):
        self.client.get("/" + SITE_ID + '/images')

    @task(1)
    def site_root(self):
        self.client.get("/" + SITE_ID + '/')

    def create_site(self):
        has_site = False
        with self.client.get('/' + SITE_ID + '/', catch_response=True) as resp:
            if resp.status_code == 200:
                has_site = True
        if not has_site:
            self.client.auth = (USER, PASS)
            with self.client.post('/@@plone-addsite', data={
                    'site_id': SITE_ID,
                    'title': 'Test Site',
                    'default_language': 'en',
                    'setup_content:boolean': 'true',
                    'form.submitted:boolean': 'True',
                    'extension_ids:list': 'plonetheme.classic:default',
                    'extension_ids:list': 'plonetheme.sunburst:default',
                    'submit': 'Create Plone Site'}, catch_response=True) as resp:
                if resp.status_code != 200:
                    resp.raise_for_status()
                if 'Welcome to Plone' not in resp.content:
                    resp.failure('Site not created')
                    self.client.auth = False
                    return
        with self.client.get('/' + SITE_ID + '/images',
                             catch_response=True) as resp:
            if resp.status_code == 200:
                return
        # Create an image folder
        with self.client.post(
                "/" + SITE_ID +
                "/portal_factory/Folder/folder.{}/atct_edit".format(
                    'images'
                ), data={
                    'id': 'images',
                    'title': 'Images',
                    'description': 'Image Folder',
                    'description_text_format': 'text/plain',
                    'form.button.save': 'Save',
                    'form.submitted': '1',
                    'last_referer': '/' + SITE_ID + '/'
                }, catch_response=True) as resp:
            if resp.status_code >= 400:
                self.client.auth = False
                resp.raise_for_status()
            if 'Changes saved.' not in resp.content:
                html = etree.HTML(resp.content)
                errors = html.xpath('//div[@class="fieldErrorBox"]/text()')
                errors = '; '.join(e for e in errors if e)
                self.client.auth = False
                resp.failure(errors)
                return
        # Publish the Folder
        with self.client.get(
                "/" + SITE_ID +
                "/images/content_status_modify?workflow_action=publish",
                catch_response=True) as resp:
            if resp.status_code >= 400:
                self.client.auth = False
                resp.raise_for_status()
        # Set the thumbnail view
        with self.client.get(
                "/" + SITE_ID +
                "/images/selectViewTemplate?templateId=atct_album_view",
                catch_response=True) as resp:
            if resp.status_code >= 400:
                self.client.auth = False
                resp.raise_for_status()
        self.client.auth = False

    def on_start(self):
        self.create_site()


class CMSUser(HttpLocust):
    task_set = SiteBrowser
    min_wait = 10000
    max_wait = 30000
