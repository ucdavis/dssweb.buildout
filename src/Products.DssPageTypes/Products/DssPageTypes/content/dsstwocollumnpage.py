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
  
    
       atapi.TextField(
               name="insetcolumn",
               widget = atapi.RichWidget(
                   label=u"Small Column Text",
                   description=u"This text will be Blue",
                   width="40",
               ),
              
            ),
        
   ))

   # Set storage on fields copied from ATContentTypeSchema, making sure
   # they work well with the python bridge properties.

DssTwoCollumnPageSchema['title'].storage = atapi.AnnotationStorage()
DssTwoCollumnPageSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema( DssTwoCollumnPageSchema, moveDiscussion=False)
   # finalizeATCTSchema moves 'location' into 'categories', we move it back:
   # IssEventSchema.changeSchemataForField('location', 'default')
   
   #Hide the lodation Field since we're not using it
   

class DssTwoCollumnPage(base.ATCTContent):
       """Event for ISS website"""
       implements(IDssTwoCollumnPage)

       meta_type = "DssTwoCollumnPage"
       schema = DssTwoCollumnPageSchema

       title = atapi.ATFieldProperty('title')
       description = atapi.ATFieldProperty('description')

       # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(DssTwoCollumnPage, PROJECTNAME)