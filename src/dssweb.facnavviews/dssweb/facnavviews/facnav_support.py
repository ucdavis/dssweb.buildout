from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter


class FacNavView(BrowserView):
    """ support for customized fac nav views """

    def navRootRelativeUrl(self, obj):
        """
            Return a URL that has been adjusted to traverse
            to the object by acquisition via the nav root.
        """

        portal_state = getMultiAdapter((self.context, self.request),
            name=u"plone_portal_state")
        portal_url = portal_state.portal_url()
        nav_url = portal_state.navigation_root_url()
        obj_url = obj.absolute_url()

        return obj_url.replace(portal_url, nav_url)
