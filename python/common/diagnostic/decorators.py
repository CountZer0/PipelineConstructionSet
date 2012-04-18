'''
Author: Jason.Parks
Created: Apr 17, 2012
Module: common.diagnostic.decorators
Purpose: some convenient decorators
'''

import hotshot.stats
import profile
import warnings

def deprecated(funcOrMessage, className=None):
	"""the decorator can either receive parameters or the function directly.

	If passed a message, the message will be appended to the standard deprecation warning and should serve to further
	clarify why the function is being deprecated and/or suggest an alternative function

	the className parameter is optional and should be included if the function is a method, since the name of the class
	cannot be automatically determined.
	"""
	#@decorator
	def deprecated2(func):
		info = dict(
			name = func.__name__,
			module = func.__module__)

		def deprecationLoggedFunc(*args, **kwargs):
			warnings.warn(message % info, DeprecationWarning, stacklevel=2)  # add to the stack-level so that this wrapper func is skipped
			return func(*args, **kwargs)

		deprecationLoggedFunc.__name__ = func.__name__
		deprecationLoggedFunc.__module__ = func.__module__
		deprecationLoggedFunc.__doc__ = message % info + '\n'
		if func.__doc__:
			deprecationLoggedFunc.__doc__ += '\n' +  func.__doc__
		return deprecationLoggedFunc

	if className:
		objName = '%(module)s.' + className + '.%(name)s'
	else:
		objName = '%(module)s.%(name)s'
	basemessage = message = "The function '" + objName + "' is deprecated and will become unavailable in future artMonkey versions"
	# check if the decorator got a 'message' parameter
	if isinstance(funcOrMessage, basestring):
		message = basemessage + '. ' + funcOrMessage
		return deprecated2
	else:
		message = basemessage
		return deprecated2(funcOrMessage)

def profileit(printlines=1):
	def _my(func):
		def _func(*args, **kargs):
			prof = hotshot.Profile("profiling.data")
			res = prof.runcall(func, *args, **kargs)
			prof.close()
			stats = hotshot.stats.load("profiling.data")
			stats.strip_dirs()
			stats.sort_stats('time', 'calls')
			print ">>>---- Begin profiling %s" % func
			stats.print_stats(printlines)
			print ">>>---- End profiling %s" % func
			return res
		return _func
	return _my

class myDecorator(object):

	def __init__(self, f):
		print "inside myDecorator.__init__()"
		f() # Prove that function definition has completed

	def __call__(self):
		print "inside myDecorator.__call__()"

class entryExit(object):

	def __init__(self, f):
		self.f = f

	def __call__(self, **kwargs):
		print "Entering", self.f.__name__
		self.f()
		print "Exited", self.f.__name__
		
class proTest(object):
	def __init__(self, f):
		self.f = f
		
	def __call__(self, **kwargs):
		
		#profile.run('ap_rigging.%s(%s)' % (self.f, kwargs), 'C:/temp/profile.txt')
		profile.run('%s(%s)' % (self.f, kwargs), 'C:/temp/profile.txt')
		import pstats
		p = pstats.Stats('C:/temp/profile.txt')
		p.sort_stats('cumulative').print_stats(10)

class myProf(object):

	def __init__(self, f):
		self.f = f
	
	def __call__(self, **kwargs):
		profile.run("%s(%s)" % (self.f(), kwargs), 'C:/temp/profile.txt')
		print "\n**********%s(%s)***********\n" % (self.f(), kwargs)
		import pstats
		p = pstats.Stats('C:/temp/profile.txt')
		p.sort_stats('time').print_stats(10)
		
def profile_module(path, module, **kwargs):
	profile.run('%s.%s(%s)' % (path, module, kwargs), 'C:/temp/profile.txt')
	import pstats
	p = pstats.Stats('C:/temp/profile.txt')
	p.sort_stats('cumulative').print_stats(10)

print "common.diagnostic.decorators imported"