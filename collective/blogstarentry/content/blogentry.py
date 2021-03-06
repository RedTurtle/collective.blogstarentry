# -*- coding: utf-8 -*-
"""Definition of the BlogEntry content type
"""
from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.ATContentTypes.content.base import registerATCT
from collective.blogstarentry.config import PROJECTNAME
from collective.blogstarentry.interfaces import IBlogEntry
from zope.interface import implements

class BlogEntry(ATNewsItem):
    """A blog entry object"""
    implements(IBlogEntry)

    meta_type = "BlogEntry"

registerATCT(BlogEntry, PROJECTNAME)
