##############################################################################
#
# Copyright (c) 2001 Zope Foundation and Contributors
# Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this
# distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
""" PluginRegistry product initialization.

$Id$
"""

from utils import allTests

import PluginRegistry

def initialize(context):

    context.registerClass( PluginRegistry.PluginRegistry
                         , constructors=[ ( 'Dummy', lambda: None ) ]
                         , visibility=None
                         , icon='www/PluginRegistry.png'
                         )

