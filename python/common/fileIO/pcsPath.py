'''
Author: Jason.Parks
Created: April 17, 2012
Module: common.fileIO.Path
Purpose: custom Path class wrapper
'''

from common.fileIO.path import *
import os, stat
import sys

class Path(path):
	'''
	PipelineConstructionSet sub-class of pymel's path class (which came from Jason Orendorff's implementation in Python 2.2)
	'''
	
	def toP4Path(self):
		''' Convert path to perforce path '''
		self = self.makePretty()
#		return '//depot/%s' % self[3:]
		return '//%s' % self[3:]
	
	def makePretty(self, lastSlash=True, backward=False):
		''' cleans up the look of the paths
			Params:
				lastSlash: keep or remove the last slash in a directory path
				backward: replace with backward or forward slashes
			Returns: Path() class object
		'''
		slashChr = '/'
		if backward:
			slashChr = '\\'
		
		# check for initial double forward slash
		network = False
		if self[:2] == '//' or self[:2] == '\\\\':
			network = True
		
		# convert to forward or backward
		for unused in range(0, 4):
			# Removal of double forward slashes
			self = self.replace('//', slashChr)
			self = self.replace('\\', slashChr)
			self = self.replace('/', slashChr)
				
		# check tail if dir
		if os.path.isdir(self):
			if self[-1:] == '/':
				if not lastSlash:
					self = self[:-1]
			else:
				if lastSlash:
					self = self + slashChr
		
		# reinstate initial double forward slash
		if network:
			if backward:
				self = '\\%s' % self
			else:
				self = '/%s' % self
				
		return Path(self)

	@property
	def pretty(self):
		''' Property, do not use ()'''
		return self.makePretty()
	
	@property
	def prettyWOSlash(self):
		''' Property, do not use ()'''
		return self.makePretty(lastSlash=False)
	
	@property	
	def isbin(self):
		""" 
		Property, do not use ()
		
		Description:	Tests for binary? 
		Inputs:	path
		Returns: True/False
		""" 
		fd = open(self, 'rb')
		for b in fd.read():
			if ord(b) > 127:
				fd.close()
				return True
			fd.close()
		return False
	
	@property
	def isReadOnly(self):
		''' Property, do not use ()'''
		fileAtt = os.stat(self)[0]
		if (not fileAtt & stat.S_IWRITE): 
			return 1
		else:
			return 0

	@property
	def isWritable(self):
		''' Property, do not use ()'''
		fileAtt = os.stat(self)[0]
		if (not fileAtt & stat.S_IREAD): 
			return 1
		else:
			return 0
	
	def makeReadOnly(self, _dir=False):
		''' make file(s) readOnly
			Params:
				_dir: if process entire directory
			Returns: True/False
		'''
		
		success = True
		
		if _dir:
			# check for dir passed
			if self.isdir:
				for _file in self.walk():
					os.chmod(_file, stat.S_IREAD)
					if self.isWritable:
						success = False
			else:
				print "%s is not a directory"
		else:
			# process single
			if self.exists:
				os.chmod(self, stat.S_IREAD)
				if self.isWritable:
					success = False
			else:
				print "%s does not exists" % self
		
		return success
	
	def makeWritable(self, _dir=False):
		''' make file(s) non-readOnly
			Params:
				_dir: if process entire directory
			Returns: True/False
		'''
		success = True
		
		if _dir:
			# check for dir passed
			if self.isdir:
				for _file in self.walk():
					os.chmod(_file, stat.S_IWRITE)
					if self.isReadOnly:
						success = False
			else:
				print "%s is not a directory"
		else:
			# process single
			if self.exists:
				os.chmod(self, stat.S_IWRITE)
				if self.isReadOnly:
					success = False
			else:
				print "%s does not exists" % self
		
		return success
		
	def modulePath(self):
		found = 0
		for p in sys.path:
			if p == self:
				found = 1
		if found:
			return True
		else: return False 	
			
	def string(self):
		return str(self)

	
print "common.fileIO.Path imported"
