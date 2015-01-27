from Products.Five.browser import BrowserView

class DssContactView(BrowserView):

  
    def __init__(self, context, request):
            self.context = context
            self.request = request
            
            
class DssTwoCollumnView(BrowserView):

  
    def __init__(self, context, request):
            self.context = context
            self.request = request