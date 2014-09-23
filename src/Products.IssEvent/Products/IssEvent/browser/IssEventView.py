from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IssEventView(BrowserView):

    template = ViewPageTemplateFile('iss_event_view.pt')

    def __call__(self):
        """"""
        self.hello_name = getattr(self.context, 'hello_name', 'World')
        return self.template()