import sys
import os
#from os import path, walk
import json
import uuid
from datetime import datetime

FileCount=1
RootFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_Games'
EndPath = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgatour/season5/apr03/Converted'
# f = []

def FindFile2Convert(SrcFolder):
    FolderList=[]
    for filename in os.listdir(SrcFolder):
        if filename.endswith(".htm"):
            FolderList.append(filename)
    return FolderList
RootFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_Games'
files= FindFile2Convert(RootFolder)
print(files.count)
def ReadInDataFile(HTMLFile):
    f=""
    with open(HTMLFile, 'r') as infile:
		f = infile.read()  # Read the contents of the file into memory.
# Return a list of the lines, breaking at line boundaries.
    ReduceList=f.splitlines()
    Marker =0
    for i,line in enumerate(ReduceList):
        if body_str in line:
            Marker=i
    #ReduceList[Marker:]

    return ReduceList[Marker:]


