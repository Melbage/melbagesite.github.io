import sys
import os
#from os import path, walk
import json
import uuid
from datetime import datetime

FileCount=1
RootFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_Games'
EndPath = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/RAW'
# f = []

def FindFile2Convert(SrcFolder):
    FolderList=[]
    for filename in os.listdir(SrcFolder):
        if filename.endswith(".htm"):
            FolderList.append(filename)
    FolderList.sort()
    return FolderList

def ReadInDataFile(HTMLFile):
    # File to be loaded.
    f=""
    CleanList=[]
    # String to match in file.
    #body_str = "<!--START OF OUTPUT FROM EXCEL PUBLISH AS WEB PAGE WIZARD"
    td_Tag = "<td"
    div_Tag ="<div"
    #Counter in files for line with above string to match
    ReadFile=RootFolder+'/'+HTMLFile
    with open(ReadFile, 'r') as infile:
		FileInMemory = infile.read()  # Read the contents of the file into memory.
    infile.close()
    # Return a list of the lines, breaking at line boundaries.
    ReduceList=FileInMemory.splitlines()
    
    #Remove any lines which begin with <col from data 
    for GoodLine in ReduceList:
        if td_Tag  in GoodLine:
            CleanList.append(GoodLine)
        if div_Tag in GoodLine:
            CleanList.append(GoodLine)
     #Only return the data from the HTLM and not the 
    return CleanList

def WriteRawData(CleanedData,filename):
    f=open(EndPath+'/'+filename,'w')
    for i,line in enumerate(CleanedData):
        f.write(str(i)+': '+line+'\n')
    f.close()  
    return

RootFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_Games'
files= FindFile2Convert(RootFolder)
for file in files:
    RawData=ReadInDataFile(file)
    WriteRawData(RawData,file)

#print(files.count)
#print('File one is ',files[1])


