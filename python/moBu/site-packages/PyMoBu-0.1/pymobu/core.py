# PyMoBu - Python enhancement for Autodesk's MotionBuilder
# Copyright (C) 2010  Scott Englert
# scott@scottenglert.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
Module for more general functions
'''
import re
from pyfbsdk import FBSystem #@UnresolvedImport
from pyfbsdk import FBProgress #@UnresolvedImport

# get the whole list of components
kAllSceneComponents = FBSystem().Scene.Components

def deselect(pattern=None, **kwargs):
    '''
    Deselects objects that match the given parameters
    See ls function for available arguments
    '''
    kwargs['selected'] = True
    
    if not hasattr(pattern, '__iter__'):
        pattern = [pattern]
    
    for item in pattern:
        matched = ls(pattern=item, **kwargs)
        for obj in matched:
            try:
                obj.component.Selected = False
            except:
                obj.Selected = False

def select(pattern=None, add=False, toggle=False, **kwargs):
    '''
    Selects objects that match the given parameters
    @param add: add the matched objects to the selection
    @param toggle: toggles the selection of the matched objects
    See ls function for additional arguments
    '''
    if not hasattr(pattern, "__iter__"):
        pattern = [pattern]
    
    kwargs.pop('selected', None)
    
    if not add and not toggle:
        deselect(pattern=None, **kwargs)
    
    if toggle:
        def selectFunc(x):
            try:
                x.component.Selected = not x.component.Selected
            except:
                x.Selected = not x.Selected
    else:
        def selectFunc(x):
            try:
                x.component.Selected = True
            except:
                x.Selected = True
                
    for item in pattern:
        matched = ls(pattern=item, **kwargs)
        map(selectFunc, matched)
    
def delete(pattern=None, **kwargs):
    '''
    Deletes objects that match the given parameters
    See ls function for additional arguments
    '''
    if not hasattr(pattern, "__iter__"):
        pattern = [pattern]
    
    for item in pattern:
        matched = ls(pattern=item, **kwargs)
        for obj in matched:
            try:
                obj.component.FBDelete()
            except:
                obj.FBDelete()

def ls(pattern=None, _type=None, selected=None, visible=None, includeNamespace=True):
    '''
    Similar to Maya's ls command - returns list of objects that match the given parameters
    @param pattern: name of an object with with optional wild cards '*'
    @param _type: object to compare if the component is of that type (either string or python class/type)
    @param selected: True/False if the object is selected or not. Default is either
    @param visible: True/False if the object is visible. Default is either 
    @param includeNamespace: does the search use the complete name (with namespace)  Default True
    '''
    # set up the name testing based on the pattern
    if pattern:
        # create a name return function
        if includeNamespace:
            getName = lambda x: getattr(x, 'LongName', x.Name)
        else:
            getName = lambda x: x.Name
        
        # if there is a wild card in the pattern
        if '*' in pattern:
            pattern = pattern.replace('*', '.*')
            # name testing function
            passesNameTest = lambda x: re.match(pattern, getName(x))
        else:
            passesNameTest = lambda x: pattern == getName(x)       
    else:
        passesNameTest = lambda x: True

    # for getting selection test
    if selected is not None:
        passesSelectionTest = lambda x: x.Selected == selected
    else:
        passesSelectionTest = lambda x: True
    
    # for getting visibility test
    if visible is not None:
        passesVisibilityTest = lambda x: visible == bool(getattr(x, 'Visibility', False))
    else:
        passesVisibilityTest = lambda x: True
    
    # for testing the type of component
    if _type:
        # if they gave a string, evaluate it
        if isinstance(_type, basestring):
            try:
                _type = eval(_type)
            except NameError:
                raise NameError("Can not find object type '%s' in current namespace" % _type)

        passesTypeTest = lambda x: isinstance(x, _type)
    # no type was given so its True by default
    else:
        passesTypeTest = lambda x: True
               
    matchList = []
    for cmpnt in kAllSceneComponents:
        # if we did not pass the selection test, continue on
        if not passesSelectionTest(cmpnt):
            continue
        # check if the object is visible
        if not passesVisibilityTest(cmpnt):
            continue
        # do the same for matching type
        if not passesTypeTest(cmpnt):
            continue
        
        if passesNameTest(cmpnt):
            # try converting it to a pymobu object
            try:
                pmbCmpnt = cmpnt.ConvertToPyMoBu()
            except:
                pmbCmpnt = cmpnt
                
            matchList.append(pmbCmpnt)
                   
    return matchList

def progressBarIterator(func, items):
    '''Function that displays a progress while looping a list of items through the function'''
    # can't figure out why it doesn't work
    # may convert this to a generator
    progressBar = FBProgress()
    progressBar.Caption = str(func.__name__)
    ret = []
    num = len(items)
    try:
        for i, item in enumerate(items):
            progressBar.Text = str(item)
            progressBar.Percent = int(i/num)
            ret.append(func(item))
    finally:
        progressBar.FBDelete()
    
    return ret

################################
# set up decorators            #
################################
def decorated(origFunc, newFunc, decoration=None):
    """
    Copies the original function's name/docs/signature to the new function, so that the docstrings
    contain relevant information again. 
    Most importantly, it adds the original function signature to the docstring of the decorating function,
    as well as a comment that the function was decorated. Supports nested decorations.
    """
    if not hasattr(origFunc, '_decorated'):
        # a func that has yet to be treated - add the original argspec to the docstring
        import inspect
        newFunc.__doc__ = "Original Arguments: %s\n\n%s" % (
            inspect.formatargspec(*inspect.getargspec(origFunc)), 
            inspect.getdoc(origFunc) or "")
    else:
        newFunc.__doc__ = origFunc.__doc__ or ""
    newFunc.__doc__ += "\n(Decorated by %s)" % (decoration or "%s.%s" % (newFunc.__module__, newFunc.__name__))
    newFunc.__name__ = origFunc.__name__
    newFunc.__module__ = origFunc.__module__
    newFunc.__dict__ = origFunc.__dict__    # share attributes
    newFunc._decorated = True   # stamp the function as decorated

def decorator(func):
    """
    Decorator for decorators. Calls the 'decorated' function above for the decorated function, to preserve docstrings.
    """
    def decoratorFunc(origFunc, *x):
        args = (origFunc,) + x
        if x:
            origFunc = x[0]
        newFunc = func(*args)
        decorated(origFunc, newFunc, "%s.%s" % (func.__module__, func.__name__))
        return newFunc
    decorated(func,decoratorFunc, "%s.%s" % (__name__, "decorator"))
    return decoratorFunc