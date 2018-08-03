import random
from Products.Five.browser import BrowserView
from zope.interface import implements
from Products.CMFCore.utils import getToolByName
from Products.DssPageTypes.browser.interfaces import IBackgroundSliderView
from Acquisition import aq_inner


class BackgroundSlideshowView(BrowserView):
    """View class for the Slideshow
    """
    implements(IBackgroundSliderView)

    def getImages(self, slideshowfolderid, randomize=False):
        # we check if there is a folder with id slideshowfolderid
        # if so, we return the images in it
        results = []
        if self.context.getId() == slideshowfolderid or \
           not self.context.isPrincipiaFolderish:
            parent = aq_inner(self.context).getParentNode()
        else:
            parent = self.context
        if slideshowfolderid in parent.objectIds():
            pc = getToolByName(self.context, 'portal_catalog')
            path = {
                'query':
                '/'.join(parent[slideshowfolderid].getPhysicalPath())}
            results = pc.searchResults(portal_type='Image',
                                       path=path,
                                       sort_on='getObjPositionInParent')
        if randomize:
            results = [brain for brain in results]
            random.shuffle(results)
        return results