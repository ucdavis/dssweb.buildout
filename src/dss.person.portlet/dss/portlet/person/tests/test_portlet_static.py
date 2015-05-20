# -*- coding: utf-8 -*-
from plone.app.portlets.storage import PortletAssignmentMapping
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.portlet.person import person
from plone.portlet.person.testing import PLONEPORTLETperson_INTEGRATION_TESTING
from plone.portlets.interfaces import IPortletAssignment
from plone.portlets.interfaces import IPortletDataProvider
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletRenderer
from plone.portlets.interfaces import IPortletType
from zope.component import getUtility, getMultiAdapter
import unittest2 as unittest


class TestPortlet(unittest.TestCase):

    layer = PLONEPORTLETperson_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.folder = getattr(self.portal, 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)

    def testPortletTypeRegistered(self):
        portlet = getUtility(IPortletType, name='plone.portlet.person.person')
        self.assertEquals(portlet.addview, 'plone.portlet.person.person')

    def testInterfaces(self):
        portlet = person.Assignment(header=u"title", text="text")
        self.failUnless(IPortletAssignment.providedBy(portlet))
        self.failUnless(IPortletDataProvider.providedBy(portlet.data))

    def testInvokeAddview(self):
        portlet = getUtility(IPortletType, name='plone.portlet.person.person')
        mapping = self.portal.restrictedTraverse(
            '++contextportlets++plone.leftcolumn'
        )
        for m in mapping.keys():
            del mapping[m]
        addview = mapping.restrictedTraverse('+/' + portlet.addview)

        addview.createAndAdd(
            data={'header': u"test title", 'text': u"test text"}
        )

        self.assertEquals(len(mapping), 1)
        self.failUnless(isinstance(mapping.values()[0], person.Assignment))

    def testInvokeEditView(self):
        mapping = PortletAssignmentMapping()
        request = self.folder.REQUEST

        mapping['foo'] = person.Assignment(header=u"title", text="text")
        editview = getMultiAdapter((mapping['foo'], request), name='edit')
        self.failUnless(isinstance(editview, person.EditForm))

    def testRenderer(self):
        context = self.folder
        request = self.folder.REQUEST
        view = self.folder.restrictedTraverse('@@plone')
        manager = getUtility(
            IPortletManager,
            name='plone.rightcolumn',
            context=self.portal
        )
        assignment = person.Assignment(header=u"title", text="text")

        renderer = getMultiAdapter(
            (context, request, view, manager, assignment),
            IPortletRenderer
        )
        self.failUnless(isinstance(renderer, person.Renderer))

        self.failUnless(renderer.available,
                        "Renderer should be available by default.")


class TestRenderer(unittest.TestCase):

    layer = PLONEPORTLETperson_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.folder = getattr(self.portal, 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)

    def renderer(self, context=None, request=None, view=None, manager=None,
                 assignment=None):
        context = context or self.folder
        request = request or self.folder.REQUEST
        view = view or self.folder.restrictedTraverse('@@plone')
        manager = manager or getUtility(
            IPortletManager,
            name='plone.rightcolumn',
            context=self.portal
        )
        assignment = assignment or person.Assignment(
            header=u"title",
            text="text"
        )
        ren = getMultiAdapter(
            (context, request, view, manager, assignment),
            IPortletRenderer
        )
        ren.__portlet_metadata__ = {
            'key': '/'.join(self.portal.getPhysicalPath())
        }
        return ren

    def test_render(self):
        r = self.renderer(
            context=self.portal,
            assignment=person.Assignment(
                header=u"title",
                text="<b>text</b>"
            )
        )
        r = r.__of__(self.folder)
        r.update()
        output = r.render()
        self.failUnless('title' in output)
        self.failUnless('<b>text</b>' in output)

    def test_no_header(self):
        r = self.renderer(
            context=self.portal,
            assignment=person.Assignment(text="<b>text</b>")
        )
        r = r.__of__(self.folder)
        r.update()
        output = r.render()
        self.assertTrue('<a class="tile"' not in output)
        self.assertTrue('<header class="portletHeader titleless"' in output)

    def test_hide(self):
        self.assertRaises(TypeError, person.Assignment, hide=True)

    def test_css_class(self):
        r = self.renderer(
            context=self.portal,
            assignment=person.Assignment(
                header=u"Welcome text",
                text="<b>text</b>"
            )
        )
        self.assertEquals('portlet-person-welcome-text', r.css_class())

    def test_relative_link(self):
        folder_id = self.portal.invokeFactory(
            'Folder',
            id='folder1',
            title='My Folder Title'
        )
        r = self.renderer(
            context=self.portal[folder_id],
            assignment=person.Assignment(
                text="""<a href="relative/link">link</a>"""
            )
        )
        r = r.__of__(self.folder)
        r.update()
        output = r.render()
        self.assertTrue("http://nohost/plone/relative/link" in output)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestPortlet))
    suite.addTest(makeSuite(TestRenderer))
    return suite
