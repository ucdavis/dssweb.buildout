from zope.interface import Interface

class IBackgroundSliderView(Interface):
    """ View class for the Slideshow
    """

    def getImages(slideshowfolderid):
        """ Get the images for the slideshow based of the given ID
        """