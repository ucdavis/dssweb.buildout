TYPES_TO_VERSION = ('DssTwoColumnPage', 'DssCourse')
def installVersionedTypes(context):
    if context.readDataFile('installVersionedTypes.txt') is None:
        return
    try:
        from Products.CMFEditions.setuphandlers import DEFAULT_POLICIES
    except ImportError:
        # Use repositorytool.xml instead (Plone 4.1 and above)
        pass
    else:
        portal = context.getSite()
        portal_repository = getToolByName(portal, 'portal_repository')
        versionable_types = list(portal_repository.getVersionableContentTypes())
        for type_id in TYPES_TO_VERSION:
            if type_id not in versionable_types:
                # use append() to make sure we don't overwrite any
                # content-types which may already be under version control
                versionable_types.append(type_id)
                for policy_id in DEFAULT_POLICIES:
                    portal_repository.addPolicyForContentType(type_id, policy_id)
        portal_repository.setVersionableContentTypes(versionable_types)
