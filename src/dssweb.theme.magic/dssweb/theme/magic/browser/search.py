# -*- coding: utf-8 -*-

from plone.app.contentlisting.interfaces import IContentListing
from plone.app.search.browser import Search as PloneSearch
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.PloneBatch import Batch
from Products.ZCTextIndex.ParseTree import ParseError
from zope.component import getMultiAdapter

import re


def scoreCmp(a, b):
    return cmp(b.data_record_normalized_score_, a.data_record_normalized_score_)


def dateCmp(a, b):
    return cmp(b.Date, a.Date)


def titleCmp(a, b):
    return cmp(a.Title.lower(), b.Title.lower())


class Search(PloneSearch):
    """ Override plone.app.search Search
    """

    def __init__(self, context, request):
        super(Search, self).__init__(context, request)
        portal_state = getMultiAdapter((self.context, self.request),
            name=u"plone_portal_state")
        self.portal_url = portal_state.portal_url()
        self.nav_url = portal_state.navigation_root_url()
        self.in_sub_site = self.portal_url != self.nav_url

    def results(self, query=None, batch=True, b_size=10, b_start=0):
        """
            Customize Plone's search to include people from the root FSD
            when searching in a departmental subsite.
        """

        if not self.in_sub_site:
            return super(Search, self).results(query, batch, b_size, b_start)

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
                            dobj = getattr(context.people, department_name, None)
                            if dobj is not None:
                                duid = dobj.UID()
                                query['getRawDepartments'] = duid
                                results = results + catalog(**query)

                                sort_on = query.get('sort_on')
                                if sort_on == 'sortable_title':
                                    sort_cmp = titleCmp
                                elif sort_on == 'Date':
                                    sort_cmp = dateCmp
                                else:
                                    sort_cmp = scoreCmp
                                # note that our results will no longer
                                # be lazy after the next step. there
                                # may be efficiency implications
                                results = sorted(results, sort_cmp)
            except ParseError:
                return []

        results = IContentListing(results)
        if batch:
            results = Batch(results, b_size, b_start)
        return results

    def navRootRelativeUrl(self, url):
        """
            Return a URL that has been adjusted to traverse
            to the object by acquisition via the nav root.
        """

        if self.in_sub_site:
            url = url.replace(self.portal_url, self.nav_url)
        return url

    def breadcrumbs(self, item):
        """
            Custom breadcrumbs to localize people
        """

        crumbs = super(Search, self).breadcrumbs(item)
        if self.in_sub_site and crumbs:
            last_crumb = crumbs[-1]
            last_crumb['absolute_url'] = self.navRootRelativeUrl(re.sub(
                r"/people$",
                '/directory-of-people',
                last_crumb['absolute_url']
                ))
        return crumbs
