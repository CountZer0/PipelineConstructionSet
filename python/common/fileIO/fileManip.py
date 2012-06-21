'''
Author: jason
Created: Jun 20, 2012
Module: common.fileIO.fileManip
Purpose: basic file utilities
'''

from common.perforce import pcsP4
from os import path
import re


class FileManip(object):
    """	Class for generic file manipulation """

    def __init__(self, maya=1):
        super(FileManip, self).__init__()

#        self.p4Obj = pcsP4.P4Lib(maya)
#        self.apParseObj = parser_AP.ParseAP()

    ##################################################################################################################################
    ##	Generic methods																												##
    ##################################################################################################################################	
    def searchReplace(self, treatFile, sDict):
        """ 
        Description: Method to search and replace in a file
        Inputs:	treatFile = File to search and replace in
        		sDict = A dictionary of search and replace terms 
        Returns: Nothing
        """
        # Open file and store content
        uFile = open(treatFile, 'r')
        content = uFile.readlines()
        uFile.close()

        # Search and replace
        updatedContent = []
        for l in content:
            for key in [key for key in sDict.keys() if re.search(key,l)]:
                l=l.replace(key, sDict[key])
            updatedContent.append(l)

        # Write result
        uFile = open(treatFile, 'w')
        uFile.writelines(updatedContent)
        uFile.close()

    def removeEmptyLines(self, treatFile):
        """ 
        Description:	Removes empty lines from files 
        Inputs:	treatFile = File to remove emty lines in
        Returns: Nothing
        """ 

        if path.exists(treatFile):
            f = open(treatFile)
            l = [l for l in f.readlines() if l.strip()]
            f.close()
            f = open(treatFile, "w")
            f.writelines(l)
            f.close()

    ##################################################################################################################################
    ##	Generic string methods																										##
    ##################################################################################################################################	

    def strNumberGenerator(self, nBase, numberBase=3):
        """ 
        Description:	Generates 01, 001, 0001 type string representations 
        Inputs:		nBase - int number to treat
        			numberBase* = Total numbers in the string
        Returns: The string number		
        """	
        if nBase > 1:
            floatRep = float(float(nBase)/(10**float(numberBase)))
            strRep = str(floatRep).split('.')[1]
            if nBase>9:
                strRep = '%s0' % strRep
            if nBase>99:
                strRep = '%s0' % strRep
            if nBase>999:
                strRep = '%s0' % strRep
            if nBase>9999:
                strRep = '%s0' % strRep
            if nBase>99999:
                strRep = '%s0' % strRep
            if nBase>999999:
                strRep = '%s0' % strRep
        else:
            floatRep = float(float(nBase)/(10**float(numberBase)))
            strRep = str(floatRep).split('.')[1]

        return strRep			


    ##################################################################################################################################
    ##	Generic XML methods																											##
    ##################################################################################################################################

    def writeCleanXML(self, xmlFile, xmlData, indent='', addindent='\t', newl='\n', encoding = 'utf-8'):
        """ Method to update the wear set xml file """
        file = open(xmlFile, "w" ) #@ReservedAssignment
        xmlData.writexml(file, indent, addindent, newl, encoding)
        file.close()
        self.removeEmptyLines(xmlFile)


fManip = FileManip()


print "common.fileIO.fileManip imported"