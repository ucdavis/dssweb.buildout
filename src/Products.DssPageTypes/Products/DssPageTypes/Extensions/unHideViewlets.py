from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
from zope.component import queryUtility

def unhide(self):
    """unhide the viewlets you accidentally hid."""
    storage = queryUtility(IViewletSettingsStorage)
    manager = u'plone.portaltop'
    for skinname in storage._hidden:
        hidden = storage.getHidden(manager, skinname)
        hidden = (x for x in hidden if x != u'plone.header')
        storage.setHidden(manager, skinname, hidden)
