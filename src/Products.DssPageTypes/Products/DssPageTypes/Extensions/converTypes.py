from Products.CMFCore.utils import getToolByName
from zope.component.hooks import getSite
from Acquisition import aq_parent

def convertTypes(self):

    site = getSite()
    source_contenttype = 'DssTwoCollumnPage'
    target_contenttype = 'DssTwoColumnPage'
    

    catalog = getToolByName(site, 'portal_catalog')

    items = catalog.searchResults(portal_type = source_contenttype)

    for item in items:
        itemobj = item.getObject()
        id = "%s-new" % itemobj.getId()
        title = itemobj.Title()
        description = itemobj.Description()
        text = itemobj.getText()
        medTopImage = itemobj.getMedTopImage()
        imageCaption = itemobj.getImageCaption()
        insettitle = itemobj.getInsettitle()
        insetcolumn = itemobj.getInsetcolumn()
        pFolder = itemobj.aq_parent

        service = pFolder.invokeFactory(target_contenttype, id,
                 title=title,description=description,text=text,medTopImage=medTopImage,imageCaption=imageCaption,insettitle=insettitle,insetcolumn=insetcolumn)