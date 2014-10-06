"""
    Support for banner images.

    This is a view named @@banner-image, registered for *.

    Strategy:
        Looks for folder with id "top-images" in current folder;
        If it finds it, gets a list of images inside.
        Redirects to random choice.

        If not top-image, looks for "top-image" (singular) object.
        If found, redirects to it.

        If neither for those works, redirects to ++theme++dssweb.theme.magic/images/banners/rec_blue_shadow.gif
"""

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter

import random


class BannerImage(BrowserView):

    def __call__(self):
        context = self.context
        request = self.request
        portal_state = getMultiAdapter((context, request), name=u'plone_portal_state')

        image_folder = getattr(context.aq_explicit, 'top-images', None)
        if image_folder is not None:
            catalog = getToolByName(context, 'portal_catalog')
            folder_path = '/'.join(image_folder.getPhysicalPath())
            results = catalog(
                path={'query': folder_path, 'depth': 1},
                portal_type='Image',
                )
            if results:
                self.request.response.redirect(random.choice(results).getURL())
                return None

        image = getattr(context.aq_explicit, 'top-image', None)
        if image is not None:
            self.request.response.redirect(image.absolute_url())
        else:
            self.request.response.redirect(portal_state.portal_url() + '/++theme++dssweb.theme.magic/images/banners/rec_blue_shadow.gif')

        return None
