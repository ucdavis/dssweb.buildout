# -*- coding: utf-8 -*-
from Products.CMFCore.permissions import setDefaultRoles
from zope.i18nmessageid import MessageFactory

PloneMessageFactory = MessageFactory('plone')

setDefaultRoles(
    'dss.portlet.person: Add person portlet',
    ('Manager', 'Site Administrator', 'Owner', )
)
