"""Common configuration constants
"""
from Products.CMFCore.permissions import setDefaultRoles
PROJECTNAME = 'Products.DssPageTypes'

ADD_CONTENT_PERMISSIONS = {
    # -*- extra stuff goes here -*-
    'DssContact': 'Products.DssPageTypes: Add Dss Contact',
    'DssTwoColumnPage': 'Products.DssPagetypes: Add Two Column Page',
    'DssTwoCollumnPage': 'Products.DssPagetypes: Add Two column Page',
    'DssCourse': 'Products.DssPageTypes: Add Dss Course',
}