import xml.sax.handler

import tempfile
import getopt
import os
import urllib2
import xml.etree.ElementTree as ElementTree
import sys
import webbrowser
import xml
import maya

class Request:
    def __init__(self):
        pass
    
    
    def setPreview(self, preview):
        pass
    
    
    def setToNativeVersion(self):
        pass
    
    
    def setVersion(self, line, release, master, build):
        pass
    
    
    def url(self):
        pass


class ParsingErrorHandler(xml.sax.handler.ErrorHandler):
    """
    ErrorHandler handles the errors encountered while parsing
    an XML from a string
    """
    
    
    
    def __init__(self, url):
        pass
    
    
    def error(self, exception):
        pass
    
    
    def fatalError(self, exception):
        pass
    
    
    def format(self, exception):
        pass


class HtmlUpdate:
    """
    This class will take an HTML content and modify it, replacing
    sections with update specific information.  One can
    specify sections that show up if there are no updates
    and sections that show up if there are updates.  In the
    later case, certain sections can be specified to be repeated
    for each update, using the update information.
    """
    
    
    
    def __init__(self, title, response):
        pass
    
    
    def process(self, html):
        pass


class HtmlTemplateUpdate:
    def __init__(self):
        pass
    
    
    def process(self, html):
        pass
    
    
    def processSingle(self, html):
        pass
    
    
    def processSingleNone(self, html):
        pass
    
    
    def processSingleSome(self, html):
        pass


class Response:
    def __init__(self, request, doRefresh=True):
        pass
    
    
    def numberOfUpdates(self, forceRefresh=False):
        pass
    
    
    def refresh(self, setTimeout=None):
        pass
    
    
    def resetRequest(self, request):
        pass
    
    
    def result(self, forceRefresh=False):
        pass



def Update(response, output):
    pass


def downloadURL(url):
    """
    http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
    """

    pass


def Download(response, output):
    pass


def usage():
    pass



