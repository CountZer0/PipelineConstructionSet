'''
Author: Jason.Parks
Created: April 25, 2012
Module: core.moBuNamespace
Purpose: Namespace convenience class
'''
from pyfbsdk import *
from common.diagnostic.pcsLogger import moBuLogger
from moBu.core.moBuCore import MoBuCore

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
	
mbNamespace = MoBuNamespace()

print "core.moBuNamespace imported" 