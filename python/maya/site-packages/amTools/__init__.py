"""
A variety of tools, primarily focused on rigging and games.

\b Usage:

Put the amTools package into a folder contained within your script path
and import it.
To import the package from a userSetup.mel file, add the following line:
python("import amTools");
To import the package from a userSetup.py file, add the following line:
import amTools

Requirements:
AM_ExposeTransform.py
AM_HipConstraint.py
AM_InsertParentsCmd.py
AM_Ribbon.py
AM_ShoulderConstraint.py

\b Creation \b Info:

\b Donations: http://adammechtley.com/donations/

\b License: The MIT License

Copyright (c) 2011 Adam Mechtley (http://adammechtley.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

\namespace amTools
"""

import sys

# import some modules into Maya's __main__ module (cmds GUI executes from __main__)
## a namespace for the cmds module in the __main__ module
__kCmdsGlobalName__ = 'amToolsCmds'
import maya.mel as mel

mel.eval('python("import maya.cmds as %s")' % __kCmdsGlobalName__)
mel.eval('python("import amTools")')

## the current version of Maya as a float
__mayaVersion__ = mel.eval('getApplicationVersionAsFloat')

## current version of the tool
kVersionNumber = '1.07'
## date of current version
kVersionDate = '2011.11.07'

import python
import utilities
import modeling
import rigging
import unity
import menu


def reloadAll():
    """This function reloads all modules in this package."""
    reload(python)
    reload(utilities)
    utilities.reloadAll()

    reload(modeling)
    modeling.reloadAll()
    reload(rigging)
    rigging.reloadAll()
    reload(unity)
    unity.reloadAll()

    reload(menu)
    mel.eval('python("import amTools"); python("reload(amTools)");')

# create the menu item
menu.build()