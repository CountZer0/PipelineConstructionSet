'''
Author: Jason.Parks
Created: Jan 17, 2012
Module: moBu.moBuNamespace
Purpose: Namespace convenience class
'''
from pyfbsdk import *
from common.diagnostic.pcsLogger import moBuLogger
from moBu.core.moBuCore import MoBuCore
from moBu.core.moBuSets import mbSets

# eclipseSyntax
if False: from pyfbsdk_gen_doc import * #@UndefinedVariable @UnusedWildImport


class MoBuNamespace(MoBuCore):
	
	def __init__(self):
		""" MoBuNamespace.__init__():  set initial parameters """
		super(MoBuNamespace, self).__init__()
		
	def addNamespace(self, node=None, ns='', hier=False):
		''' adds a namespace
			Params:
				node: node to add to
				ns: namespace to add
				hier: process hierarchy or not
			Returns: True/False
		'''
		if not node:
			moBuLogger.error("No node passed.")
		if not ns:
			moBuLogger.error("No namespace passed.")
		
		# skip if namespace already there
		if ns in node.LongName:
			moBuLogger.debug("'%s' already in object: '%s'" % (ns, node.LongName))
			return False
		
		try:
			if hier:
				node.ProcessNamespaceHierarchy(FBNamespaceAction.kFBConcatNamespace, ns, None, False)
			else:
				node.ProcessObjectNamespace(FBNamespaceAction.kFBConcatNamespace, ns, None, False)
		except:
			return False
		return True 

	def getAllNamespaces(self):
		''' removes all namespaces
			Params: none
			Returns: list of Namespaces/False
		'''
		EXTRAnameSPACES = ['Transport Controls  -  Keying Group', 'Take 001', 'CharacterTool']
		allNamespaces = []
		for comp in self.getAllByType(_type='all'):
			
			splitByColon = comp.LongName.split(':')
			for i in range(len(splitByColon) - 1):
				nSpace = splitByColon[i]
				if not nSpace in allNamespaces and not nSpace in EXTRAnameSPACES:
					allNamespaces.append(nSpace)
			
			# also add multi-Namespaces
			if len(splitByColon) > 2:
				nSpace = splitByColon[0]
				for i in range(1, len(splitByColon) - 1):
					nSpace += ':%s' % splitByColon[i]
					if not nSpace in allNamespaces and not nSpace in EXTRAnameSPACES:
						allNamespaces.append(nSpace)
		
		if len(allNamespaces) == 0:
			allNamespaces = False
				
		return allNamespaces
	
	def getNamespace(self, node=None):
		''' returns namespaces on node
			Params:
				node: node to remove from
				hier: process hierarchy or not
			Returns: list of namespaces /False
		'''
		if not node:
			moBuLogger.error("No node passed.")

		nameSpaces = []			
		splitByColon = node.LongName.split(':')
		for i in range(len(splitByColon) - 1):
			nameSpaces.append(splitByColon[i])
			
		if not nameSpaces:
			return False
		
		return nameSpaces
						
	def removeAllNamespaces(self, node=None, hier=False):
		''' removes all namespaces
			Params:
				node: node to remove from
				hier: process hierarchy or not
			Returns: True/False
		'''
		if not node:
			moBuLogger.error("No node passed.")
		try:
			if hier:
				node.ProcessNamespaceHierarchy(FBNamespaceAction.kFBRemoveAllNamespace, "")
			else:
				node.ProcessObjectNamespace(FBNamespaceAction.kFBRemoveAllNamespace, "")
		except:
			return False
		return True
	
	def removeAllNamespacesFromScene(self):
		try:
			for lComp in FBSystem().Scene.Components:
				# This function is a recursive function that will go through the whole hierarchy to add or replace the prefix
				lComp.ProcessNamespaceHierarchy (FBNamespaceAction.kFBRemoveAllNamespace   , '', '', False)
			moBuLogger.info("Removed all namespaces")
			return True
		except:
			moBuLogger.info("Failed to removed all namespaces")
			return False
				
	def replaceNamespace(self, node=None, nsOrig='', nsReplace='', hier=False):	
		''' replaces all namespaces
			Params:
				node: node to replace
				nsOrig: namespace to replace
				nsReplace: new namespace
				hier: process hierarchy or not
			Returns: True/False
		'''
		if not node:
			moBuLogger.error("No node passed.")
		if not nsOrig:
			moBuLogger.error("No namespace passed.")
		if not nsReplace:
			moBuLogger.error("No namespace passed.")
		try:
			if hier:
				node.ProcessNamespaceHierarchy(FBNamespaceAction.kFBReplaceNamespace, nsOrig, nsReplace, False)
			else:
				node.ProcessObjectNamespace(FBNamespaceAction.kFBReplaceNamespace, nsOrig, nsReplace, False)
		except:
			return False
		return True
	
	def replaceNamespaceOnChar(self, nSpace='', quiet=False):
		''' replace namespace on character or add if none
			Params:
				nSpace: namespace to add/replace with
				quiet: suppress message
			Returns: True/False
		'''
		
		success = True
		
		# get selected reference or find it
		selected = self.getSelected(_type='all', found=True)
		if not selected:
			# try to select
			selected = self.getReference(namespace='', pyMB=False)
			if not selected:
				# run again
				if not quiet:
					moBuLogger.errorDialog("Select a node from the character")
				else:
					moBuLogger.error("Select a node from the character")
				return False
		
		# get the FBSet associated with the character
		if isinstance(selected, FBSet):
			charSet = selected
		else:
			charSet = mbSets.findSetFromObject(pObject=selected, quiet=quiet)
		if not charSet:
			return False
	
		# iterate through all items in set		
		for item in charSet.Items:
			# check if already has namespaces
			currentNS = None
			if mbNamespace.getNamespace(node=item):
				for ns in mbNamespace.getNamespace(node=item):
					# do NOT replace '*_Template' Namespaces
					if not '_Template' in ns:
						currentNS = ns
						
						# check for replace or add
						if not mbNamespace.replaceNamespace(node=item, nsOrig=currentNS, nsReplace=nSpace, hier=False):
							moBuLogger.debug("Failed to replaceNamespace on: '%s'" % item.LongName)
							success = False
					else:	#_Template Namespace
						# check for existence of new nSpace
						if not nSpace in mbNamespace.getNamespace(node=item):
							# add
							if not mbNamespace.addNamespace(node=item, ns=nSpace, hier=False):
								moBuLogger.debug("Failed to addNamespace on: '%s'" % item.LongName)
								success = False
			else:
				if not mbNamespace.addNamespace(node=item, ns=nSpace, hier=False):
					moBuLogger.debug("Failed to addNamespace on: '%s'" % item.LongName)
					success = False
			
		# add nameSpace to set as well
		if not mbNamespace.addNamespace(node=charSet, ns=nSpace, hier=False):
			moBuLogger.debug("Failed to addNamespace on: '%s'" % charSet.LongName)
			# no need to report False, already getting added
		
		return success

mbNamespace = MoBuNamespace()

print "core.moBuNamespace imported" 
