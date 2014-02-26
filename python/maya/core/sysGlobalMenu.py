"""
Author: Jason.Parks
Created: May 15, 2012
Module: maya.core.sysGlobalMenu
Purpose: Art Menu global class
"""

#from functools import partial
from pymel.all import *  # @UnusedWildImport
from pymel.util import *  # @UnusedWildImport
from re import search  # @Reimport
from shutil import copyfile
import datetime
import fnmatch
import getpass  # @UnusedImport @Reimport
import os  # @UnusedImport @Reimport
import sys  # @UnusedImport @Reimport
import xml.etree.ElementTree as ET

# ---- !!!!!!!! IMPORTANT !!!!!!!!! --------
# Do NOT import ANYTHING that is under PCS GLOBAL CODE REPOSITORY here, DO your IMPORTS on the BOTTOM 


class MayaMenu(object):
    """
    SYNOPSIS
     Super class of Maya Tool Delivery Menu.
     Methods to manage the delivery system.
    """

    def __init__(self):
        """ MayaMenu.__init__():  set initial parameters """
        super(MayaMenu, self).__init__()

        # Set who is running
        self.userName = getpass.getuser()
        self.PCStoolsLocation = gv.toolsLocation
        self.PCSlogLocation = gv.logLocation

        # Parse the backbone XML
        self.pcsXML = ET.parse('%s/schemas/pcsSchema.xml' % gv.toolsLocation)
        self.pcsXMLcore = self.pcsXML.getiterator('Core')[0]
        self.log = None
        self.PCSMenu = None
        self.menuDict = {}

        # Expose Global Variables
        self.PCSDevelopers = eval(self.pcsXMLcore.get('devs'))
        self.PCStoolName = self.pcsXMLcore.get('PCStoolName')
        self.PCStPad = 'mtPCSG'  # runtime command prefix?

        # Set Run Time Variables
        self.PCSmenuPath = '%s/maya' % self.PCStoolsLocation
        self.PCSmenuStart = '%s/menu' % self.PCSmenuPath
        self.runTimeAnnotation = '%s Maya Tools' % self.PCStoolName
        self.menuName = 'mt_%s' % self.PCStoolName.replace(' ', '_')
        self.PCSmVersion = None

    # Any additions
    #		#-- P4 Active
    #		if not self.userXMLCore.get('P4Active'):
    #			if not self.PCSactiveTeam == 'teamB':
    #				if self.PCSP4userName and self.PCSP4server and self.PCSP4workspace:
    #					self.userXMLCore.set('P4Active', '1')
    #				else:
    #					self.userXMLCore.set('P4Active', '0')
    #			else:
    #				self.userXMLCore.set('P4Active', '0')
    #			self.userXML.write('%s/data/%s/PCS.xml' % (self.PCSlogLocation, self.userName))
    #
    #		self.p4Active = eval(self.userXMLCore.get('P4Active'))

    def setGlobalVars(self):
        """ Set Needed Global Vars """
        if search('x64', about(version=1)):
            self.PCSmVersion = float(about(version=1).split(' ')[0])
        else:
            self.PCSmVersion = float(about(version=1))
        melGlobals.initVar('float', 'PCSmVersion')
        melGlobals['PCSmVersion'] = self.PCSmVersion
        melGlobals.initVar('string', 'PCSmenuPath')
        melGlobals['PCSmenuPath'] = '%s/' % self.PCSmenuPath

        # Temp for prefs
        melGlobals.initVar('string', 'PCStoolName')
        melGlobals['PCStoolName'] = self.PCStoolName
        melGlobals.initVar('string', 'PCSos')
        melGlobals['PCSos'] = about(os=True)

    def setLogger(self, logInit=0):
        # Logger Object
        self.log = logger
        self.log.setLevel(10)

        if logInit:
            self.log.debug('PCStoolsLocation is - %s' % self.PCStoolsLocation)
            self.log.debug('PCSDevelopers are - %s' % self.PCSDevelopers)
            self.log.debug('PCStoolName is - %s' % self.PCStoolName)
            self.log.debug('PCSmenuPath is - %s' % self.PCSmenuPath)

            # report run from location
            fileLocation = os.path.dirname(inspect.getsourcefile(tempFunc))
            self.log.debug("Ran sysGlobalMenu.py from '%s'" % fileLocation)

    def injectPaths(self):
        """ Inject paths needed """
        # already done in mayaMenuBoot.py
        sys.path.append('%s/python/maya/site-packages' % self.PCStoolsLocation)
        #sys.path.append('%s/python/maya/site-packages/pymel-1.0.5' % self.PCStoolsLocation) # add to Maya.env to get it
        # in early enough

        mVer = about(version=1)
        if search('x64', mVer):
            mVer = mVer.split(' ')[0]
            putEnv("MAYA_PLUG_IN_PATH", [getEnv('MAYA_PLUG_IN_PATH'), '%s/plugins/%s/win64' % (self.PCSmenuPath, mVer),
                                         '%s/plugins/%s/win64/others' % (self.PCSmenuPath, mVer)])
            # sys.path.append('%s/python/common/pyQt/PyQt4/2012/win64' % self.PCStoolsLocation)
        else:
            putEnv("MAYA_PLUG_IN_PATH", [getEnv('MAYA_PLUG_IN_PATH'), '%s/plugins/%s/win32' % (self.PCSmenuPath, mVer),
                                         '%s/plugins/%s/win32/others' % (self.PCSmenuPath, mVer)])
            # sys.path.append('%s/python/common/pyQt/PyQt4/2012/win32' % self.PCStoolsLocation)
        # # Add extraScripts/include folder
        # putEnv("MAYA_SCRIPT_PATH",
        #        [getEnv('MAYA_SCRIPT_PATH'), '%s/extraScripts/include/%s' % (self.PCSmenuPath, mVer)])

    def startUp(self):
        """ Menu Start Up Command """

        # Set the logger
        self.setLogger(1)

        # Spawn Global Variables
        self.setGlobalVars()
        self.log.debug('Global Vars Created')

        # Inject Variables
        # Done Upon instantiation

        # Construct Menu Base
        self.PCSMenu_build()
        self.log.debug('ArtMonkey Global Menu Built')

        # Print Environment
        self.PCSMenu_envPrinter()
        self.log.debug('Environment written to network')

        # Copy Local Environment Files
        self.PCSMenu_localFileCopy()
        self.log.debug('User Setup and Maya env copied to network')

        # Write Metrics File (Basic Info)
        self.PCSMenu_metrics()
        self.log.debug('Metrics written to file')

        # Initialize Logger Menu
        self.PCSMenu_loggerMenuInit()
        self.log.debug('Logger menu initialized')

        # Start up xPrefs
        self.PCSMenu_xPrefsInit()
        self.log.debug('X Prefs initialized')

    @staticmethod
    def PCSMenu_xPrefsInit():
        """ Initialize xPrefs """
        if os.path.exists('%s%s' % (
                internalVar(userScriptDir=True), 'mayaToolsMenuPrefs_xPrefs.mel')):  # @UndefinedVariable
            mel.eval('source "%s%s"' % (
                internalVar(userScriptDir=True), 'mayaToolsMenuPrefs_xPrefs.mel'))  # @UndefinedVariable
            scriptJob(event=('SceneOpened', "mel.mayaToolsMenuPrefs_xPrefs()"))
            scriptJob(event=('NewSceneOpened', "mel.mayaToolsMenuPrefs_xPrefs()"))

    @staticmethod
    def PCSMenu_loggerMenuInit():
        """ Add logging menu """
        loggingControl.initMenu()

    def PCSMenu_metrics(self):
        """ Method to replace the mel based metrics """
        # noinspection PyListCreation
        writeArr = []
        writeArr.append('Maya Last Used On: %s' % datetime.datetime.now().strftime("%m/%d/%y : %H:%M:%S"))
        writeArr.append('Running From: %s' % self.PCStoolsLocation)
        writeArr.append('OS Used: %s' % about(osv=True))
        writeArr.append('Maya Version: %s' % about(v=True))

        _file = open('%s/data/%s/%s.PCS' % (self.PCSlogLocation, self.userName, self.userName), "w")
        for l in writeArr:
            l = l.strip()
            _file.write('%s\n' % l)
        _file.close()

    # noinspection PyArgumentList
    def PCSMenu_localFileCopy(self):
        """ Copies userSetup.mel, Maya.env and PCSlobalSetup.mel """

        usrSetupFile = pcsPath.Path('%s%s' % (internalVar(userScriptDir=True), 'userSetup.mel'))  # @UndefinedVariable
        mayaEnvFile = pcsPath.Path(about(environmentFile=True))

        # userSetup.mel
        if usrSetupFile.exists():
            targetPath = '%s/data/%s/%s_networkCopy%s' % (
                self.PCSlogLocation, self.userName, usrSetupFile.namebase, usrSetupFile.ext)
            copyfile(usrSetupFile, targetPath)

        # Maya.env
        if mayaEnvFile.exists():
            targetPath = '%s/data/%s/%s_networkCopy%s' % (
                self.PCSlogLocation, self.userName, mayaEnvFile.namebase, mayaEnvFile.ext)
            copyfile(mayaEnvFile, targetPath)

    def PCSMenu_envPrinter(self):
        """ Print the Maya environment to remote path. """

        _file = open('%s/data/%s/%s.envp' % (self.PCSlogLocation, self.userName, self.userName), "w")
        for l in mayaCore.Maya().getEnv(0):
            _file.write(l)
        _file.close()

    def PCSMenu_cleanRunTimeCommands(self):
        """ Clean out run time commands """

        searchPadding = self.PCStPad
        for e in runTimeCommand(q=1, userCommandArray=1):  # @UndefinedVariable
            if len(e.split('_')) > 1:
                if e.split('_')[0] == searchPadding:
                    runTimeCommand(e, e=1, delete=1)  # @UndefinedVariable

    # noinspection PyUnresolvedReferences
    def PCSMenu_build(self):
        """ Recursive portion """

        #0. Build base
        if not cmds.menuItem(self.menuName, q=1, ex=1):
            self.PCSMenu = Menu(self.menuName, parent=melGlobals['gMainWindow'], allowOptionBoxes=1, tearOff=1,
                                label=self.PCStoolName)
        else:
            self.PCSMenu = Menu(self.menuName)

        with self.PCSMenu:
            with subMenuItem('Options', label="Options", tearOff=1, allowOptionBoxes=1):
                menuItem(label='Refresh Menu', command=self.PCSMenu_refresh)  # @UndefinedVariable
                mel.eval('source "%s/mel/ca_Strings.mel"' % self.PCSmenuPath)
                mel.eval('source "%s/mel/ca_UIFunctions.mel"' % self.PCSmenuPath)  # @UndefinedVariable
                menuItem(divider=1)  # @UndefinedVariable
            with subMenuItem(label="Docs", tearOff=1, allowOptionBoxes=1):
                menuItem(label='Docs01')  # @UndefinedVariable
            menuItem(divider=1)  # @UndefinedVariable

        # 1. Build a construction dictionary with {folder=[files]}
        for root, unused, unused in os.walk(os.path.abspath(self.PCSmenuStart)):
            if not pcsPath.Path(root).makePretty(0, 0) == self.PCSmenuStart:
                mFiles = []
                for fname in os.listdir(root):
                    fullPath = '%s/%s' % (root, fname)
                    # noinspection PyArgumentList
                    if pcsPath.Path(fullPath).isfile() and (
                            fnmatch.fnmatch(fname, '*.mel') or fnmatch.fnmatch(fname, '*.div')):
                        mFiles.append(fname)
                self.menuDict[pcsPath.Path(root).makePretty(0, 0)] = mFiles

        # 2. Sorted Keys list
        sKeys = []
        for dr in self.menuDict.iterkeys():
            sKeys.append(dr)
        sKeys.sort()

        # 3. Build Sorted Menu
        for e in sKeys:
            # Store & Sort The Files
            dictFiles = self.menuDict[e]
            dictFiles.sort()
            # Store the menuName
            cMainName = e.replace(self.PCSmenuStart, self.PCStPad).replace('/', '_').replace('\\', '_')
            # Store the menuLabel
            if len(e.namebase.split('_')) > 1:
                cMainLabel = e.namebase.split('_')[len(e.namebase.split('_')) - 1]
            else:
                cMainLabel = e.namebase
            # Store the parent of the menu
            cMainParent = e.dirname()
            if cMainParent == self.PCSmenuStart:
                cMainParent = self.PCSMenu
            else:
                cMainParent = cMainParent.replace(self.PCSmenuStart, self.PCStPad).replace('/', '_')
            # Intercept Folder Divider
            if re.search('_div', str(e)):
                cmds.menuItem(p=cMainParent, divider=1)
            else:
                #with subMenuItem(cMainName, parent=cMainParent, label=cMainLabel, tearOff=1, allowOptionBoxes=1):
                with subMenuItem(cMainName, label=cMainLabel, tearOff=1, allowOptionBoxes=1):
                    if dictFiles:
                        for dFile in dictFiles:
                            # Intercept File Divider
                            if re.search('.div', dFile):
                                menuItem(divider=1)  # @UndefinedVariable
                            else:
                                # Mel file with no extension (this is a string of the mel file name)
                                fName = dFile.split('.')[0]
                                # Full Path to Mel File
                                sPath = '%s/%s' % (e, fName)
                                rtCommand = "mel.source('%s')\nmel.%s()" % (sPath, fName)
                                # Make Run Time Command Name
                                rtName = '%s_%s' % (self.PCStPad, fName)
                                # If the run time command doesn't exist
                                if not runTimeCommand(rtName, q=1, ex=1):  # @UndefinedVariable
                                    runTimeCommand(rtName, commandLanguage="python", annotation=self.runTimeAnnotation,
                                                   category=self.PCStoolName, command=rtCommand)  # @UndefinedVariable
                                    runTimeCommand(edit=1, category=self.PCStoolName, save=1)  # @UndefinedVariable
                                # If the run time command does exist
                                else:
                                    existingRTCommand = runTimeCommand(rtName, q=1, command=1)  # @UndefinedVariable
                                    if not existingRTCommand == rtCommand:
                                        runTimeCommand(rtName, e=1, command=rtCommand)  # @UndefinedVariable
                                        runTimeCommand(edit=1, category=self.PCStoolName, save=1)  # @UndefinedVariable

                                # Look for matching icon for menu item
                                icon = ''
                                if os.path.exists('%s.bmp' % sPath):
                                    icon = '%s.bmp' % sPath
                                if os.path.exists('%s.png' % sPath):
                                    icon = '%s.png' % sPath
                                if icon:
                                    menuItem(label=fName, command='python("mel.%s()")' % rtName,
                                             image=icon)  # @UndefinedVariable
                                else:
                                    menuItem(label=fName, command='python("mel.%s()")' % rtName)  # @UndefinedVariable
                                # Intercept the engineA exporter
                                if fName == 'objectExporter':
                                    # Source the option box
                                    mel.eval('source "%s/mel/engineA/objectExporterOptions.mel"' % self.PCSmenuPath)
                                    # Connect command with proc
                                    menuItem(optionBox=1,
                                             command='python("mel.objectExporterOptions()")')  # @UndefinedVariable
                                else:
                                    # Look for matching option box item
                                    if os.path.exists('%s.opb' % sPath):
                                        mel.eval('source "%s/mel/ca_Strings.mel"' % self.PCSmenuPath)
                                        mel.eval('source "%s/mel/ca_UIFunctions.mel"' % self.PCSmenuPath)
                                        menuItem(optionBox=1,
                                                 command='python("mel.ca_descriptWin(\'%s.opb\', \'%s\')")' % (
                                                     sPath, fName))  # @UndefinedVariable

                        # Divider between Commands and Folders
                        menuItem(divider=1)  # @UndefinedVariable

    # noinspection PyUnusedLocal
    def PCSMenu_refresh(self, *unused):
        """ Refresh Menu """
        self.log.info('Executing Refresh Menu...')
        self.PCSMenu.deleteAllItems()
        self.PCSMenu.delete()
        # Clean up run time commands
        self.PCSMenu_cleanRunTimeCommands()
        self.PCSMenu_build()
        self.log.info('Menu Refreshed')

    # def PCSActiveTeam_change(self, *args):
    #     """ Edit the active team globally """
    #     self.log.info('Executing Change Active Team')
    #     changeTeam = args[0][0]
    #     itemArray = args[0][1]
    #     value = args[1]
    #     if not changeTeam == self.PCSactiveTeam:
    #         for itm in itemArray:
    #             cVal = 0
    #             if re.search(changeTeam, itm.name()):
    #                 if value:
    #                     cVal = 1
    #                     self.userXMLCore.set('PCSactiveTeam', changeTeam)
    #                     self.PCSactiveTeam = changeTeam
    #                     if self.PCSactiveTeam in self.PCSEngineTeams:
    #                         self.userXMLCore.set('PCSmyEngine', '1')
    #                         self.PCSmyEngine = 1
    #                         melGlobals['PCSmyEngine'] = self.PCSmyEngine
    #                     self.userXML.write('%s/data/%s/PCS.xml' % (self.PCSlogLocation, self.userName))
    #                     self.log.debug('userXML written')
    #                     # Handle overload source and save intercept source
    #                     # See if the teamXML is present
    #                     if os.path.exists('%s/installData/%sTB.XML' % (gv.toolsLocation, changeTeam)):
    #                         self.log.debug('Path exists - %s/installData/%sTB.XML' % (gv.toolsLocation, changeTeam))
    #                         teamXML = ET.parse('%s/installData/%sTB.XML' % (gv.toolsLocation, changeTeam))
    #                         teamXMLCore = teamXML.getiterator('Core')[0]
    #                         lookPath = '%s/extraScripts' % teamXMLCore.get('teamTBRoot')
    #                         self.log.debug('Look path set to - %s' % lookPath)
    #                         #							pPath = parser_PCS.ParsePCS().userGet('PCSprojectToolPath')
    #                         pPath = gv.toolsLocation
    #                         if os.path.exists('%s/teamSave.mel' % lookPath):
    #                             self.log.debug('teamSave found - %s/teamSave.mel' % lookPath)
    #                             mel.eval('source "%s/maya/mel/overload/saveOverload_%s.mel"' % (
    #                                 pPath, about(version=1).split(' ')[0]))
    #                             mel.eval('source "%s/teamSave.mel"' % lookPath)
    #                         else:
    #                             # Source the original autodesk procs
    #                             mel.eval(
    #                                 'source "%s/scripts/others/pv_performAction.mel"' % mel.getenv('MAYA_LOCATION'))
    #                             mel.eval('source "%s/scripts/startup/FileMenu.mel"' % mel.getenv('MAYA_LOCATION'))
    #                         # Team Scene
    #                         if os.path.exists('%s/teamScene.mel' % lookPath):
    #                             mel.eval('source "%s/teamScene.mel"' % lookPath)
    #                         else:
    #                             for sj in scriptJob(listJobs=True):
    #                                 if re.search('teamScene', sj):
    #                                     jNumb = int(sj.split(':')[0])
    #                                     scriptJob(kill=jNumb, force=True)
    #                     else:
    #                         self.log.debug('Team install data not present - %s/installData/%sTB.XML' % (
    #                             gv.toolsLocation, changeTeam))
    #                 else:
    #                     cVal = 0
    #             menuItem(itm, e=1, checkBox=cVal)  #@UndefinedVariable
    #         self.log.info('Active team changed to: %s' % self.PCSactiveTeam)
    #     # Reset the active team to on
    #     else:
    #         for itm in itemArray:
    #             if re.search(changeTeam, itm.name()):
    #                 menuItem(itm, e=1, checkBox=1)  #@UndefinedVariable
    #         self.log.info('Active team is the same: %s' % self.PCSactiveTeam)


def tempFunc():
    pass


if __name__ == 'main':
    print 'Ran Main'
else:
    from common.core import globalVariables as gv
    # need gv first
    MayaMenu().injectPaths()
    from common.fileIO import pcsPath
    from pymel.tools import loggingControl
    from common.diagnostic.pcsLogger import logger
    import mayaCore  # @UnresolvedImport @UnusedImport

    print "maya.core.sysGlobalMenu imported"