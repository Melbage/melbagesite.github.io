import sys
import  os
import json

def FindFile2Convert(SrcFolder):
    FolderList=[]
    for filename in os.listdir(SrcFolder):
        if filename.endswith(".htm"):
            FolderList.append(filename)
    FolderList.sort()
    return FolderList

#Reads in a blank JSON template for scorecard
def ReadJSONSchema(FileJSONLocation):
    #Read JSON schema.
   with open(FileJSONLocation) as Schema:
    JSONRecord= json.load(Schema)
    Schema.close()
    return JSONRecord

# create a blank record list
def TrackerRecordset(FileList,RecordJSON):
    #FRecords=ReadJSONSchema(RecordJSON)
    #FileRecords=FRecords
    FileRecords=ReadJSONSchema(RecordJSON)
    #with open('TrackerData.json') as FD:
    data = [] #json.load(FD)
    for item in FileList:
        FileRecords=ReadJSONSchema(RecordJSON)
        FileRecords['FileName'] = item
        FileRecords['Status']='NotTried'
        FileRecords['Message']=''
        data.append(FileRecords)
        #FileRecords=FRecords
        
        #data[FC]=FileRecords
    #print(data)
    with open('TrackerData.json') as FD:
        json.dumps(data,FD,indent=4)

    return(data)



#global PlayerScoreCard
global ConvertFileName
#ConvertFileName=''
#Static Varibiles
global RootFolder 
global TargetJSONFolder
global TargetHTMLFolder 
#Set static Varibiles
RootFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_Games'
TargetJSONFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_JSON'
TargetHTMLFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_HTML'
#Following folder were found to have different lenght data files. so slip them into groups.
F223Folder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/RAW/223'
F224Folder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/RAW/224'
OtherFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/RAW/other'
FolderJSON= '/Users/paulcarter/Documents/GITHUB/Melbage/Melbagesite/melbagesite.github.io/Code/JSON/Data/'

TrackerFile='FileTracker.json'

#Create a list of files to convert
FileList= FindFile2Convert(RootFolder)
JSONfile=FolderJSON+TrackerFile
Recordset= TrackerRecordset(FileList,JSONfile)
print(Recordset)

