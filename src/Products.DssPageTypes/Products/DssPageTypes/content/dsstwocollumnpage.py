"""Definition of the Iss Event content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content import document

# -*- Message Factory Imported Here -*-

from Products.DssPageTypes.interfaces import IDssTwoCollumnPage
from Products.DssPageTypes.config import PROJECTNAME
from Products.ATExtensions.ateapi import *



DssTwoCollumnPageSchema = document.ATDocumentSchema.copy() + atapi.Schema((
  
    
       atapi.ImageField(
           name="medTopImage",
           widget=atapi.ImageWidget(
               label=u"Top Image",
               description=u"this is a large top image",
               
           ),
       ),
      atapi.StringField(
          name="imageCaption",
          widget=atapi.StringWidget(
              label=u"Image Caption",
              description=u"Image Caption Here",
          ),
      ),
      atapi.StringField(
          name="insettitle",
          widget=atapi.StringWidget(
              label=u"Small Collumn Title",
              description=u"This text will be blue"
          ),
      ),     
       
       atapi.TextField(
               name="insetcolumn",
               widget = atapi.RichWidget(
                   label=u"Small Column Text",
                   description=u"for blue headings pick the blueheading style",
                   width="40",
                   ),
                   searchable=True,
                   validators=('isTidyHtmlWithCleanup',),
                   default_output_type='text/x-html-safe',
               
              
            ),
        
   ))

   # Set storage on fields copied from ATContentTypeSchema, making sure
   # they work well with the python bridge properties.

DssTwoCollumnPageSchema['title'].storage = atapi.AnnotationStorage()
DssTwoCollumnPageSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema( DssTwoCollumnPageSchema, moveDiscussion=False)
  
   #Move inset collumn field before bodytext so it's first on the form

DssTwoCollumnPageSchema.moveField('insetcolumn',after='description')
DssTwoCollumnPageSchema.moveField('insettitle',after='description')   

class DssTwoCollumnPage(base.ATCTContent):
       """Two Collumn Page"""
       implements(IDssTwoCollumnPage)

       meta_type = "DssTwoCollumnPage"
       schema = DssTwoCollumnPageSchema

       title = atapi.ATFieldProperty('title')
       description = atapi.ATFieldProperty('description')

       # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(DssTwoCollumnPage, PROJECTNAME)