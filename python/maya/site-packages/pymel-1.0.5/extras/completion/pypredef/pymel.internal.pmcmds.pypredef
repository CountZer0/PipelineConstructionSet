"""
There are a number of pymel objects which must be converted to a "mel-friendly"
representation. For example, in versions prior to 2009, some mel commands (ie, getAttr) which expect
string arguments will simply reject custom classes, even if they have a valid string representation.
Another Example is mel's matrix inputs, which expects a flat list of 16 flaots, while pymel's Matrix has a more typical
4x4 representation.

If you're having compatibility issues with your custom classes when passing them to maya.cmds,
simply add a __melobject__ function that returns a mel-friendly result and pass them to pymel's wrapped commands.

The wrapped commands in this module are the starting point for any other pymel customizations.
"""

import pymel.versions as versions
import sys
import os
import warnings
import maya
import pymel.util as util

from maya.cmds import *

from exceptions import ValueError as objectErrorType

def instance(*args, **kwargs):
    pass


def polySplit(*args, **kwargs):
    pass


def toolPropertyWindow(*args, **kwargs):
    pass


def getCmdName(inFunc):
    """
    Use in place of inFunc.__name__ when inFunc could be a maya.cmds cmd
    
    handles stubFuncs
    """

    pass


def toolBar(*args, **kwargs):
    pass


def getPanel(*args, **kwargs):
    pass


def polyReduce(*args, **kwargs):
    pass


def pointConstraint(*args, **kwargs):
    pass


def floatScrollBar(*args, **kwargs):
    pass


def getAttr(*args, **kwargs):
    pass


def polyColorPerVertex(*args, **kwargs):
    pass


def polyDelEdge(*args, **kwargs):
    pass


def textField(*args, **kwargs):
    pass


def pointOnPolyConstraint(*args, **kwargs):
    pass


def filter(*args, **kwargs):
    pass


def extendSurface(*args, **kwargs):
    pass


def insertKnotCurve(*args, **kwargs):
    pass


def curveIntersect(*args, **kwargs):
    pass


def parentConstraint(*args, **kwargs):
    pass


def fontDialog(*args, **kwargs):
    pass


def rebuildSurface(*args, **kwargs):
    pass


def connectAttr(*args, **kwargs):
    pass


def polyNormalizeUV(*args, **kwargs):
    pass


def polyToSubdiv(*args, **kwargs):
    pass


def polyCone(*args, **kwargs):
    pass


def polyTriangulate(*args, **kwargs):
    pass


def createDisplayLayer(*args, **kwargs):
    pass


def polyBoolOp(*args, **kwargs):
    pass


def skinCluster(*args, **kwargs):
    pass


def directionalLight(*args, **kwargs):
    pass


def nurbsPlane(*args, **kwargs):
    pass


def offsetSurface(*args, **kwargs):
    pass


def fluidEmitter(*args, **kwargs):
    pass


def scriptJob(*args, **kwargs):
    pass


def manipMoveContext(*args, **kwargs):
    pass


def sceneEditor(*args, **kwargs):
    pass


def loft(*args, **kwargs):
    pass


def commandLine(*args, **kwargs):
    pass


def colorIndexSliderGrp(*args, **kwargs):
    pass


def exportEdits(*args, **kwargs):
    pass


def listConnections(*args, **kwargs):
    pass


def workspace(*args, **kwargs):
    pass


def MentalRayApproxEditor(*args, **kwargs):
    pass


def hudButton(*args, **kwargs):
    pass


def boundary(*args, **kwargs):
    pass


def visor(*args, **kwargs):
    pass


def subdMapCut(*args, **kwargs):
    pass


def move(*args, **kwargs):
    pass


def GpuCacheExportSelectionOptions(*args, **kwargs):
    pass


def nurbsCurveToBezier(*args, **kwargs):
    pass


def nonLinear(*args, **kwargs):
    pass


def spotLight(*args, **kwargs):
    pass


def intScrollBar(*args, **kwargs):
    pass


def nodeOutliner(*args, **kwargs):
    pass


def lattice(*args, **kwargs):
    pass


def checkBox(*args, **kwargs):
    pass


def menu(*args, **kwargs):
    pass


def checkBoxGrp(*args, **kwargs):
    pass


def select(*args, **kwargs):
    pass


def image(*args, **kwargs):
    pass


def unloadPlugin(*args, **kwargs):
    pass


def lightList(*args, **kwargs):
    pass


def distanceDimension(*args, **kwargs):
    pass


def hudSlider(*args, **kwargs):
    pass


def attrEnumOptionMenu(*args, **kwargs):
    pass


def symbolButton(*args, **kwargs):
    pass


def menuEditor(*args, **kwargs):
    pass


def polyColorDel(*args, **kwargs):
    pass


def createRenderLayer(*args, **kwargs):
    pass


def reverseCurve(*args, **kwargs):
    pass


def manipScaleContext(*args, **kwargs):
    pass


def MentalRayLogfileRender(*args, **kwargs):
    pass


def scrollField(*args, **kwargs):
    pass


def imageWindowEditor(*args, **kwargs):
    pass


def polyHelix(*args, **kwargs):
    pass


def shelfButton(*args, **kwargs):
    pass


def group(*args, **kwargs):
    pass


def arrayMapper(*args, **kwargs):
    pass


def userCtx(*args, **kwargs):
    pass


def animLayer(*args, **kwargs):
    pass


def sets(*args, **kwargs):
    pass


def savePrefs(*args, **kwargs):
    pass


def iconTextScrollList(*args, **kwargs):
    pass


def rowLayout(*args, **kwargs):
    pass


def uiTemplate(*args, **kwargs):
    pass


def polyStraightenUVBorder(*args, **kwargs):
    pass


def iconTextRadioButton(*args, **kwargs):
    pass


def iconTextCheckBox(*args, **kwargs):
    pass


def rampColorPort(*args, **kwargs):
    pass


def radioButton(*args, **kwargs):
    pass


def polySoftEdge(*args, **kwargs):
    pass


def gradientControl(*args, **kwargs):
    pass


def turbulence(*args, **kwargs):
    pass


def polySewEdge(*args, **kwargs):
    pass


def toolButton(*args, **kwargs):
    pass


def flowLayout(*args, **kwargs):
    pass


def projectCurve(*args, **kwargs):
    pass


def timeControl(*args, **kwargs):
    pass


def floatSlider(*args, **kwargs):
    pass


def getClassification(*args, **kwargs):
    pass


def attrFieldSliderGrp(*args, **kwargs):
    pass


def addPP(*args, **kwargs):
    pass


def picture(*args, **kwargs):
    pass


def GpuCacheExportAllOptions(*args, **kwargs):
    pass


def attrEnumOptionMenuGrp(*args, **kwargs):
    pass


def expression(*args, **kwargs):
    pass


def tangentConstraint(*args, **kwargs):
    pass


def dagPose(*args, **kwargs):
    pass


def transferAttributes(*args, **kwargs):
    pass


def AlembicExportSelection(*args, **kwargs):
    pass


def attachCurve(*args, **kwargs):
    pass


def polyPrism(*args, **kwargs):
    pass


def polyPlane(*args, **kwargs):
    pass


def polyMapCut(*args, **kwargs):
    pass


def polyOptUvs(*args, **kwargs):
    pass


def assignCommand(*args, **kwargs):
    pass


def polyTorus(*args, **kwargs):
    pass


def polyMoveVertex(*args, **kwargs):
    pass


def polyCloseBorder(*args, **kwargs):
    pass


def paneLayout(*args, **kwargs):
    pass


def polyAverageVertex(*args, **kwargs):
    pass


def orientConstraint(*args, **kwargs):
    pass


def optionMenu(*args, **kwargs):
    pass


def objectTypeUI(*args, **kwargs):
    """
    This command returns the type of UI element such as button, sliders, etc.
    
    Flags:
      - isType : i                     (unicode)       [create]
          Returns true|false if the object is of the specified type.
    
      - listAll : la                   (bool)          [create]
          Returns a list of all known UI commands and their respective types. Each entry contains three strings which are the
          command name, ui type and class name. Note that the class name is internal and is subject to change.
    
      - superClasses : sc              (bool)          [create]
          Returns a list of the names of all super classes for the given object. Note that all class names are internal and are
          subject to change.Flag can appear in Create mode of commandFlag can have multiple arguments, passed either as a tuple or
          a list.
    
    
    Derived from mel command `maya.cmds.objectTypeUI`
    """

    pass


def scrollLayout(*args, **kwargs):
    pass


def shelfLayout(*args, **kwargs):
    pass


def nameCommand(*args, **kwargs):
    pass


def detachSurface(*args, **kwargs):
    pass


def cameraSet(*args, **kwargs):
    pass


def commandPort(*args, **kwargs):
    pass


def MentalRayCustomTextEditor(*args, **kwargs):
    pass


def listAnimatable(*args, **kwargs):
    pass


def cmdScrollFieldExecuter(*args, **kwargs):
    pass


def roundConstantRadius(*args, **kwargs):
    pass


def window(*args, **kwargs):
    pass


def clipSchedulerOutliner(*args, **kwargs):
    pass


def webBrowser(*args, **kwargs):
    pass


def volumeAxis(*args, **kwargs):
    pass


def blendShapePanel(*args, **kwargs):
    pass


def psdChannelOutliner(*args, **kwargs):
    """
    Dynamic library stub function
    """

    pass


def subdMapSewMove(*args, **kwargs):
    pass


def polyBlindData(*args, **kwargs):
    pass


def flushUndo(*args, **kwargs):
    pass


def confirmDialog(*args, **kwargs):
    pass


def spotLightPreviewPort(*args, **kwargs):
    pass


def soundControl(*args, **kwargs):
    pass


def normalConstraint(*args, **kwargs):
    pass


def layeredShaderPort(*args, **kwargs):
    pass


def modelEditor(*args, **kwargs):
    pass


def rotate(*args, **kwargs):
    pass


def jointCluster(*args, **kwargs):
    pass


def layout(*args, **kwargs):
    pass


def menuBarLayout(*args, **kwargs):
    pass


def keyframeStats(*args, **kwargs):
    pass


def imagePlane(*args, **kwargs):
    pass


def ikSystem(*args, **kwargs):
    pass


def undoInfo(*args, **kwargs):
    pass


def removeWrappedCmd(cmdname):
    pass


def iconTextRadioCollection(*args, **kwargs):
    pass


def polyEditEdgeFlow(*args, **kwargs):
    pass


def hyperPanel(*args, **kwargs):
    pass


def attributeMenu(*args, **kwargs):
    pass


def progressBar(*args, **kwargs):
    pass


def adskAssetListUI(*args, **kwargs):
    pass


def poleVectorConstraint(*args, **kwargs):
    pass


def artUserPaintCtx(*args, **kwargs):
    pass


def SelectedAnimLayer(*args, **kwargs):
    pass


def joint(*args, **kwargs):
    pass


def draggerContext(*args, **kwargs):
    pass


def GpuCacheImport(*args, **kwargs):
    pass


def reverseSurface(*args, **kwargs):
    pass


def character(*args, **kwargs):
    pass


def AlembicExportAll(*args, **kwargs):
    pass


def loadPlugin(*args, **kwargs):
    pass


def renderer(*args, **kwargs):
    pass


def polyLayoutUV(*args, **kwargs):
    pass


def polyCut(*args, **kwargs):
    pass


def headsUpDisplay(*args, **kwargs):
    pass


def hotBox(*args, **kwargs):
    pass


def art3dPaintCtx(*args, **kwargs):
    pass


def addAttr(*args, **kwargs):
    pass


def ambientLight(*args, **kwargs):
    pass


def polyNormal(*args, **kwargs):
    pass


def editMetadata(*args, **kwargs):
    pass


def repeatLast(*args, **kwargs):
    pass


def dynPaintEditor(*args, **kwargs):
    pass


def keyframeOutliner(*args, **kwargs):
    pass


def callbacks(*args, **kwargs):
    pass


def nBase(*args, **kwargs):
    pass


def listSets(*args, **kwargs):
    pass


def rebuildCurve(*args, **kwargs):
    pass


def gradientControlNoAttr(*args, **kwargs):
    pass


def polySphere(*args, **kwargs):
    pass


def polyFlipEdge(*args, **kwargs):
    pass


def globalStitch(*args, **kwargs):
    pass


def timePort(*args, **kwargs):
    pass


def air(*args, **kwargs):
    pass


def assembly(*args, **kwargs):
    pass


def textureWindow(*args, **kwargs):
    pass


def flexor(*args, **kwargs):
    pass


def polyBevel(*args, **kwargs):
    pass


def textFieldGrp(*args, **kwargs):
    pass


def offsetCurve(*args, **kwargs):
    pass


def addDynamic(*args, **kwargs):
    pass


def fileInfo(*args, **kwargs):
    pass


def defaultLightListCheckBox(*args, **kwargs):
    pass


def manipRotateContext(*args, **kwargs):
    pass


def choice(*args, **kwargs):
    pass


def quit(*args, **kwargs):
    pass


def arclen(*args, **kwargs):
    pass


def AlembicOpen(*args, **kwargs):
    pass


def pairBlend(*args, **kwargs):
    pass


def polyProjectCurve(*args, **kwargs):
    pass


def getMelRepresentation(args, recursionLimit=None, maintainDicts=True):
    """
    Will return a list which contains each element of the iterable 'args' converted to a mel-friendly representation.
    
    :Parameters:
        recursionLimit : int or None
            If an element of args is itself iterable, recursionLimit specifies the depth to which iterable elements
            will recursively search for objects to convert; if ``recursionLimit==0``, only the elements
            of args itself will be searched for PyNodes -  if it is 1, iterables within args will have getMelRepresentation called
            on them, etc.  If recursionLimit==None, then there is no limit to recursion depth.
    
        maintainDicts : bool
            In general, all iterables will be converted to tuples in the returned copy - however, if maintainDicts==True,
            then iterables for which ``util.isMapping()`` returns True will be returned as dicts.
    """

    pass


def polyCopyUV(*args, **kwargs):
    pass


def preloadRefEd(*args, **kwargs):
    pass


def softMod(*args, **kwargs):
    pass


def eval(*args, **kwargs):
    """
    Dynamic library stub function
    """

    pass


def outlinerEditor(*args, **kwargs):
    pass


def optionMenuGrp(*args, **kwargs):
    pass


def hyperGraph(*args, **kwargs):
    pass


def insertKnotSurface(*args, **kwargs):
    pass


def scriptTable(*args, **kwargs):
    pass


def scaleConstraint(*args, **kwargs):
    pass


def ls(*args, **kwargs):
    pass


def componentBox(*args, **kwargs):
    pass


def colorSliderGrp(*args, **kwargs):
    pass


def setParent(*args, **kwargs):
    pass


def listHistory(*args, **kwargs):
    pass


def cmdScrollFieldReporter(*args, **kwargs):
    pass


def listAttr(*args, **kwargs):
    pass


def closeCurve(*args, **kwargs):
    pass


def polyInstallAction(*args, **kwargs):
    pass


def blendTwoAttr(*args, **kwargs):
    pass


def fileBrowserDialog(*args, **kwargs):
    pass


def bezierCurveToNurbs(*args, **kwargs):
    pass


def polyUVRectangle(*args, **kwargs):
    pass


def polyQuad(*args, **kwargs):
    pass


def batchRender(*args, **kwargs):
    pass


def nodeTreeLister(*args, **kwargs):
    pass


def switchTable(*args, **kwargs):
    pass


def modelPanel(*args, **kwargs):
    pass


def nodeEditor(*args, **kwargs):
    pass


def messageLine(*args, **kwargs):
    pass


def sequenceManager(*args, **kwargs):
    pass


def nameField(*args, **kwargs):
    pass


def mute(*args, **kwargs):
    pass


def attrNavigationControlGrp(*args, **kwargs):
    pass


def keyingGroup(*args, **kwargs):
    pass


def untrim(*args, **kwargs):
    pass


def ikSolver(*args, **kwargs):
    pass


def jointLattice(*args, **kwargs):
    pass


def hyperShade(*args, **kwargs):
    pass


def attrFieldGrp(*args, **kwargs):
    pass


def treeLister(*args, **kwargs):
    pass


def hotkey(*args, **kwargs):
    pass


def attrColorSliderGrp(*args, **kwargs):
    pass


def swatchDisplayPort(*args, **kwargs):
    pass


def saveImage(*args, **kwargs):
    pass


def intSlider(*args, **kwargs):
    pass


def keyframe(*args, **kwargs):
    pass


def runTimeCommand(*args, **kwargs):
    pass


def revolve(*args, **kwargs):
    pass


def AlembicImport(*args, **kwargs):
    pass


def reference(*args, **kwargs):
    pass


def polyDelFacet(*args, **kwargs):
    pass


def polyMoveUV(*args, **kwargs):
    pass


def popupMenu(*args, **kwargs):
    pass


def polyColorMod(*args, **kwargs):
    pass


def annotate(*args, **kwargs):
    pass


def addWrappedCmd(cmdname, cmd=None):
    pass


def angleBetween(*args, **kwargs):
    pass


def radioMenuItemCollection(*args, **kwargs):
    pass


def radioCollection(*args, **kwargs):
    pass


def canvas(*args, **kwargs):
    pass


def polySmooth(*args, **kwargs):
    pass


def referenceEdit(*args, **kwargs):
    pass


def polySplitEdge(*args, **kwargs):
    pass


def radioButtonGrp(*args, **kwargs):
    pass


def toolCollection(*args, **kwargs):
    pass


def polySeparate(*args, **kwargs):
    pass


def polyUnite(*args, **kwargs):
    pass


def polySelectConstraintMonitor(*args, **kwargs):
    pass


def timeWarp(*args, **kwargs):
    pass


def floatSliderButtonGrp(*args, **kwargs):
    pass


def intField(*args, **kwargs):
    pass


def floatField(*args, **kwargs):
    pass


def polyCylinder(*args, **kwargs):
    pass


def file(*args, **kwargs):
    pass


def particle(*args, **kwargs):
    pass


def pointLight(*args, **kwargs):
    pass


def layoutDialog(*args, **kwargs):
    pass


def floatSlider2(*args, **kwargs):
    pass


def hwReflectionMap(*args, **kwargs):
    pass


def cylinder(*args, **kwargs):
    pass


def nParticle(*args, **kwargs):
    pass


def projectTangent(*args, **kwargs):
    pass


def polyDelVertex(*args, **kwargs):
    pass


def textScrollList(*args, **kwargs):
    pass


def polyPoke(*args, **kwargs):
    pass


def plane(*args, **kwargs):
    pass


def fitBspline(*args, **kwargs):
    pass


def textFieldButtonGrp(*args, **kwargs):
    pass


def iconTextButton(*args, **kwargs):
    pass


def polyCrease(*args, **kwargs):
    pass


def polyTransfer(*args, **kwargs):
    pass


def polyMapSew(*args, **kwargs):
    pass


def EmptyAnimLayer(*args, **kwargs):
    pass


def palettePort(*args, **kwargs):
    pass


def polyAppendVertex(*args, **kwargs):
    pass


def text(*args, **kwargs):
    pass


def outlinerPanel(*args, **kwargs):
    pass


def GpuCacheExportSelection(*args, **kwargs):
    pass


def optionVar(*args, **kwargs):
    pass


def disconnectAttr(*args, **kwargs):
    pass


def currentTime(*args, **kwargs):
    pass


def selectKeyframe(*args, **kwargs):
    pass


def showManipCtx(*args, **kwargs):
    pass


def shot(*args, **kwargs):
    pass


def scriptedPanel(*args, **kwargs):
    pass


def shadingNode(*args, **kwargs):
    pass


def lsThroughFilter(*args, **kwargs):
    pass


def extrude(*args, **kwargs):
    pass


def AlembicExportSelectionOptions(*args, **kwargs):
    pass


def columnLayout(*args, **kwargs):
    pass


def selectionConnection(*args, **kwargs):
    pass


def cmdShell(*args, **kwargs):
    pass


def extendCurve(*args, **kwargs):
    pass


def button(*args, **kwargs):
    pass


def closeSurface(*args, **kwargs):
    pass


def parent(*args, **kwargs):
    pass


def intFieldGrp(*args, **kwargs):
    pass


def vortex(*args, **kwargs):
    pass


def _testDecorator(function):
    pass


def AlembicImportOptions(*args, **kwargs):
    pass


def exclusiveLightCheckBox(*args, **kwargs):
    pass


def deformer(*args, **kwargs):
    pass


def polyWedgeFace(*args, **kwargs):
    pass


def bevel(*args, **kwargs):
    pass


def subdCleanTopology(*args, **kwargs):
    pass


def panel(*args, **kwargs):
    pass


def spring(*args, **kwargs):
    pass


def nurbsCube(*args, **kwargs):
    pass


def shelfTabLayout(*args, **kwargs):
    pass


def spaceLocator(*args, **kwargs):
    pass


def nodeType(*args, **kwargs):
    pass


def menuItem(*args, **kwargs):
    pass


def MentalRayLogfileBatch(*args, **kwargs):
    pass


def iconTextStaticLabel(*args, **kwargs):
    pass


def treeView(*args, **kwargs):
    pass


def hudSliderButton(*args, **kwargs):
    pass


def hotkeyCheck(*args, **kwargs):
    pass


def dropoffLocator(*args, **kwargs):
    pass


def dockControl(*args, **kwargs):
    pass


def flow(*args, **kwargs):
    pass


def layeredTexturePort(*args, **kwargs):
    pass


def rigidBody(*args, **kwargs):
    pass


def smoothCurve(*args, **kwargs):
    pass


def help(*args, **kwargs):
    pass


def flagTest(*args, **kwargs):
    pass


def grid(*args, **kwargs):
    pass


def artAttrCtx(*args, **kwargs):
    pass


def arcLengthDimension(*args, **kwargs):
    pass


def gravity(*args, **kwargs):
    pass


def polyAppend(*args, **kwargs):
    pass


def animCurveEditor(*args, **kwargs):
    pass


def GpuCacheExportAll(*args, **kwargs):
    pass


def alignCurve(*args, **kwargs):
    pass


def instancer(*args, **kwargs):
    pass


def polyPrimitive(*args, **kwargs):
    pass


def polyPlatonicSolid(*args, **kwargs):
    pass


def rename(*args, **kwargs):
    pass


def characterMap(*args, **kwargs):
    pass


def AlembicExportAllOptions(*args, **kwargs):
    pass


def referenceQuery(*args, **kwargs):
    pass


def frameLayout(*args, **kwargs):
    pass


def polySplitRing(*args, **kwargs):
    pass


def rangeControl(*args, **kwargs):
    pass


def symbolCheckBox(*args, **kwargs):
    pass


def polyMapDel(*args, **kwargs):
    pass


def polyExtrudeEdge(*args, **kwargs):
    pass


def floatSliderGrp(*args, **kwargs):
    pass


def polyConnectComponents(*args, **kwargs):
    pass


def pluginInfo(*args, **kwargs):
    pass


def floatFieldGrp(*args, **kwargs):
    pass


def polyCollapseEdge(*args, **kwargs):
    pass


def polyMoveFacetUV(*args, **kwargs):
    pass


def container(*args, **kwargs):
    pass


def filletCurve(*args, **kwargs):
    pass


def polyMoveEdge(*args, **kwargs):
    pass


def paramDimension(*args, **kwargs):
    pass


def polyMergeUV(*args, **kwargs):
    pass


def camera(*args, **kwargs):
    pass


def polyMergeEdge(*args, **kwargs):
    pass


def polyMapSewMove(*args, **kwargs):
    pass


def polyPyramid(*args, **kwargs):
    pass


def prepareRender(*args, **kwargs):
    pass


def polyBridgeEdge(*args, **kwargs):
    pass


def polyPipe(*args, **kwargs):
    pass


def polyFlipUV(*args, **kwargs):
    pass


def polyNormalPerVertex(*args, **kwargs):
    pass


def event(*args, **kwargs):
    pass


def polyChipOff(*args, **kwargs):
    pass


def snapshot(*args, **kwargs):
    pass


def cone(*args, **kwargs):
    pass


def scriptedPanelType(*args, **kwargs):
    pass


def devicePanel(*args, **kwargs):
    pass


def layerButton(*args, **kwargs):
    pass


def detachCurve(*args, **kwargs):
    pass


def AlembicHelp(*args, **kwargs):
    pass


def lsUI(*args, **kwargs):
    pass


def circle(*args, **kwargs):
    pass


def condition(*args, **kwargs):
    pass


def AlembicReplace(*args, **kwargs):
    pass


def addAllWrappedCmds():
    pass


def surface(*args, **kwargs):
    pass


def cluster(*args, **kwargs):
    pass


def boneLattice(*args, **kwargs):
    pass


def polyDuplicateEdge(*args, **kwargs):
    pass


def blendShape(*args, **kwargs):
    pass


def geometryConstraint(*args, **kwargs):
    pass


def bevelPlus(*args, **kwargs):
    pass


def formLayout(*args, **kwargs):
    pass


def pointPosition(*args, **kwargs):
    pass


def control(*args, **kwargs):
    pass


def nurbsSquare(*args, **kwargs):
    pass


def stroke(*args, **kwargs):
    pass


def sculpt(*args, **kwargs):
    pass


def sphere(*args, **kwargs):
    pass


def createNode(*args, **kwargs):
    pass


def nurbsToSubdiv(*args, **kwargs):
    pass


def nodeIconButton(*args, **kwargs):
    pass


def namespaceInfo(*args, **kwargs):
    pass


def menuSet(*args, **kwargs):
    pass


def channelBox(*args, **kwargs):
    pass


def partition(*args, **kwargs):
    pass


def shadingLightRelCtx(*args, **kwargs):
    pass


def shadingGeometryRelCtx(*args, **kwargs):
    pass


def scriptCtx(*args, **kwargs):
    pass


def cameraView(*args, **kwargs):
    pass


def uniform(*args, **kwargs):
    pass


def ikHandle(*args, **kwargs):
    pass


def polyCube(*args, **kwargs):
    pass


def trim(*args, **kwargs):
    pass


def attrControlGrp(*args, **kwargs):
    pass


def tabLayout(*args, **kwargs):
    pass


def torus(*args, **kwargs):
    pass


def scale(*args, **kwargs):
    pass


def subdLayoutUV(*args, **kwargs):
    pass


def delete(*args, **kwargs):
    pass


def duplicate(*args, **kwargs):
    pass


def drag(*args, **kwargs):
    pass


def rigidSolver(*args, **kwargs):
    pass


def listRelatives(*args, **kwargs):
    pass


def colorSliderButtonGrp(*args, **kwargs):
    pass


def renderWindowEditor(*args, **kwargs):
    pass


def subdiv(*args, **kwargs):
    pass


def colorEditor(*args, **kwargs):
    pass


def polyExtrudeVertex(*args, **kwargs):
    pass


def helpLine(*args, **kwargs):
    pass


def hardwareRenderPanel(*args, **kwargs):
    pass


def promptDialog(*args, **kwargs):
    pass


def gridLayout(*args, **kwargs):
    pass


def aimConstraint(*args, **kwargs):
    pass


def wire(*args, **kwargs):
    pass


def GpuCacheImportOptions(*args, **kwargs):
    pass


def emitter(*args, **kwargs):
    pass


def alignSurface(*args, **kwargs):
    pass


def curve(*args, **kwargs):
    pass


def intSliderGrp(*args, **kwargs):
    pass


def dynGlobals(*args, **kwargs):
    pass


def separator(*args, **kwargs):
    pass


def attachSurface(*args, **kwargs):
    pass


def rowColumnLayout(*args, **kwargs):
    pass


def setAttr(*args, **kwargs):
    pass



objectErrorReg = None


