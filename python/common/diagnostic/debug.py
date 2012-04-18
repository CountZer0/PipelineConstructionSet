'''
Author: Jason.Parks
Created: Apr 12, 2012
Module: common.diagnostics.debug
Purpose: to import debug methods
'''

from diagnostic import wingdbstub
from diagnostic.pcsLogger import logger

class Debug(object):
	'''
	General class to hold methods to help debugging from any DCC app
	'''

	def __init__(self):
		'''
		Constructor
		'''
		
		
	def connectToWing(self):
		"""
		SYNOPSIS
		 Connects to wingIDE debugger	 
		
		INPUTS NONE
		 
		RETURNS: Nothing 
		"""
#		from diagnostics import wingdbstub
		try:
			wingdbstub.Ensure()
			logger.info('Connected to wingIDE')
			print 'Connected to wingIDE'
			return True
		except ValueError:
			logger.info('Could NOT connect to wingIDE')
			print 'Could NOT connect to wingIDE'
			return False
	
	def connectToEclipse(self, host='localhost'):
		"""
		SYNOPSIS
		 Connects to Eclipse PyDev debug server	 
		
		INPUTS NONE
		 
		RETURNS: Nothing 
		"""
		from diagnostic.pydevDebug import pydevd
		try:
			pydevd.settrace(host=host, stdoutToServer=True, stderrToServer=False, suspend=False)
			print 'Connected to Eclipse'
		except: print 'Could NOT connect to Eclipse'

print "common.diagnostics.debug imported"
