"""Definition of the Iss Event content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content import document

# -*- Message Factory Imported Here -*-

from Products.DssPageTypes.interfaces import IFrontPage
from Products.DssPageTypes.config import PROJECTNAME
from Products.ATExtensions.ateapi import *



FrontPageSchema = document.ATDocumentSchema.copy() 

   # Set storage on fields copied from ATContentTypeSchema, making sure
   # they work well with the python bridge properties.

FrontPageSchema['title'].storage = atapi.AnnotationStorage()
FrontPageSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema( FrontPageSchema, moveDiscussion=False)
  
   #Move inset column field before bodytext so it's first on the form



class FrontPage(base.ATCTContent):
       """Two column Page"""
       implements(IFrontPage)

       meta_type = "FrontPage"
       schema = FrontPageSchema

       title = atapi.ATFieldProperty('title')
       description = atapi.ATFieldProperty('description')

       # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(FrontPage, PROJECTNAME)