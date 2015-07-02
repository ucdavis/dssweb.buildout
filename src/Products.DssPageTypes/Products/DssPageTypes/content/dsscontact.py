"""Definition of the Iss Event content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content import document
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget


# -*- Message Factory Imported Here -*-

from Products.DssPageTypes.interfaces import IDssContact
from Products.DssPageTypes.config import PROJECTNAME
from Products.ATExtensions.ateapi import *



DssContactSchema = document.ATDocumentSchema.copy() + atapi.Schema((
  
    
       atapi.TextField(
               name="mapurl",
               max_size="500",
               widget = atapi.TextAreaWidget(
                   label=u"Map URL",
                   description=u"Paste Google Map URL in here, no iframe tag or quotes",
                   rows="5",
               ),
              
            ),
        atapi.StringField(
            name="mapwidth",
            widget = atapi.StringWidget(
                label=u"Map Width",
                description=u"IFrame Map Width",
                
            ),
        ),
        
        atapi.StringField(
           name="mapheight",
           widget = atapi.StringWidget(
               label=u"Map Height",
               description=u"IFrame Map Height",
               
           ),
       ),
        atapi.StringField(
           name="mapstyle",
           widget = atapi.StringWidget(
               label=u"Map Style",
               description=u"Add some inline-styles",
               
           ),
       ),
       
   ))

   # Set storage on fields copied from ATContentTypeSchema, making sure
   # they work well with the python bridge properties.

DssContactSchema['title'].storage = atapi.AnnotationStorage()
DssContactSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema( DssContactSchema, moveDiscussion=False)
   # finalizeATCTSchema moves 'location' into 'categories', we move it back:
   # IssEventSchema.changeSchemataForField('location', 'default')
   
   #Hide the lodation Field since we're not using it
   

class DssContact(base.ATCTContent):
       """Event for ISS website"""
       implements(IDssContact)

       meta_type = "DssContact"
       schema = DssContactSchema

       title = atapi.ATFieldProperty('title')
       description = atapi.ATFieldProperty('description')

       # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(DssContact, PROJECTNAME)