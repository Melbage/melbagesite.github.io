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
print('File one is ',files[1])

