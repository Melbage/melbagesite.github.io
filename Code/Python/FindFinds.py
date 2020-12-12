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

# for (dirpath, dirnames, filenames) in walk(RootFolder,topdown=False):
#     for file in filenames:
#             #yield os.path.join(root,file)
#             #f.extend(filenames)
#             FileCount+=FileCount+1
#     #break
# print(FileCount)
# check file are of the right type
# FileList = list()
# for i in f:
# 	if i.find('.htm') != -1:
# 		print( i)
# 		FileList.append(i)
# for dirpath, dirnames, filenames in walk(RootFolder):
#     directory_level = dirpath.replace(macpath, " ")
#     directory_level = directory_level.count(sep)
#     indent = " " * 4
#     print("{}{}/".format(indent*directory_level, path.basename(dirpath)))
#     for f in filenames:
#         print("{}{}".format(indent*(directory_level+1), f))
#         FileCount+=FileCount+1
print(FileCount)

# for filename in os.listdir(RootFolder):
#     if filename.endswith(".htm"):
#         FileCount+=1
#         if(len(filename)>=14):
#             PM=filename[:-4]
#             if(PM[-2:]=='pm'):
#                 print("PM 1",filename,FileCount,len(filename),PM[-2:])
#             elif(PM[-2:]=='m2'):
#                 print("PM 2",filename,FileCount,len(filename),PM[-2:])
#             else:
#                 print("AM",filename,FileCount,len(filename),PM[-2:])
#         #continue
#     else:
#         continue
# print(FileCount)

def FindFile2Convert(SrcFolder):
    FolderList=[]
    for filename in os.listdir(SrcFolder):
        if filename.endswith(".htm"):
            FolderList.append(filename)
    return FolderList
RootFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_Games'
files= FindFile2Convert(RootFolder)
print(files.count)

