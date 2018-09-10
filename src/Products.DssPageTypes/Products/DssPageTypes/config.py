"""Common configuration constants
"""
from Products.CMFCore.permissions import setDefaultRoles
PROJECTNAME = 'Products.DssPageTypes'

ADD_CONTENT_PERMISSIONS = {
    # -*- extra stuff goes here -*-
    'DssContact': 'Products.DssPageTypes: Add Dss Contact',
    'DssTwoColumnPage': 'Products.DssPageTypes: Add Two Column Page',
    'DssCourse': 'Products.DssPageTypes: Add Dss Course',
    'DssTwoCollumnPage': 'Products.DssPageTypes: Add Two Collumn Page',
}