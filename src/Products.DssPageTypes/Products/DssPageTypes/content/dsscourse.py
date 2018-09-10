"""Definition of the Iss Event content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content import document

# -*- Message Factory Imported Here -*-

from Products.DssPageTypes.interfaces import IDssCourse
from Products.DssPageTypes.config import PROJECTNAME
from Products.ATExtensions.ateapi import *
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin




DssCourseSchema = document.ATDocumentSchema.copy() + atapi.Schema((
  
    
       atapi.StringField(
           name="imageHelp",
           widget=atapi.LabelWidget(
               label=u"Lead Image Help",
               description=u"This is a small image that will only show on course listings.  It doesn't show on the actual course page",
              
           ),
       ),
        atapi.ImageField(
            name="inlineTopImage",
            widget=atapi.ImageWidget(
                label=u"Top Image",
                description=u"this is a medium image.  Optimum resolution is 750x422",
               
            ),
        ),
        atapi.StringField(
            name="imageCaption",
            widget=atapi.StringWidget(
                label=u"Image Caption",
                description=u"Image Caption Here",
            ),
        ),
        atapi.TextField(
            name="faculty",
            widget = atapi.RichWidget(
                label=u"Faculty Names",
                description=u"",
                
            ),
            searchable=True,
            validators=('isTidyHtmlWithCleanup',),
            default_output_type='text/x-html-safe',
        ),
        atapi.StringField(
            name="units",
            widget = atapi.StringWidget(
                label=u"units",
                description=u"",
                
            ),
        ),
        atapi.StringField(
            name="prerequs",
            widget = atapi.StringWidget(
                label=u"Prerequisites",
                description=u"",
                
            ),
        ),
        atapi.StringField(
            name="quarters",
            widget = atapi.StringWidget(
                label=u"Quarters Offered",
                description=u"",
               
           ),
       ),
      
   ))

   # Set storage on fields copied from ATContentTypeSchema, making sure
   # they work well with the python bridge properties.

DssCourseSchema['title'].storage = atapi.AnnotationStorage()
DssCourseSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema( DssCourseSchema, moveDiscussion=False)
   # finalizeATCTSchema moves 'location' into 'categories', we move it back:
   # IssEventSchema.changeSchemataForField('location', 'default')
   
   #Hide the lodation Field since we're not using it
   

class DssCourse(base.ATCTContent):
       """Course for Website"""
       implements(IDssCourse)

       meta_type = "DssCourse"
       schema = DssCourseSchema

       title = atapi.ATFieldProperty('title')
       description = atapi.ATFieldProperty('description')
       DssCourseSchema.moveField('imageHelp', before='text')
       DssCourseSchema.moveField('inlineTopImage', after='imageHelp')
       DssCourseSchema.moveField('imageCaption', after='inlineTopImage')
       

       # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(DssCourse, PROJECTNAME)