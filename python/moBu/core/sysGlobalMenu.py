'''
Author: Jason.Parks
Created: Apr 22, 2012
Module: moBu.sysGlobalMenu
Purpose: start main MoBu menu
'''
	
from pyfbsdk import *
from common.core import globalVariables as gv
from common.diagnostic.pcsLogger import moBuLogger
from common.fileIO.pcsPath import Path
from moBu.core.moBuCore import mbCore
import datetime
import fnmatch
import getpass #@UnusedImport
import imp
import os
import sys

# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UnusedWildImport

_VERSION = 1.00

# Load additions dependent on MoBu version
if mbCore.mobuVer == 2010:
	from pyfbsdk_additions import CreateUniqueTool as FBCreateUniqueTool #@UnresolvedImport @UnusedImport
	from pyfbsdk_additions import HBoxLayout as FBHBoxLayout #@UnusedImport @UnresolvedImport
	from pyfbsdk_additions import TabControl as FBTabControl #@UnusedImport @UnresolvedImport
	from pyfbsdk_additions import GridLayout as FBGridLayout #@UnusedImport @UnresolvedImport
elif mbCore.mobuVer == 2012 or mbCore.mobuVer == 2013:
	from pyfbsdk_additions import FBCreateUniqueTool, FBHBoxLayout, FBTabControl, FBGridLayout #@Reimport @UnresolvedImport @UnusedImport
else:
	moBuLogger.error("Failed to find proper MoBu version: '%s'" % mbCore.mobuVer)

class MoBuToolsMenu(object):
	'''
	Super class of MotionBuilder Tool Delivery Menu. 
	Methods to manage the delivery system.
	'''

	def __init__(self):
		""" MoBuToolsMenu.__init__():  set initial parameters """
		super(MoBuToolsMenu, self).__init__()
		
		# Set who is running for metrics
		self.userName = getpass.getuser()
		
		# run metrics
		self.PCSmoBuMenu_metrics()
		
		self.pcsImagePath = '%s/moBu/icons' % gv.toolsLocation
		
		#TODO: Have buildPipeline generate number into globalVariables
		self.buildNumber = gv.build

	
	def KToolsCallback(self, control, event):
		# import module
		fp, pathname, description = imp.find_module(str(control.Caption))
		menuModule = imp.load_module(str(control.Caption), fp, pathname, description)
		menuModule.run()
		return True
	
	def openToolDocs(self, control, event):
		os.startfile(('%s/docs/tools/index.htm' % gv.toolsLocation).replace('/','\\'))
	
	def getMenuDic(self):
		menuDict = {}
		ext = '.py'
		
		# Add tools procedurally from ../mobuMenu
		self.mobuMenuPath = '%s/python/moBu/menu/' % gv.toolsLocation
		if self.mobuMenuPath[:2] == '//':
			# network, look for .pyc
			ext = '.pyc'
		for root, unused, unused in os.walk(os.path.abspath(self.mobuMenuPath)):
			if not Path(root).makePretty(lastSlash=False, backward=False) == self.mobuMenuPath:
				mFiles = []
				for fname in os.listdir(root):
					fullPath = '%s/%s' % (root, fname)
					if Path(fullPath).isfile() and fnmatch.fnmatch(fname, '*%s' % ext):
						mFiles.append(fname) 
				menuDict[Path(root).makePretty(lastSlash=False, backward=False)] = mFiles
		return menuDict, ext
	
	def createTool(self):
		moBuLogger.info('----------------------------------------')
		moBuLogger.info('|     Running Art Monkey v:%s     |' % _VERSION)
		moBuLogger.info('|     Build #:%s     |' % self.buildNumber)
		moBuLogger.info('----------------------------------------')
		
		pcsGlobalToolName = "Art Monkey"
		tool = FBCreateUniqueTool(pcsGlobalToolName)
		tool.StartSizeX = 500
		tool.StartSizeY = 120
		
		# Layout for the controls
		x = FBAddRegionParam(5, FBAttachType.kFBAttachLeft, "")
		y = FBAddRegionParam(0, FBAttachType.kFBAttachNone, "")
		w = FBAddRegionParam(50, FBAttachType.kFBAttachRight, "")
		h = FBAddRegionParam(85, FBAttachType.kFBAttachNone, "")
		tool.AddRegion("main", "main", x, y, w, h)
		
		# Add grid layout
		grid = FBGridLayout()
		tool.SetControl("main", grid)
		
		col = 0
		
		logo = FBButton()
		logo.SetImageFileNames('%s/logo_small.jpg' % self.pcsImagePath)
		logo.Caption = "yeah"
		logo.OnClick.Add(self.openToolDocs)
		grid.AddRange(logo, 0, 1, col, col)
		grid.SetColWidth( col, 70 )
		
		v = FBLabel()
		v.Caption = 'v:%s' % _VERSION
		v.Style = FBTextStyle.kFBTextStyleItalic
		v.Justify = FBTextJustify.kFBTextJustifyCenter
		grid.Add(v, 2, col)
		col +=1
		
		# create load button
		loadB = FBButton()
		loadB.Caption = "Load"
		loadB.Look = FBButtonLook.kFBLookColorChange
		loadB.OnClick.Add(self.KToolsCallback)
		
		# create save button
		saveB = FBButton()
		saveB.Caption = "Save"
		saveB.Look = FBButtonLook.kFBLookColorChange
		saveB.OnClick.Add(self.KToolsCallback)
		
		# create saveAs button
		saveAsB = FBButton()
		saveAsB.Caption = "SaveAs"
		saveAsB.Look = FBButtonLook.kFBLookColorChange
		saveAsB.OnClick.Add(self.KToolsCallback)
		
		# add buttons to row 1,2,3 column 1
		grid.Add(loadB, 0, col)
		grid.Add(saveB, 1, col)
		grid.Add(saveAsB, 2, col)
		
		# want to fix the width of column 1 and 2 so the buttons are of a normal size
		grid.SetColWidth( col, 40 )

		col +=1
				
		# create tab
		tab = FBTabControl()
		# we want the tab to span from row 0 to row 2 and from column 2 to column 2
		grid.AddRange(tab, 0, 2, col, col)
		
		# set the spacing between col0 and col1
		grid.SetColSpacing(col, 20)
		
		# now assign the rows and columns attributes
		# Fixed the height of row 0 and row 2 so the label and the buttons have a normal height
		grid.SetRowHeight(0, 20)
		grid.SetRowHeight(1, 20)
		grid.SetRowHeight(2, 20)
		
		# 1. Build a construction dictionary with {folder=[files]}
		self.menuDict, ext = self.getMenuDic()
		
		# 2. Sorted Keys list
		sKeys = []
		for dr in self.menuDict.iterkeys():
			sKeys.append(dr)
		sKeys.sort()
		
		for menu in sKeys:
			
			menuName = str(Path(menu).basename())
			# skip root and 'old'
			if not menuName == 'old' and not menuName == 'menu':
				lyt = FBHBoxLayout()
				lyt.default_space = 5
				lyt.SetRegionTitle("My Title", "Title")
				
				x = FBAddRegionParam(10, FBAttachType.kFBAttachLeft, "")
				y = FBAddRegionParam(20, FBAttachType.kFBAttachTop, "")
				w = FBAddRegionParam(140, FBAttachType.kFBAttachRight, "")
				h = FBAddRegionParam(75, FBAttachType.kFBAttachBottom, "")
				lyt.AddRegion(menuName, menuName, x, y, w, h)
		
				# must add dir to sys.path so imp can find it
				if not Path.modulePath(menu):
					sys.path.append(menu)
				
				for script in self.menuDict[menu]:
					if not script == '__init__%s' % ext:
						toolName = str(Path(script).namebase)
						lTool = FBButton()
						lTool.Caption = toolName
						lTool.Justify = FBTextJustify.kFBTextJustifyCenter
						
						# Make "Fix this!" red
						if toolName == 'Fix this!':
							lTool.Look = FBButtonLook.kFBLookColorChange
							lTool.SetStateColor(FBButtonState.kFBButtonState0, mbCore.Red)
							lTool.SetStateColor(FBButtonState.kFBButtonState1, mbCore.Red)
		
						# this callBack is active and all buttons will run this "last" menuModule.run()
						lTool.OnClick.Add(self.KToolsCallback)
						
						# add button to tabbed sub-layout
						lyt.Add(lTool, len(toolName) * 7)
			
				# add layouts to tabControl with name of dir
				tab.Add(menuName, lyt)
		
		# finish up tab
		tab.SetContent(0)
		tab.TabPanel.TabStyle = 0 # normal tabs
	
	def PCSmoBuMenu_metrics(self):
		""" Method to replace the mel based metrics """
		writeArr = []
		writeArr.append('Last Used On: %s' % datetime.datetime.now().strftime("%m/%d/%y : %H:%M:%S"))
		writeArr.append('Running From: %s' % gv.toolsLocation)
		writeArr.append('Mobu Version: %s %s' % (mbCore.moBuVersion(), mbCore.moBuBitVersion()))
		
		_file = open('%s/data/%s/%s.PCS' % (gv.schemaLocation, self.userName, self.userName), "w")
		for l in writeArr:
			l = l.strip()
			_file.write('%s\n' % l)
		_file.close()


def KFileCallbackMenu(control, event):
	# check for File Menu hacks
	if event.Name == "(PCS) Save As...":
		fp, pathname, description = imp.find_module("SaveAs")
		menuModule = imp.load_module("SaveAs", fp, pathname, description)
		menuModule.run()
	elif event.Name == "(PCS) Save...":
		fp, pathname, description = imp.find_module("Save")
		menuModule = imp.load_module("Save", fp, pathname, description)
		menuModule.run()
	elif event.Name == "(PCS) Open...":
		fp, pathname, description = imp.find_module("Load")
		menuModule = imp.load_module("Load", fp, pathname, description)
		menuModule.run()

def KToolsCallbackMenu(control, event):
	# check for documentation hack
	if event.Name == "Documentation":
		MoBuToolsMenu().openToolDocs(control, event)

def KToolsCallbackSubMenu(control, event):
	# import module
	try:
		fp, pathname, description = imp.find_module(str(event.Name))
		menuModule = imp.load_module(str(event.Name), fp, pathname, description)
		menuModule.run()
	except ImportError:
		moBuLogger.errorDialog("Unable to load and run module: '%s'" % event.Name)
	
#	# try to log tool usage
#	try:
#		ParsePCS().toolSet(pathname)
#	except:
#		moBuLogger.warning("Failed to log usage for tool '%s'" % pathname)

###################################################################		
# Have to run outside of a class or function, some kind of bug
###################################################################
# do File Menu
#TODO: Defer evaluation so hacks to top of menu?
menuMgrF = FBMenuManager()
mainMenuF = menuMgrF.GetMenu("&File")
mainMenuF.InsertFirst("(PCS) Save As...", 0)
mainMenuF.InsertFirst("(PCS) Save...", 1)
mainMenuF.InsertFirst("(PCS) Open...", 2)
mainMenuF.OnMenuActivate.Add(KFileCallbackMenu)

# do ArtMonkey Menu
menuMgr = FBMenuManager()
menuMgr.InsertBefore(None, "&Help", "ArtMonkey")
menu = menuMgr.GetMenu("ArtMonkey")
	
# Docs menu item first
docMenuItem = menu.InsertFirst("Documentation", 0)
menu.OnMenuActivate.Add(KToolsCallbackMenu)

menuDict, ext = MoBuToolsMenu().getMenuDic()

# 2. Sorted Keys list
sKeys = []
for dr in menuDict.iterkeys():
	sKeys.append(dr)
sKeys.sort()

count = 0
for menuNamePath in sKeys:
	menuName = str(Path(menuNamePath).basename())
	# skip root and 'old'
	if not menuName == 'old' and not menuName == 'mobuMenu':
		subMenu = FBGenericMenu()
		i = 0
		for script in menuDict[menuNamePath]:
			if not script == '__init__%s' % ext:
				toolName = str(Path(script).namebase)
				subMenu.InsertFirst(toolName, i)
				i+=1
				
		subMenu.OnMenuActivate.Add(KToolsCallbackSubMenu)
		menu.InsertLast(menuName, 101+count, subMenu)
		count+=1

###################################################################

	
if __name__ == "__builtin__":
#	MoBuToolsMenu().createTool()
	pass
else:
	print "moBu.pcsGlobalMenu imported"
