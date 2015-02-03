from Products.Five.browser import BrowserView
from Acquisition import aq_inner
from zope.component import getMultiAdapter


class DssContactView(BrowserView):

  
    def __init__(self, context, request):
            self.context = context
            self.request = request
            
    def portal_state(self):
         context = aq_inner(self.context)
         portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
         return portal_state
                
            
            
class DssTwoCollumnView(BrowserView):

  
    def __init__(self, context, request):
            self.context = context
            self.request = request