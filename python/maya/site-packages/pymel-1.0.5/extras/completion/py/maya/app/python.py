"""
!!!!!!!!
As of 2011, this file is no longer part of the 'official' maya distribution -
it is included here only to override it in older maya versions
!!!!!!!!


The maya.app.python module contains utilites which Maya uses to communicate
with Python.  These functions are not part of Maya's public API and may be
subject to change.

Simple test script to exercise these manually:

import maya.cmds as cmds
def e1():
    cmds.error("DUH")
def e2():
    e1()
def e3():
    cmds.ls(duh=1)
def e4():
    e3()
def e5():
    cmds.xform( q=True )
def e6():
    e5()
"""

import maya
import sys
import traceback

from maya.utils import *

