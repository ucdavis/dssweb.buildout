"""Definition of the Iss Event content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content import document

# -*- Message Factory Imported Here -*-

from Products.DssPageTypes.interfaces import IDssTwoColumnPage
from Products.DssPageTypes.config import PROJECTNAME
from Products.ATExtensions.ateapi import *



DssTwoColumnPageSchema = document.ATDocumentSchema.copy() + atapi.Schema((
  
    
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
              label=u"Small column Title",
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

DssTwoColumnPageSchema['title'].storage = atapi.AnnotationStorage()
DssTwoColumnPageSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema( DssTwoColumnPageSchema, moveDiscussion=False)
  
   #Move inset column field before bodytext so it's first on the form

DssTwoColumnPageSchema.moveField('insetcolumn',after='description')
DssTwoColumnPageSchema.moveField('insettitle',after='description')   

class DssTwoColumnPage(base.ATCTContent):
       """Two column Page"""
       implements(IDssTwoColumnPage)

       meta_type = "DssTwoColumnPage"
       schema = DssTwoColumnPageSchema

       title = atapi.ATFieldProperty('title')
       description = atapi.ATFieldProperty('description')

       # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(DssTwoColumnPage, PROJECTNAME)