from eea.facetednavigation.interfaces import ICriteria
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from collective.contentleadimage.config import IMAGE_FIELD_NAME
from collective.contentleadimage.config import IMAGE_CAPTION_FIELD_NAME
import DateTime


def _getObjectByUID_cachekey(method, self, UID):
    return UID


class FacNavView(BrowserView):
    """ support for customized fac nav views """

    def __init__(self, context, request):
        super(FacNavView, self).__init__(context, request)
        portal_state = getMultiAdapter((self.context, self.request),
            name=u"plone_portal_state")
        self.portal_url = portal_state.portal_url()
        self.nav_url = portal_state.navigation_root_url()
        self.catalog = getToolByName(context, 'portal_catalog')

    def navRootRelativeUrl(self, obj):
        """
            Return a URL that has been adjusted to traverse
            to the object by acquisition via the nav root.
        """

        # import pdb; pdb.set_trace()
        # dept = obj.getPrimaryDepartment()
        # mi = dept.getMembershipInformation(obj)

        obj_url = obj.absolute_url()

        return obj_url.replace(self.portal_url, self.nav_url)

    def defaultForVocabulary(self, vocabulary):
        """
            return the faceted nav default for a particular criteria
        """

        for criterion in ICriteria(self.context).criteria:
            if criterion.vocabulary == vocabulary:
                return criterion.default

        return None

    def getObjectByUID(self, UID):
        """
            find the object with this UID
        """

        brains = self.catalog(UID=UID)
        return brains[0].getObject()

    def getFacNavDepartment(self):
        """
            Get the FSD department criteria for this
            FacetedNavigation views
        """

        dept_uid = self.defaultForVocabulary(u'Department Names')
        if dept_uid:
            return self.getObjectByUID(dept_uid)

        return None
        
    def tag(self, obj, css_class='tileImage'):
            scale - 'thumb'
            context = aq_inner(obj)
            field = context.getField(IMAGE_FIELD_NAME)
            titlef = context.getField(IMAGE_CAPTION_FIELD_NAME)
            if titlef is not None:
                title = titlef.get(context)
            else:
                title = ''
            if field is not None:
                if field.get_size(context) != 0:
                    return field.tag(context, scale=scale, css_class=css_class, title=title)
            return ''
    
    def getPiName(self, obj):
         context = aq_inner(obj)
         pifield = context.getField(pi)
         if pifield is not None:
             title = pifield.get(context)
         else:
             pifield = ''
         if field is not None:
             
           return pifield.tag(context, scale=scale, css_class=css_class, title=title)
         return ''
         
        
        
    
            
            
            