# -*- coding: utf-8 -*-
"""Definition of the Blog content type
"""
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content.base import registerATCT
from collective.blogstarentry.config import PROJECTNAME
from collective.blogstarentry.interfaces import IBlog
from zope.interface import implements

class Blog(folder.ATFolder):
    """Folder for Blog"""
    implements(IBlog)

    meta_type = "Blog"

registerATCT(Blog, PROJECTNAME)
