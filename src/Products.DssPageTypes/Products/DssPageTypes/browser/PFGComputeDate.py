from zope.publisher.browser import BrowserView
import datetime

class fixDates(BrowserView):
    """ this should be fun"""
    def _call_(self):
        request = self.request
        context = self.context


        dt = datetime.strptime((form['start-date-and-time']),'%Y%m%d %H%M')
        mins = (form['duration-in-minutes'])
        newdate = dt + timedelta(minutes = mins)
        return newdate
        
        