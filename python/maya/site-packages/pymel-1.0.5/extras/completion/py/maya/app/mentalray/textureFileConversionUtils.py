import maya.OpenMaya as OpenMaya
import maya.OpenMayaRender as OpenMayaRender
import maya.cmds as cmds
import maya
import maya.mel as mel
import os
import subprocess
import sys

def refreshAllMapFiles(referencedOnly=True):
    """
    Refresh (where required) the cache files corresponding to file
    textures in the scene. Currently the MR plugin assumes those to be
    nodes of type "file", "mentalrayTexture" or "psdFileTex"
    
    If referencedOnly is True, only convert files that appear to be used in
    the scene. Otherwise convert all files.
    """

    pass


def refreshMapFile(fileName):
    """
    Check for a cache file corresponding to the image file denoted by fileName
    and generate it (using imf_copy -p -r) if it is out of date or missing
    
    Returns the name of the generated file if successful, and an empty string
    otherwise
    """

    pass

