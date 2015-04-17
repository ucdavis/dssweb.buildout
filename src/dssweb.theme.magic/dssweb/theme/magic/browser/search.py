# -*- coding: utf-8 -*-

from plone.app.search.browser import Search as PloneSearch
from plone.app.contentlisting.interfaces import IContentListing
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.PloneBatch import Batch
from Products.ZCTextIndex.ParseTree import ParseError
from zope.component import getMultiAdapter


def scoreCmp(a, b):
    return cmp(b.data_record_normalized_score_, a.data_record_normalized_score_)


class Search(PloneSearch):
    """ Override plone.app.search Search
    """

    def __init__(self, context, request):
        super(Search, self).__init__(context, request)
        portal_state = getMultiAdapter((self.context, self.request),
            name=u"plone_portal_state")
        self.portal_url = portal_state.portal_url()
        self.nav_url = portal_state.navigation_root_url()

    def results(self, query=None, batch=True, b_size=10, b_start=0):
        """ Get properly wrapped search results from the catalog.
        Everything in Plone that performs searches should go through this view.
        'query' should be a dictionary of catalog parameters.
        """

        context = self.context

        if query is None:
            query = {}
        if batch:
            query['b_start'] = b_start = int(b_start)
            query['b_size'] = b_size
        query = self.filter_query(query)

        if query is None:
            results = []
        else:
            catalog = getToolByName(self.context, 'portal_catalog')
            try:
                results = catalog(**query)
                if query['path'] and 'FSDPerson' in query['portal_type']:
                    # we're in a subsite/section and people are allowed
                    # in the results.
                    people = getattr(self.context, 'people', None)
                    if people is not None:
                        query['path'] = '/'.join(people.getPhysicalPath())
                        query['portal_type'] = ['FSDPerson']
                        # limit to the department.
                        # strategy: get department name as last id in
                        # navigation root path.
                        # Find matching FSD department, get its UID;
                        # use that to match getRawDepartments.
                        department_name = self.nav_url.split('/')[-1]
                        department = getattr(context, department_name, None)
                        if department is not None:
                            duid = context.people[department_name].UID()
                            query['getRawDepartments'] = duid
                            results = results + catalog(**query)
                            # note that our results will no longer
                            # be lazy after the next step. there
                            # may be efficiency implications
                            results = sorted(results, scoreCmp)
            except ParseError:
                return []

        results = IContentListing(results)
        if batch:
            results = Batch(results, b_size, b_start)
        return results

    # def navRootRelativeUrl(self, url):
    #     """
    #         Return a URL that has been adjusted to traverse
    #         to the object by acquisition via the nav root.
    #     """

    #     return url.replace(self.portal_url, self.nav_url)
