"""
Author: jason
Created: Jun 20, 2012
Module: maya.core.mayaCore
Purpose: Super class and foundational Maya utility library
"""

from common.core import globalVariables as gv
from common.diagnostic import pcsLogger
from common.fileIO import parser_schema, pcsPath, fileManip
from copy import copy  # @UnusedImport
from pymel.all import *  # @UnusedWildImport
from pymel.internal.plogging import pymelLogger  # @Reimport
from re import search
import getpass  # @Reimport
import time


# noinspection PyMethodMayBeStatic
class Maya(object):
    """
    Super (super) class and foundational Maya utility library
    """

    def __init__(self):
        """ Maya.__init__():  set initial parameters """
        super(Maya, self).__init__()

        #maya info
        self.mayaVer = self.getMayaVersion()  # has to be first, 'cause it is read in other methods

        # make logger
        self.logger = None
        self.setLogger()

    @property
    def teamA(self):
        return gv.teamA

    @property
    def teamB(self):
        return gv.teamB

    def getMayaVersion(self, strVersion=0):
        """
        SYNOPSIS: Returns application version

        INPUTS:	stringVersion of version number (default false

        RETURNS: (float/string)	application version
        """

        if search('x64', about(version=1)):
            if strVersion:
                return about(version=1).split(' ')[0]
            else:
                return float(about(version=1).split(' ')[0])
        else:
            if strVersion:
                return about(version=1)
            else:
                return float(about(version=1))

    def makeLogger(self, filePathName='%s/data/%s/%s.log' % (gv.logLocation, getpass.getuser(), getpass.getuser()),
                   name='pcsLogger', fresh=0):
        """
        SYNOPSIS
         returns a new logger for diagnostics.apLogger.pcsLogger()

        INPUTS
        (string) 	filePathName:	path and file name of FileHandler stream
         (string) 			name:	'handle' to logger object
         (bool) 			   fresh:	1 = tries to delete old log file


        RETURNS: (logging.Logger) logger object
        """
        return pcsLogger.pcs_logger(filePathName, pymelLogger, name, fresh)

    def setLogger(self, filePathName='%s/data/%s/%s.log' % (gv.logLocation, getpass.getuser(), getpass.getuser()),
                  name='pcsLogger', fresh=0):
        """
        SYNOPSIS
         sets mCore.logger to a path and sets its name
         NOTE: There can only be 1 of these at a time! If you want another logger,
                 you should use MayaCore.makeLogger() or diagnostics.apLogger.pcsLogger()

        INPUTS
        (string) 	filePathName:	path and file name of FileHandler stream
         (string) 			name:	'handle' to logger object
         (bool) 			   fresh:	1 = tries to delete old log file


        RETURNS: nothing
        """
        self.logger = pcsLogger.pcs_logger(filePathName=filePathName, name=name, fresh=fresh)

    def getEnv(self, sPrint=1, unformattedReturn=0):
        """
        NAME: getEnv

        SYNOPSIS
         prints all needed paths

        INPUTS	nothing

        RETURNS: none
        """
        scriptPaths = mel.getenv("MAYA_SCRIPT_PATH")
        plugInPaths = mel.getenv("MAYA_PLUG_IN_PATH")
        pythonPaths = mel.getenv("PYTHONPATH")
        iconPaths = mel.getenv("XBMLANGPATH")
        pathPaths = mel.getenv("PATH")
        sysPaths = sys.path
        envReturn = []
        splitString = ';'
        if os.name == 'posix':
            splitString = ':'

        allPythonPaths = pythonPaths.split(splitString)
        envReturn.append("PYTHONPATHs are:\n")
        for pythonPath in allPythonPaths:
            envReturn.append('%s\n' % pythonPath)

        allIconPaths = iconPaths.split(splitString)
        envReturn.append("\nXBMLANGPATH are:\n")
        for iconPath in allIconPaths:
            envReturn.append('%s\n' % iconPath)

        allPathPaths = pathPaths.split(splitString)
        envReturn.append("\nPATHs are:\n")
        for pathPath in allPathPaths:
            envReturn.append('%s\n' % pathPath)

        envReturn.append("\nsys.paths are:\n")
        for sysPath in sysPaths:
            envReturn.append('%s\n' % sysPath)

        allScriptPaths = scriptPaths.split(splitString)
        envReturn.append("\nMAYA_SCRIPT_PATHs are:\n")
        for scriptPath in allScriptPaths:
            envReturn.append('%s\n' % scriptPath)

        allPlugInPaths = plugInPaths.split(splitString)
        envReturn.append("\nMAYA_PLUG_IN_PATH are:\n")
        for plugInPath in allPlugInPaths:
            envReturn.append('%s\n' % plugInPath)

        if sPrint:
            print '\n'
            pArr = [pArr for pArr in envReturn if pArr.strip()]
            for p in pArr:
                if p.split('\n')[0]:
                    print p.split('\n')[0]
                elif p.split('\n')[1] != '':
                    print '\n'
                    print p.split('\n')[1]
        else:
            if unformattedReturn:
                pArr = [pArr for pArr in envReturn if pArr.strip()]
                uReturn = []
                for l in pArr:
                    if l != '':
                        uReturn.append(str(l.replace('\n', '')))
                return uReturn
            else:
                return envReturn

    def getMayaEnvFile(self):
        """ Return path to local env file """
        return pcsPath.Path(about(environmentFile=True))

    def getMayaUserSetupFile(self):
        """ Return path to local user setup file """
        usf = '%s%s' % (cmds.internalVar(userScriptDir=True), 'userSetup.mel')
        return pcsPath.Path(usf)

    def loadPlugIn(self, plugName):
        """ Tries to load passed plugin"""
        result = 1

        if not cmds.pluginInfo(plugName, q=True, l=True):
            cmds.loadPlugin(plugName)
            result = cmds.pluginInfo(plugName, q=True, l=True)

        return result


#	def verifyP4(self):
#		try:
#			dir(self.p4)
#		except:
#			from perforce import apP4
#			self.p4 = apP4.P4Lib()

class MayaPrintCore(Maya):
    """
    Super (super) class and foundational Maya utility library
    """

    def __init__(self):
        """ MayaPrintCore.__init__():  set initial parameters """
        super(MayaPrintCore, self).__init__()

    def debugInfo(self, loud, text, title=''):
        """
        SYNOPSIS: gives debug and confirmation dialogue options

        INPUTS
         (int) 		loud:	0=off, 1=print, 2=confirmDialogue
         (string) 	text:	text to print
         (string) 	title:	title to print

        RETURNS: nothing
        """
        if not self.logger:
            self.setLogger()
        self.logger.debug(text)
        if loud == 1:
            print"\ndebugInfo:	%s\n" % text
        cmds.refresh()

        if loud == 2:
            result = cmds.confirmDialog(t="Debug Info: %s" % title, m=text, b=['OK', 'Cancel'], db='OK', cb='Cancel',
                                        ds='Cancel');
            if result == "Cancel":
                print "*** Canceled ***"
                sys.exit()


# noinspection PyMethodMayBeStatic
class MayaSceneCore(Maya):
    ##################################################################################################################################
    #	Note:	These methods should FIRST use the metaNetwork to find the information needed
    #			THEN go to hierarchy traversal as a backup																			##
    ##################################################################################################################################

    def __init__(self):
        """ MayaSceneCore.__init__():  set initial parameters """
        super(MayaSceneCore, self).__init__()

    def getAllControls(self, ns=None):
        """
        SYNOPSIS
         searches and tries to find set called 'allControls'
         and selects it

        INPUTS:	* = optional
            (string)	ns*:	optional namespace

        RETURNS: (string)	name of allControls set
        """

        allControls = None
        setName = 'allControls'
        if ns:
            setName = '%s:%s' % (ns, setName)

        if objExists(setName):
            allControls = setName
        else:
            for oSet in ls(type='objectSet'):
                if re.search(setName, oSet):
                    allControls = oSet

        if objExists(allControls):
            select(allControls)
        else:
            self.logger.warning("%s set doesn't exists in scene." % setName)

        return allControls

    def getTopGroups(self):
        # find topGroups
        topGroups = [grp for grp in ls(type='transform') if not grp.getParent() and not grp.getShape()]

        # remove cameras
        newTopGroups = []
        if self.mayaVer >= 2011:
            newTopGroups = copy.copy(topGroups)
        else:
            newTopGroups = copy(topGroups)
        for cam in topGroups:
            # check for dupes
            for child in cam.getChildren():
                self.check4Dup(child, 1, '. Suggest deleting history')
            if len(cam.getChildren()) == 1 and objectType(cam.getChildren()) == 'camera':
                newTopGroups.remove(cam)
        return newTopGroups

    def getFosterParents(self):
        """ Parse the scene and return all foster parent nodes """
        fParents = []
        tNodes = ls(type='transform')
        if tNodes:
            for e in tNodes:
                if re.search('fosterParent', e.name()):
                    fParents.append(e)
        if fParents:
            return fParents

    def getMeshGrps(self, meshes=0):
        """
        SYNOPSIS
         Parses scene for groups contain actor/environment meshes

        INPUTS
         (bool)	meshes:	return all meshes instead of groups

        RETURNS:
         (list) meshGrps
         or
         (list) allMeshes

        """
        # find mesh groups
        meshGrps = []
        allMeshes = []
        for grp in self.getTopGroups():
            for child in self.meshesInGroup(grp):
                if isinstance(child, nt.Mesh) or re.search('lod', child.name(), re.I):
                    meshGrps.append(Transform(grp))
                    allMeshes.append(child)
        assert (len(meshGrps) > 0), "Could not find mesh group in scene. Missing 'lod0' suffix?"

        if meshes:
            assert (len(allMeshes) > 0), 'No actor meshes found'
            return allMeshes
        return meshGrps

    def getActorMeshes(self):
        # return each mesh in all meshGroups
        return self.getMeshGrps(1)

    def getDefaultExportMeshes(self):
        """ Method to gather default export meshes (in the absence of anything selected) """

        # First Attempt to find top groups with the _gr naming convention
        grGrps = []
        eMeshes = []

        # Look for groups with the '_gr' naming
        for grp in [grp for grp in self.getTopGroups() if self.getTopGroups()]:
            if re.search('_gr', grp.name(), re.I):
                grGrps.append(grp)

        # If groups exist in the scene with the '_gr' naming
        if grGrps:
            for g in grGrps:
                for msh in [msh for msh in self.meshesInGroup(g) if self.meshesInGroup(g)]:
                    # Append any meshes with lod0
                    if re.search('_lod0', msh.name(), re.I):
                        eMeshes.append(msh)

        # Fall back, scrape the scene for meshes with 'lod0' name
        else:
            for msh in [msh for msh in self.gimmeMeshes() if self.gimmeMeshes()]:
                if re.search('_lod0', msh.name(), re.I):
                    eMeshes.append(msh)

        if eMeshes:
            return eMeshes
        else:
            self.logger.error('Failed to find any valid export meshes')

    def getRigRootObj(self):
        # find rig root group
        for grp in self.getTopGroups():
            for child in grp.getChildren():
                if isinstance(child, nt.Joint):
                    return Transform(grp)

    def getRigRootJoint(self):
        """ Return the rig root joint. """
        topGrp = self.getRigRootObj()
        for child in [child for child in topGrp.getChildren() if isinstance(child, nt.Joint)]:
            if objectType(child) == 'joint':
                return child

    def getFBIKcharacter(self):
        #for grp in self.getTopGroups():
        for char in ls(type='character'):
            if char.name()[char.name().rfind(':') + 1:] == 'fbikCharacter':
                return char

    def getSkeletonObj(self):
        # find rig root group
        for grp in self.getTopGroups():
            for child in grp.getChildren():
                #if objectType(child) == 'joint': return child
                if isinstance(child, nt.Joint):
                    return child

    def getLocatorObj(self):
        rigRoot = self.getRigRootObj()

        # find rig root group
        for grp in rigRoot.getChildren():
            if grp == 'doNotTouch':
                for child in grp.getChildren():
                    if objectType(child) == 'transform' and child == 'locator_buildHelpers':
                        return child

    def getSceneBaseName(self, extension=0):
        """ Return just the scene name string from unique file id"""
        if (extension):
            return sceneName().name
        else:
            return sceneName().namebase

    def parentSingleNode(self, child, prnt):
        """
        NAME: parentSingleNode

        SYNOPSIS
         This is a simple wrapper for MEL's "parent" command that
         conveniently returns a single string.

        INPUTS
         (string) child:  The child node.
         (string) prnt:  The parent node.

        RETURNS: (string)  The name of the child node.
        """

        result = PyNode(parent(child, prnt)[0])
        return result


class MayaNodeCore(Maya):
    ##################################################################################################################################
    #	Node Class																													##
    ##################################################################################################################################

    def __init__(self):
        """ MayaSceneCore.__init__():  set initial parameters """
        super(MayaNodeCore, self).__init__()

    def isGroup(self, node):
        """ Checks if the passed node is of type group """
        node = self.convertToPyNode(node)
        if nodeType(node) == 'transform' and not node.getShapes():
            return 1;
        else:
            return 0

    def isMesh(self, node):
        """ Checks if the passed node is of type mesh """
        node = self.convertToPyNode(node)
        if nodeType(node) == 'transform':
            if nodeType(node.getShape()) == 'mesh':
                return 1
            else:
                return 0


class MayaMiscCore(Maya):
    ##################################################################################################################################
    ##	Generic methods																												##
    ##################################################################################################################################

    def __init__(self):
        """ MayaMiscCore.__init__():  set initial parameters """
        super(MayaMiscCore, self).__init__()


    @staticmethod
    def addAttr(object_, attributes):

        #attributes = [{'attrName':'elbowTwist','type':'double','min':'','max':'','default':''},{'attrName':'ikBlend','type':'double','min':'0','max':'1','default':'0'}]
        # adds attributes to control
        for attribute in attributes:
            object_.addAttr(attribute['attrName'], at=attribute['type'], k=1)

            # sets min if applicable
            if attribute['min']:
                addAttr('%s.%s' % (object_, attribute['attrName']), e=1, minValue=float(attribute['min']))

            # sets max if applicable
            if attribute['max']:
                addAttr('%s.%s' % (object_, attribute['attrName']), e=1, maxValue=float(attribute['max']))

            # sets default if applicable
            if attribute['default']:
                object_.attr(attribute['attrName']).set(float(attribute['default']))

    def average(self, evalNodes):
        """
        SYNOPSIS
         Calculate the mathematical average position of passed nodes or components

        INPUTS
         (string?/PyNode?) evalNodes:	list of components or nodes

        RETURNS: (float list) average position
         """

        if not evalNodes:
            evalNodes = selected(fl=1)

        select(cl=1)
        filteredEval = []
        if evalNodes:
            for e in evalNodes:
                select(e, r=1)
                if len(e.split('.')) > 1:
                    if not search('MeshVertex', str(type(e))):
                        mel.ConvertSelectionToVertices()
                        for a in selected(fl=1):
                            filteredEval.append(a)
                        select(cl=1)
                    else:
                        filteredEval.append(e)
                else:
                    if nodeType(e) == 'transform':
                        filteredEval.append(e)

        if filteredEval:
            divFactor = float(len(filteredEval))

            xComp = float(0.0000)
            yComp = float(0.0000)
            zComp = float(0.0000)
            for each in filteredEval:
                # Branch component items here
                if len(each.split('.')) > 1:
                    xComp = xComp + float(each.getPosition('world')[0])
                    yComp = yComp + float(each.getPosition('world')[1])
                    zComp = zComp + float(each.getPosition('world')[2])
                else:
                    if nodeType(each) == 'transform':
                        xComp = xComp + float(each.getTranslation('world')[0])
                        yComp = yComp + float(each.getTranslation('world')[1])
                        zComp = zComp + float(each.getTranslation('world')[2])
            self.logger.debug('X - %s' % xComp)
            self.logger.debug('Y - %s' % yComp)
            self.logger.debug('Z - %s' % zComp)
            self.logger.debug('X Result - %s' % str(xComp / divFactor))
            self.logger.debug('Y Result - %s' % str(yComp / divFactor))
            self.logger.debug('Z Result - %s' % str(zComp / divFactor))

            return [xComp / divFactor, yComp / divFactor, zComp / divFactor]

    @property
    def mathAvgSelected(self):
        return self.average()

    @staticmethod
    def pyNodeString(node):
        """
        SYNOPSIS
         checks and converts to string

        INPUTS
         (string?/PyNode?) node:	node name

        RETURNS: (string) node
        """

        #if not re.search('pymel', str(node.__class__)):
        if re.search('pymel', str(node.__class__)):
            return node.name()
        else:
            return node

    def check4Dup(self, node, quit=0, message=''):  #@ReservedAssignment
        """
        SYNOPSIS
         checks for multiple nodes

        INPUTS
         (string) node:	node name
         (bool)	quit:	force quit if dup

        RETURNS: (bool) 1 if duplicate exists
        """
        # check for multiples
        if len(ls(node)) > 1:
            self.logger.warning("More than one object matches name%s: '%s'" % (message, node))
            select(ls(node), r=1)
            if quit:
                sys.exit()
            return 1

        return 0

    def cleaner(self, node, channels=['']):
        """
        SYNOPSIS
         locks and hides

        INPUTS
         (string) 		node:		node to lock
         ([strings]) channels:	channels to remain keyable

        RETURNS: nothing
        """
        # make sure not list
        if node.__class__ == list:
            node = node[0]

        # skip if node doesn't exist
        if not objExists(node):
            if objExists:
                pass
            self.logger.warning("metarigging.cleaner(): node '%s' doesn't exist, skipping cleaning" % node)
            return

        # convert to pyNode
        node = self.convertToPyNode(node)

        # gets current channel box info
        keyableList = listAttr(node, keyable=1)  # need to be locked and hidden
        nonKeyableList = listAttr(node, channelBox=1)  # need to be hidden

        # locks and hides unless in channel list
        if keyableList:
            for keyable in keyableList:
                if len(keyable.split('.')) == 1:
                    if channels.count(keyable) == 0:
                        setAttr('%s.%s' % (node, keyable), lock=True, keyable=False)

        # hides non-keyable
        if nonKeyableList:
            for nonKeyable in nonKeyableList:
                node.attr(nonKeyable).lock()
                node.attr(nonKeyable).showInChannelBox(0)

    def convertToPyNode(self, node):
        """
        SYNOPSIS: checks and converts to PyNode
        INPUTS: (string?/PyNode?) node:	node name
        RETURNS: (PyNode) node
        """

        if not self.isPyNode(node):
            if not node.__class__ == str and re.search('Meta', str(node)):
                return node  # pass Meta objects too
            return PyNode(node)
        else:
            return node

    @staticmethod
    def dateAsDecimal():
        tokenizedTime = time.localtime(time.time())
        month = tokenizedTime[1]
        day = tokenizedTime[2]
        if month < 10:
            month = '0%s' % month

        monthDay = '.%s%s' % (month, day)

        return float(monthDay)

    @staticmethod
    def isPyNode(node):
        """ Checks if node is of type pyNode """
        if re.search('pymel', str(node.__class__)):
            return 1
        else:
            return 0

    @staticmethod
    def isMetaNode(node):
        """ Checks if node is of type Meta """
        if re.search('Meta', str(node.__class__)):
            return 1
        else:
            return 0

    def copyWorldXform(self, source='', target=''):
        if not source:
            if len(selected()) == 2:
                source = selected()[0]
                target = selected()[1]
            else:
                self.logger.error('Please select or pass 2 objects')
        if not target:
            self.logger.error('Please select or pass 2 objects')

        xform(target, ws=1, t=source.getTranslation(ws=1))
        xform(target, ws=1, ro=source.getRotation(ws=1))

    @staticmethod
    def findAvailbleNodeName(nameBase, numberBase=3):
        """ Loops through and finds available node name for Maya scene"""
        nBase = 1
        strRep = fileManip.FileManip().strNumberGenerator(nBase, numberBase)
        while (objExists(nameBase.replace('@', strRep))):
            nBase = nBase + 1
            strRep = fileManip.FileManip().strNumberGenerator(nBase, numberBase)
        return nameBase.replace('@', strRep)

    def listcP(self, nodeWplug, quiet=0, all=0):  #@ReservedAssignment
        """
        SYNOPSIS
         Simple wrapper for listConnetions w/ plug

        INPUTS
         (PyNode.attr) mtNodeWPlug:  The metaNode.plug to look at connections.
         (bool)				quiet:	 1 = suppress warning
         (bool) 			  all:	 Return all connections

        RETURNS: (PyNode)  connected node via plug
        """
        try:
            if listConnections(nodeWplug):
                allConnections = listConnections(nodeWplug)
                if all:
                    return map(lambda x: PyNode(x), allConnections)
                return PyNode(allConnections[0])
        except:
            if not quiet:
                self.logger.warning("Nothing connected to '%s'" % nodeWplug)
            return 0

    @staticmethod
    def mi(node=''):
        """
        SYNOPSIS
         Freeze transforms

        INPUTS
         (string) node:	node name

        RETURNS: Nothing
        """

        if not node:
            makeIdentity(apply=True, s=1, r=1, t=1, n=0, jo=1)
        else:
            makeIdentity(node, apply=True, s=1, r=1, t=1, n=0, jo=1)

    def groupTo(self, mNode='', mGrp=''):
        """
        SYNOPSIS
         Move nodes to group, if no group is passed it parents the node to world

        INPUTS
         mNode*:	node name
         mGrp*:	group name

        RETURNS: Nothing
        """

        if mNode:
            mNode = self.convertToPyNode(mNode)
        else:
            if self.verifyMeshSelection():
                mNode = selected()[0]

        if mNode:
            if mGrp:
                mGrp = self.convertToPyNode(mGrp)
                if mNode.getParent():
                    if not mNode.getParent() == mGrp.name():
                        parent(mNode.name(), mGrp.name())
                    else:
                        self.logger.info('Node is already child of group')
                else:
                    parent(mNode.name(), mGrp.name())
            else:
                if mNode.getParent():
                    parent(mNode.name(), world=1)
                else:
                    self.logger.info('Node is already child of world')

    @staticmethod
    def pymelVersion():
        """
        SYNOPSIS
         looks for pymel version

        INPUTS	nothing

        RETURNS: version
        """
        version = 0.7
        if re.search('core.general', PyNode.__module__):
            version = 1.0
        return version


class MayaReferenceCore(Maya):
    ##################################################################################################################################
    ##	Reference methods																												##
    ##################################################################################################################################

    def __init__(self):
        """ MayaReferenceCore.__init__():  set initial parameters """
        super(MayaReferenceCore, self).__init__()

    def refreshRefs(self, node='', sync=1):
        """
        SYNOPSIS
         Method to refresh references

        INPUTS
         (str)*	node:	Pass a node and only act on the reference, the node belongs to. If the reference passed is nested, includeNested will be forced.
         (bool)* sync:	Sync P4 reference file

        RETURNS: Nothing
        """

        allRefs = self.getRefs(node=node)
        for er in allRefs:
            if sync:
                if self.apParseObj.isp4Active:
                    # Ensure self.p4
                    self.verifyP4()
                    self.p4.filename = er.path
                    self.p4.p4Sync()
                else:
                    self.logger.warning('Perforce flag is set to off')
            er.load()

    @staticmethod
    def getNestedRefs(ref=''):
        """ Method to get the nested references """
        searchRefs = []
        if not ref:
            topRefs = getReferences()
            if topRefs:
                for refNode, ref in topRefs.iteritems():  # @UnusedVariable
                    searchRefs.append(ref)
        else:
            searchRefs.append(ref)
        subRefs = []
        if searchRefs:
            #			for refNode, ref in topRefs.iteritems():
            for r in searchRefs:
                sub = getReferences(parentReference=r)
                for rn, rf in sub.iteritems():  # @UnusedVariable
                    if sub:
                        subRefs.append(rf)
            return subRefs

    @property
    def sceneHasNestedRefs(self):
        """ Method to check if scene has nested references """
        if self.getNestedRefs():
            return 1
        else:
            return 0

    def nodeIsNested(self, node):
        """ True or false if the object passed is referenced """
        node = self.convertToPyNode(node)
        if node.isReferenced():
            fRefObj = FileReference(referenceQuery(node, referenceNode=1), namespace=node.parentNamespace())
            for n in self.getNestedRefs():
                if n.refNode == fRefObj.refNode:
                    return 1
                    break
            return 0
        else:
            return 0

    def getTopLevelRef(self, node):
        """ Return the top level reference for the passed node """

        node = self.convertToPyNode(node)
        if node.isReferenced():
            fRefObj = FileReference(referenceQuery(node, referenceNode=1), namespace=node.parentNamespace())
            if self.nodeIsNested(node):
                topRefs = getReferences()
                for nSpace, rPath in topRefs.iteritems():
                    fRef = FileReference(referenceQuery(rPath, referenceNode=1), namespace=nSpace)
                    if fRefObj.refNode in fRef.nodes():
                        for g in fRef.nodes():
                            if fRefObj.refNode == g and objExists(g):
                                self.logger.debug('Node reference nested, returning - %s' % fRef.path)
                                return fRef
            else:
                self.logger.debug('Node reference not nested, returning - %s' % fRefObj.path)
                return fRefObj
        else:
            self.logger.debug('Node not referenced, not returning anything')

    def getRefs(self, includeNested=1, node=''):
        """
        SYNOPSIS
         Method to get scene references

        INPUTS
         (bool)	includeNested:		also include nested references
         (str)*	node:				Pass a node and only act on the reference, the node belongs to. If the reference passed is nested, includeNested will be forced.

        RETURNS:
         (list) file references in scene or attached to node
        """

        allRefs = []

        #Get all the top level references
        if node:
            node = self.convertToPyNode(node)
            topLevel = self.getTopLevelRef(node)
            if topLevel:
                allRefs.append(topLevel)
            else:
                self.logger.warning('Node - %s - was passed and no reference found' % node)

            if self.nodeIsNested(node):
                nested = self.getNestedRefs(topLevel)
                if nested:
                    self.logger.info('Node was passed and reference was nested - all subrefs will be included')
                    for n in nested:
                        allRefs.append(n)

        else:
            topRefs = getReferences()
            for rn, ref in topRefs.iteritems():  # @UnusedVariable
                allRefs.append(ref)
                # Look for nested references
                if includeNested:
                    nested = self.getNestedRefs(ref)
                    if nested:
                        for n in nested:
                            allRefs.append(n)
        return allRefs

    def importReferences(self, includeNested=1, removeNamespaces=1, returnNodes=0, node=''):
        """
        SYNOPSIS
         Imports all references for the current scene

        INPUTS
         (bool)	includeNested:		also include nested references
         (bool)	removeNamespaces:	remove no namespaces (0), remove all namespaces (1) & strip namespaces to 1 level (2)
         (bool)	returnNodes:		pass back all nodes imported
         (str)*	node:				Pass a node and only act on the reference, the node belongs to. If the reference passed is nested, includeNested will be forced.

        RETURNS:
         (list) imported nodes (If returnNodes is passed (1))
        """

        #Get all the top level references
        rNodes = []
        cleanNS = []
        initError = 0

        # Prep checks
        if removeNamespaces:
            if removeNamespaces == 2 and not includeNested:
                self.logger.error(
                    'If you want to strip down to 1 namespace level (removeNamespaces=2) , you must pass includeNested as 1')
                initError = 1

        if not initError:
            allRefs = self.getRefs(includeNested=includeNested, node=node)
            for each in allRefs:
                ns = each.namespace
                subRefs = self.getNestedRefs(each)
                if subRefs:
                    for cns in subRefs:
                        cleanNS.append([cns.namespace, ns])
                nodes = each.nodes()
                each.importContents()

                # Remove all namespaces
                if removeNamespaces:
                    if removeNamespaces == 1:
                        namespace(mv=(ns, ':'), f=1)  #@UndefinedVariable
                        Namespace(ns).remove()
                # Store all nodes that was a part of the referenced file
                if returnNodes:
                    rNodes.extend(nodes)

            # Strip to 1 9 level
            if removeNamespaces:
                if removeNamespaces == 2:
                    for c in cleanNS:
                        Namespace.create(c[0])
                        self.logger.info('Moving name space - %s:%s - to - %s' % (c[1], c[0], c[0]))
                        namespace(mv=('%s:%s' % (c[1], c[0]), c[0]), f=1)  #@UndefinedVariable
                    for delC in cleanNS:
                        Namespace('%s:%s' % (delC[1], delC[0])).remove()
                    for unused in cleanNS:
                        if ':%s' % delC[1] in listNamespaces():
                            Namespace(':%s' % delC[1]).remove()

        removed = ''
        if removeNamespaces:
            removed = ', namespaces removed'
        self.logger.info('References imported%s' % removed)

        if returnNodes:
            existingRNodes = []
            for r in rNodes:
                if objExists(r):
                    existingRNodes.append(r)
            if existingRNodes:
                return existingRNodes


class MayaNamespaceCore(Maya):
    ##################################################################################################################################
    ##	Namespace methods																												##
    ##################################################################################################################################

    def __init__(self):
        """ MayaNamespaceCore.__init__():  set initial parameters """
        super(MayaNamespaceCore, self).__init__()

    @staticmethod
    def nameSpaces(case):
        """ Name space manipulation """
        sceneNameSpaces = listNamespaces(recursive=False, internal=False)
        if case == 'clean':
            for ga in sceneNameSpaces:
                namespace(set=ga)  #@UndefinedVariable
                if not namespaceInfo(listOnlyDependencyNodes=True):
                    ga.remove()
            namespace(set=':')  #@UndefinedVariable

    @staticmethod
    def giveNameSpace(node):
        """ Return full namespace """
        return (':'.join(node.split(':')[:-1])) + ':'

    @staticmethod
    def nameRoot(node):
        """
        SYNOPSIS
         Gets the name root of the input name string.  Removes all
         colon separated namespaces and pipe separated long names.

        INPUTS
         (string) node:  The node to get the name root of.

        RETURNS: (string)  The name root of the input node.
        """

        result = node.replace(mel.eval('match( ".*|", "%s" )' % node), "")
        sn = result.replace(mel.eval('match( ".*:", "%s" )' % result), "")
        return sn

    @staticmethod
    def removeNameSpace(ns, nuke=0):

        # parse ns
        parentNS, childNS = ns.split(':')

        # create new children NS
        if childNS not in namespaceInfo(lon=1):
            Namespace.create(childNS)

        namespace(set=':')  #@UndefinedVariable
        if nuke:
            childNS = ':'
        namespace(mv=(ns, childNS), f=1)  #@UndefinedVariable

        # delete it
        Namespace(ns).remove()

        try:
            # try to remove parent if it is not part of another child namespace
            nss = listNamespaces(recursive=True, internal=False)
            if not [ns for ns in nss if re.search('%s:' % parentNS, ns)]:
                Namespace(parentNS).clean()
                Namespace(parentNS).remove()
        except:
            pass  # still stuff in it

    def removePrefix(self, node):
        """
        SYNOPSIS
         Removes the underscore separated prefix from the input string.

        INPUTS
         (string) node:  The node name to remove prefix from.

        RETURNS: (string)  The input string minus the first underscore prefix.
        """

        nRoot = self.nameRoot(node)
        if not re.search('_', nRoot):
            return nRoot
        else:
            return nRoot[nRoot.find('_') + 1:]

    @staticmethod
    def stripNameSpace(node):
        """ Strip and return name space """

        return node.split(':')[-1]


class MayaVisibilityCore(Maya):
    ##################################################################################################################
    ##	Visibility methods																							##
    ##################################################################################################################

    def __init__(self):
        """ MayaVisibilityCore.__init__():  set initial parameters """
        super(MayaVisibilityCore, self).__init__()


    def jpHideAndLock(self, nodes, keyT=1, keyR=1, keyS=1, keyV=1, LockT=1, LockR=1, LockS=1, LockV=1, all=2, keyAll=2,
                      lockAll=2):  #@ReservedAssignment
        """
        SYNOPSIS
         Locks and hides attributes

             1 = Hide or Lock
             0 = Show or Unlock

             Default for all is ON (Hide and Lock)

             example:
             jpHideAndLock('root',1,0,0,0,1,0,0,0)
             Hides and Locks translate only
             jpHideAndLock('root',keyR=0)
             Hides and Locks all except rotation is still keyable




        INPUTS	*=optional
         (string) nodes:	The node(s) to work on
         (bool)* keyT: 1 = Hide translate x,y,z
         (bool)* keyR: 1 = Hide rotate x,y,z
         (bool)* keyS: 1 = Hide scale x,y,z
         (bool)* keyV: 1 = Hide visibility
         (bool)* LockT: 1 = Lock translate x,y,z
         (bool)* LockR: 1 = Lock rotate x,y,z
         (bool)* LockS: 1 = Lock scale x,y,z
         (bool)* LockV: 1 = Lock visibility
         (int)* all: 0 = show and unlock all attrs
                      1 = hide and lock all attrs
         (int)* keyAll: 0 = show all attrs
                         1 = hide all attrs
         (int)* lockAll: 0 = unlock all attrs
                          1 = lock all attrs

        RETURNS: nothing
        """
        if str(nodes.__class__) == "<type 'list'>":
            for node_ in nodes:
                self.jpHideAndLock(node_, keyT, keyR, keyS, keyV, LockT, LockR, LockS, LockV, all, keyAll, lockAll)
            return
        else:
            node = nodes
        if not objExists(node):
            self.logger.warning("jpHideAndLock: %s doesn't exist" % node)
            return

        if all == 1:
            keyT, keyR, keyS, keyV, LockT, LockR, LockS, LockV = [1, 1, 1, 1, 1, 1, 1, 1]
        elif all == 0:
            keyT, keyR, keyS, keyV, LockT, LockR, LockS, LockV = [0, 0, 0, 0, 0, 0, 0, 0]
        if keyAll == 1:
            keyT, keyR, keyS, keyV = [1, 1, 1, 1]
        if keyAll == 0:
            keyT, keyR, keyS, keyV = [0, 0, 0, 0]
        if lockAll == 1:
            LockT, LockR, LockS, LockV = [1, 1, 1, 1]
        if lockAll == 0:
            LockT, LockR, LockS, LockV = [0, 0, 0, 0]
        node = self.convertToPyNode(node)
        node.tx.setKeyable(keyT - 1)
        node.ty.setKeyable(keyT - 1)
        node.tz.setKeyable(keyT - 1)
        node.rx.setKeyable(keyR - 1)
        node.ry.setKeyable(keyR - 1)
        node.rz.setKeyable(keyR - 1)
        node.sx.setKeyable(keyS - 1)
        node.sy.setKeyable(keyS - 1)
        node.sz.setKeyable(keyS - 1)
        node.v.setKeyable(keyV - 1)

        node.tx.setLocked(LockT)
        node.ty.setLocked(LockT)
        node.tz.setLocked(LockT)
        node.rx.setLocked(LockR)
        node.ry.setLocked(LockR)
        node.rz.setLocked(LockR)
        node.sx.setLocked(LockS)
        node.sy.setLocked(LockS)
        node.sz.setLocked(LockS)
        node.v.setLocked(LockV)

        if objExists('%s.radius' % node):
            node.radius.lock()
            node.radius.setKeyable(0)  # <-- Need to do both
            node.radius.showInChannelBox(0)  # <-- Need to do both

        #disable all upper and lower rotation limits
        transformLimits(node, erx=(0, 0))
        transformLimits(node, ery=(0, 0))
        transformLimits(node, erz=(0, 0))

    def jpHideAndLockPCons(self, nodes):
        """
        SYNOPSIS
         Locks and hides common attributes on a parentConstraint

        INPUTS
         (string) nodes:	The node(s) to work on

        RETURNS: nothing
        """
        if nodes.__class__ == list:
            for node_ in nodes:
                self.jpHideAndLockPCons(node_)
            return
        else:
            node = nodes

        node.nds.set(lock=True, keyable=False)
        node.int.set(lock=True, keyable=False)
        node.w0.set(lock=True, keyable=False)

    @staticmethod
    def jpHideAndLockDetailed(node, keyTX=1, keyTY=1, keyTZ=1, keyRX=1, keyRY=1, keyRZ=1, keySX=1, keySY=1,
                              keySZ=1, keyV=1, LockTX=1, LockTY=1, LockTZ=1, LockRX=1, LockRY=1, LockRZ=1, LockSX=1,
                              LockSY=1, LockSZ=1, LockV=0):
        """
        SYNOPSIS
         Locks and hides attributes

             1 = Hide or Lock
             0 = Show or Unlock

             example:
             jpHideAndLockDetailed('root',1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0)
             Hides and Locks translate x,z only


        INPUTS	*=optional
         (string) node:	The node to work on
         (bool)* keyTX: 1 = Hide translate x
         (bool)* keyTY 1 = Hide translate y
         (bool)* keyTZ: 1 = Hide translate z
         (bool)* keyRX: 1 = Hide rotate x
         (bool)* keyRY: 1 = Hide rotate y
         (bool)* keyRZ: 1 = Hide rotate z
         (bool)* keySX: 1 = Hide scale x
         (bool)* keySY: 1 = Hide scale y
         (bool)* keySZ: 1 = Hide scale z
         (bool)* keyV: 1 = Hide visibility
         (bool)* LockTX: 1 = Lock translate x
         (bool)* LockTY: 1 = Lock translate y
         (bool)* LockTZ: 1 = Lock translate z
         (bool)* LockRX: 1 = Lock rotate x
         (bool)* LockRY: 1 = Lock rotate y
         (bool)* LockRZ: 1 = Lock rotate z
         (bool)* LockSX: 1 = Lock scale x
         (bool)* LockSY: 1 = Lock scale y
         (bool)* LockSZ: 1 = Lock scale z
         (bool)* LockV: 1 = Lock visibility

        RETURNS: nothing
        """

        node = PyNode(node)
        node.tx.setKeyable(keyTX - 1)
        node.ty.setKeyable(keyTY - 1)
        node.tz.setKeyable(keyTZ - 1)
        node.rx.setKeyable(keyRX - 1)
        node.ry.setKeyable(keyRY - 1)
        node.rz.setKeyable(keyRZ - 1)
        node.sx.setKeyable(keySX - 1)
        node.sy.setKeyable(keySY - 1)
        node.sz.setKeyable(keySZ - 1)
        node.v.setKeyable(keyV - 1)
        node.tx.setLocked(LockTX)
        node.ty.setLocked(LockTY)
        node.tz.setLocked(LockTZ)
        node.rx.setLocked(LockRX)
        node.ry.setLocked(LockRY)
        node.rz.setLocked(LockRZ)
        node.sx.setLocked(LockSX)
        node.sy.setLocked(LockSY)
        node.sz.setLocked(LockSZ)
        node.v.setLocked(LockV)

        #if node.radius.exists():	# <- deprecated
        if objExists('%s.radius' % node):
            node.radius.lock()
            node.radius.setKeyable(0)  # <-- Need to do both
            node.radius.showInChannelBox(0)  # <-- Need to do both

        #disable all upper and lower rotation limits
        transformLimits(node, erx=(0, 0))
        transformLimits(node, ery=(0, 0))
        transformLimits(node, erz=(0, 0))

    @staticmethod
    def jpHideAndLockIK(node, keyPX=1, keyPY=1, keyPZ=1, keyO=1, keyR=1, keyT=1, keyB=1, lockPX=1, lockPY=1,
                        lockPZ=1, lockO=1, lockR=1, lockT=1, lockB=1, all=2):  #@ReservedAssignment
        """
        SYNOPSIS
         Locks and hides attributes

             1 = Hide or Lock
             0 = Show or Unlock

             Default for all is ON (Hide and Lock)

             example:
             jpHideAndLockIK('ikHandle',keyT=1,all=0)
             Hides and Locks twist only
             jpHideAndLock('ikHandle',keyR=0)
             Hides and Locks all except roll is still keyable


        INPUTS	*=optional
         (string) node:	The node to work on
         (bool)* keyPX: 1 = Hide poleVectorX
         (bool)* keyPY: 1 = Hide poleVectorY
         (bool)* keyPZ: 1 = Hide poleVectorZ
         (bool)* keyO: 1 = Hide offset
         (bool)* keyR: 1 = Hide roll
         (bool)* keyT: 1 = Hide twist
         (bool)* keyB: 1 = Hide ikBlend
         (bool)* keyPX: 1 = Hide poleVectorX
         (bool)* keyPY: 1 = Hide poleVectorY
         (bool)* keyPZ: 1 = Hide poleVectorZ
         (bool)* keyO: 1 = Hide offset
         (bool)* keyR: 1 = Hide roll
         (bool)* keyT: 1 = Hide twist
         (bool)* keyB: 1 = Hide ikBlend
         (int)* all: 0 = show and unlock all attrs
                      1 = hide and lock all attrs

        RETURNS: nothing
        """
        if all == 1:
            keyPX, keyPY, keyPZ, keyO, keyR, keyT, keyB, lockPX, lockPY, lockPZ, lockO, lockR, lockT, lockB = [1, 1, 1,
                                                                                                               1, 1, 1,
                                                                                                               1, 1, 1,
                                                                                                               1, 1, 1,
                                                                                                               1, 1]
        elif all == 0:
            keyPX, keyPY, keyPZ, keyO, keyR, keyT, keyB, lockPX, lockPY, lockPZ, lockO, lockR, lockT, lockB = [0, 0, 0,
                                                                                                               0, 0, 0,
                                                                                                               0, 0, 0,
                                                                                                               0, 0, 0,
                                                                                                               0, 0]
        node = PyNode(node)
        node.poleVectorX.setKeyable(keyPX - 1)
        node.poleVectorY.setKeyable(keyPY - 1)
        node.poleVectorZ.setKeyable(keyPZ - 1)
        node.offset.setKeyable(keyO - 1)
        node.roll.setKeyable(keyR - 1)
        node.twist.setKeyable(keyT - 1)
        node.ikBlend.setKeyable(keyB - 1)
        node.poleVectorX.setLocked(lockPX)
        node.poleVectorY.setLocked(lockPY)
        node.poleVectorZ.setLocked(lockPZ)
        node.offset.setLocked(lockO)
        node.roll.setLocked(lockR)
        node.twist.setLocked(lockT)
        node.ikBlend.setLocked(lockB)

    def lockAndHideAttributes(self, node, attrs):
        """
        SYNOPSIS
         Locks all and hides the input attributes on the specified node.

        INPUTS
         (string) node:  The node to lock keyable attributes on.
         (list)	attrs:	Attributes to lock

        RETURNS: Nothing.
        """
        node = self.convertToPyNode(node)
        for attr in attrs:
            setAttr((node.name() + "." + attr), k=False, l=True)

    def lockVisibleAttrs(self, node):
        """
        SYNOPSIS
         Locks all keyable attributes on the input node.

        INPUTS
         (string) node:  The node to lock keyable attributes on.

        RETURNS: Nothing.
        """

        if not len(ls(node)):
            self.logger.error("lockVisibleAttrs: input node does not exist '%s'.\n" % node)
        node = self.convertToPyNode(node)

        keyableAttrs = node.listAttr(k=1)
        if keyableAttrs:
            for kAttr in keyableAttrs:
                try:
                    kAttr.lock()
                except:
                    pass

    def unlockVisibleAttrs(self, node):
        """
        SYNOPSIS
         Locks all keyable attributes on the input node.

        INPUTS
         (string) node:  The node to lock keyable attributes on.

        RETURNS: Nothing.
        """
        node = self.convertToPyNode(node)

        keyableAttrs = node.listAttr(k=1)
        if keyableAttrs:
            for kAttr in keyableAttrs:
                try:
                    kAttr.unlock()
                except:
                    pass


class MayaMeshCore(Maya):
    ##################################################################################################################################
    ##	Mesh methods																												##
    ##################################################################################################################################

    def __init__(self):
        """ MayaMeshCore.__init__():  set initial parameters """
        super(MayaMeshCore, self).__init__()


    def checkHier4Mesh(self, metaRoot):
        """
        NAME: checkHier4Mesh

        SYNOPSIS
         Check main hierarchy to see if any joint has a 'mesh' (poly)
         shape node parented to it. This will break the granny exporter

        INPUTS
         (string) 	metaRoot:	metaRoot PyNode

        RETURNS: (list) [result, [offending]]
        """

        offending = []
        result = [0, 0]

        if objExists(metaRoot):
            metaRoot = self.convertToPyNode(metaRoot)
            rootJoint = self.listcP(metaRoot.rootJoint)
            if rootJoint:
                for child in rootJoint.getChildren(ad=1):
                    try:
                        if objectType(child) == 'mesh':
                            if child.getParent().attr('type').get() == 5:  #ball joints
                                offending.append(child)
                    except:
                        pass  # pymel erros on checking objectType of effectors?

        if offending:
            result = [1, offending]
            select(offending, r=1)

        return result

    def checkUnmergedVerts(self, meshes=[], precision=4, merge=0):
        """
        SYNOPSIS: Check verts sharing space with other verts
        INPUTS: meshes* - meshes to check (if none passed, do all in scene)
                precision* - decimal precision when comparing verts (default 4)
                merge* - optionally merge instead of pass back
        RETURNS: none
        """
        if not meshes:
            meshes = self.gimmeMeshes()
        allSharedVerts = []

        for meshCheck in meshes:
            sharedVerts = []
            boundaryVerts = []
            vts = meshCheck.getShape().verts
            for v in vts:
                if v.isOnBoundary():
                    boundaryVerts.append(v)
            if boundaryVerts:
                for bv in boundaryVerts:
                    for bCompare in boundaryVerts:
                        if not bCompare == bv:
                            if round(bv.getPosition()[0], precision) == round(bCompare.getPosition()[0],
                                                                              precision) and round(bv.getPosition()[1],
                                                                                                   precision) == round(
                                    bCompare.getPosition()[1], precision) and round(bv.getPosition()[2],
                                                                                    precision) == round(
                                    bCompare.getPosition()[2], precision):
                                sharedVerts.append(bv)
                                sharedVerts.append(bCompare)
                                allSharedVerts.append(bv)
                                allSharedVerts.append(bCompare)

            if sharedVerts:
                if merge:
                    polyMergeVertex(sharedVerts, d=float(1 / (10 ** float(precision))))  #@UndefinedVariable

        if not merge:
            if allSharedVerts:
                select(sharedVerts)

    def cleanNetworkNodes(self, all=0, withinProtectedName=1):  #@ReservedAssignment
        """
        SYNOPSIS: Cleans out network nodes
        INPUTS*: all = 	True - Take care of duplicates of our implemented sceneBrain and asset hubs
                                False - Remove all network nodes
                withinProtected - Search only within protected names
        RETURNS: None
        """
        nNodes = ls(type='network')
        protectedNames = ['sceneBrain', 'assetHub', 'shaderContainer', 'collisionContainer', 'meshContainer',
                          'groupContainer', 'lodContainer']
        if nNodes:
            for nNode in nNodes:
                if not nNode.isReferenced():
                    if withinProtectedName:
                        for p in protectedNames:
                            if search(p, nNode.name()):
                                if not nNode.name() == p:
                                    self.disconnectAttrs(nNode)
                                    delete(nNode)
                    else:
                        if not all:
                            if not nNode.name() in protectedNames:
                                self.disconnectAttrs(nNode)
                                delete(nNode)
                        else:
                            self.disconnectAttrs(nNode)
                            delete(nNode)

    def disconnectInputs(self, node):
        """ Disconnect all output attrs for a given node """
        node = self.convertToPyNode(node)
        if not node.isReferenced():
            input = node.inputs(c=1, p=1)  #@ReservedAssignment
            for i in input:
                disconnectAttr(i[1], i[0])

    def disconnectOutputs(self, node):
        """ Disconnect all output attrs for a given node """
        node = self.convertToPyNode(node)
        if not node.isReferenced():
            output = node.outputs(c=1, p=1)
            for o in output:
                disconnectAttr(o[0], o[1])

    def disconnectAttrs(self, node):
        """ Disconnect all attrs for a given node """
        node = self.convertToPyNode(node)
        if not node.isReferenced():
            input = node.inputs(c=1, p=1)  #@ReservedAssignment
            output = node.outputs(c=1, p=1)

            for i in input:
                disconnectAttr(i[1], i[0])

            for o in output:
                disconnectAttr(o[0], o[1])

    def cleanMeshes(self, meshes=[]):
        """
        SYNOPSIS: Cleans out duplicate shape nodes
        INPUTS*: meshes = list of specific meshes to clean
        RETURNS: None

        NOTE: Do not run this command on deformed objects (other than skin cluster type)
        TODO: Find a way to query if a mesh is being deformed period....
        """
        if not meshes:
            meshes = self.gimmeMeshes()
        if meshes:
            for m in meshes:
                if not m.isReferenced():
                    shapes = m.getShapes()
                    for s in shapes:
                        if s.intermediateObject.get():
                            if not s.outputs():
                                delete(s)
                    rename(m.getShape(), '%sShape' % m.name())

    @staticmethod
    def getDisplayLayer(node):
        """
        SYNOPSIS: Queries and returns displayLayer from node
        INPUTS: node - node to query
        RETURNS: displayLayer
        """
        if node.listConnections(type='displayLayer'):
            return node.listConnections(type='displayLayer')[0]

    def getNodeFromSchema(self, varName, listName=None):
        if listName:
            result = parser_schema.ParseSchema().getWellFormed(varName, listName)
        else:
            result = parser_schema.ParseSchema().getWellFormed(varName)
        if result.__class__ is float:
            return result
        else:
            if result:
                if objExists(result):
                    self.check4Dup(result, 1)
                    return self.convertToPyNode(result)
                else:
                    self.logger.debug("%s doesn't exist in the scene" % result)
                    return result
            else:
                self.logger.error("Failed to getWellFormed data '%s' from Schema" % varName)

    @staticmethod
    def gimmeMeshes():
        """
        SYNOPSIS: Returns nodes from current scene
        INPUTS: none
        RETURNS: all meshes
        """
        allMeshes = []
        for t in (ls(type='transform')):
            if t.getShape():
                #				if nodeType(t.getShape()) == 'mesh':
                if isinstance(t.getShape(), nt.Mesh):
                    allMeshes.append(t)
        if allMeshes:
            return allMeshes

    def meshesInGroup(self, grp):
        """ Return all meshes in this group and all of it's sub groups """
        gMeshes = []
        grp = self.convertToPyNode(grp)
        if self.isGroup(grp):
            for m in grp.listRelatives(ad=1, typ='transform'):
                if not self.isGroup(m):
                    gMeshes.append(m)
        if gMeshes:
            return gMeshes

    def polyMergePlus(self):
        """
        SYNOPSIS: Merge utility - Preserves pivot, name, and layer from first in selection
        INPUTS: none
        RETURNS: none
        """
        if selected():
            if len(selected()) > 1:
                if self.verifyMeshSelection(1):
                    oSelection = selected()
                    nName = selected()[0].name()
                    nPiv = xform(selected()[0].name(), q=1, a=1, ws=1, rp=1)
                    dLayer = self.getDisplayLayer(selected()[0])
                    nParent = ''
                    if selected()[0].getParent():
                        nParent = selected()[0].getParent()
                    select(oSelection, r=1)
                    cResult = PyNode(polyUnite(ch=0)[0])  #@UndefinedVariable
                    cResult.rename(nName)
                    # Re-set pivot of new object
                    cResult.setPivots(nPiv)
                    select(cResult, r=1)
                    if dLayer:
                        editDisplayLayerMembers(dLayer.name(), cResult.name())
                    if nParent:
                        cResult.setParent(nParent)

    @staticmethod
    def swapShapeNode(shapeTransform, node):
        """
        SYNOPSIS
         Parents the input shape node to the second input node.
         The original shape node transform is deleted.
         Preserves incoming visibility connections to shapeNode.

        INPUTS
         (string) shapeTransform:  The transform of the shape node to use.
         (string) node:  The node to parent the shape node to.

        RETURNS: new shapeNode.
        """

        shapeTransform = PyNode(shapeTransform)

        # check for current incoming visibility connections
        shapeVisSource = ''
        if node.getShape():
            shapeVisSource = listConnections(node.getShape().visibility, p=1)

        makeIdentity(shapeTransform, apply=True, s=1, r=0, t=0, n=0)
        shapes = listRelatives(shapeTransform, pa=1, s=1)

        # get shape that is 'real' shape, i.e.- non-intermediate object
        shape = ''
        for testShape in map(lambda x: PyNode(x), shapes):
            if not testShape.intermediateObject.get():
                shape = testShape

        # parent right one
        shape = PyNode(parent(shape, node, add=1, s=1)[0])

        # rename shape node proper
        shape = rename(shape, '%sShape' % shape[:shape.find('|')])

        # connect visibility if old shape was connected
        if shapeVisSource:
            shape.v.unlock()
            shapeVisSource[0].connect(shape.v)
            shape.v.lock()

        delete(shapeTransform)
        reorder(shape, f=1)

        return shape

    def turnOffDoubleSided(self):
        """ Utility method to turn off all double sided flags """

        oTurnOff = []
        if selected():
            if self.verifyMeshSelection(1):
                for each in selected():
                    oTurnOff.append(each)
        # If nothing is selected, get meshes from whole scene
        else:
            oTurnOff = self.gimmeMeshes()

        if oTurnOff:
            for offObj in oTurnOff:
                offObj.getShape().doubleSided.set(0)
                offObj.getShape().opposite.set(0)

    @staticmethod
    def verifyMeshSelection(all=0):  # @ReservedAssignment
        """
        SYNOPSIS: Verifies the selection to be mesh transform
        INPUTS: all = 0 - acts only on the first selected item
                all = 1 - acts on all selected items
        RETURNS: 0 if not mesh transform or nothing is selected
                 1 if all/first selected is mesh transform
        """
        if not selected():
            return 0
        allSelected = []
        error = 0
        if all:
            allSelected = selected()
        else:
            allSelected.append(selected()[0])

        if allSelected:
            for each in allSelected:
                if nodeType(each) == 'transform' and nodeType(each.getShape()) == 'mesh':
                    pass
                else:
                    error = 1
        else:
            error = 1

        if error:
            return 0
        else:
            return 1


class MayaCore(MayaSceneCore, MayaNodeCore, MayaMiscCore, MayaPrintCore, MayaNamespaceCore, MayaReferenceCore,
               MayaVisibilityCore, MayaMeshCore):
    """
    Super/sub class and foundational Maya utility library
    """

    def __init__(self):
        """ MayaCore.__init__():  set initial parameters """
        super(MayaCore, self).__init__()


mCore = MayaCore()

print "maya.core.mayaCore imported"