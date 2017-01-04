# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api
from collective.blog.view.interfaces import IBlogEntryRetriever


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'collective.blogstarentry:uninstall',
        ]


def post_install(context):
    """Post install script"""
    if context.readDataFile('collectiveblogstarentry_default.txt') is None:
        return

    # Do something during the installation of this package
    api.portal.set_registry_record(
        'blog_types', u'BlogEntry', interface=IBlogEntryRetriever)
