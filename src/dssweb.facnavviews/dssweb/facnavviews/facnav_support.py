from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter
from Products.FacultyStaffDirectory import Person


class FacNavView(BrowserView):
    """ support for customized fac nav views """

    def __init__(self, context, request):
        super(FacNavView, self).__init__(context, request)
        portal_state = getMultiAdapter((self.context, self.request),
            name=u"plone_portal_state")
        self.portal_url = portal_state.portal_url()
        self.nav_url = portal_state.navigation_root_url()

    def navRootRelativeUrl(self, obj):
        """
            Return a URL that has been adjusted to traverse
            to the object by acquisition via the nav root.
        """

        obj_url = obj.absolute_url()

        return obj_url.replace(self.portal_url, self.nav_url)
