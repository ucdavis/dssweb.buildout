# -*- coding: utf-8 -*-
"""view to unify api for folder, old-style collection and new-style collection
"""
from Products.Five.browser import BrowserView


class UnifiedContentMixin(object):
    """This mixin provides a unified api call for getting objects in a location

    it is intended to work with ATFolder, ATTopic and plone.app.collection types
    """

    def results(self, **kwargs):
        """pass call through to individual implementations"""
        return self._results(**kwargs)

    def _results(self, **kwargs):
        """subclasses must implement this method"""
        raise NotImplementedError()


class FolderUnifiedView(UnifiedContentMixin, BrowserView):
    """wrapper for unified view api around an ATFolder"""

    def _results(self, batch=True, b_start=0, b_size=0, sort_on=None, brains=False, custom_query={}):
        return []


class TopicUnifiedView(UnifiedContentMixin, BrowserView):
    """wrapper for unified view api around an ATTopic"""

    def _results(self, batch=True, b_start=0, b_size=0, sort_on=None, brains=False, custom_query={}):
        return []


class CollectionUnifiedView(UnifiedContentMixin, BrowserView):
    """wrapper for unified view api around a plone.app.collecitons collection
    """

    def _results(self, batch=True, b_start=0, b_size=0, sort_on=None, brains=False, custom_query={}):
        return self.context.results(batch, b_start, b_size, sort_on, brains, custom_query)