from Products.Five.browser import BrowserView
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName


class DssContactView(BrowserView):

  
    def __init__(self, context, request):
            self.context = context
            self.request = request
            
    def render_form(self):
         portal = getToolByName(self.context, 'portal_url').getPortalObject()
         form_view = portal.restrictedTraverse('contact/contact-form/@@embedded')
         form_view.prefix = 'mypfg'
         return form_view()
            
    def portal_state(self):
         context = aq_inner(self.context)
         portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
         return portal_state
                
            
            
class DssTwoCollumnView(BrowserView):

  
    def __init__(self, context, request):
            self.context = context
            self.request = request

class DssCourseView(BrowserView):

  
    def __init__(self, context, request):
            self.context = context
            self.request = request