import sys
import  os
import json
import uuid
from datetime import datetime

#Create a list of HTML files to be converted. 
def FindFile2Convert(SrcFolder):
    #Create a JSON format for recording the status of the where we are.
    FileRecord={""}
    FolderList=[]
    for filename in os.listdir(SrcFolder):
        if filename.endswith(".htm"):
            FolderList.append(filename)
    FolderList.sort()
    return FolderList


#Reads in a blank JSON template for scorecard
def ReadJSONSchema():
    #Read JSON schema.
   with open('/Users/paulcarter/Documents/GITHUB/Melbage/Melbagesite/melbagesite.github.io/Code/JSON/Data/PlayersScoreCardTmplate.json') as Schema:
    SCasJSON= json.load(Schema)
    return SCasJSON

#Remove unwanted HTML charaters from strings
def Remove_nbsp(nbsp):

        #Test to see if there is a non-breaking space and if so replace it with zero
    if(nbsp=='&nbsp;'): nbsp = '0'
    return nbsp

#Cuts out the data from the line 
def RemoveData(LineOfData):
    #Function to remove the HTML from the data line and return just the data cleaned ready for assihgning to value
    #HTML data is held betwene the following tabs > and </td>
    BetweenThis = '>'
    BetweenThat = '</td>'
    CleanLineOfData = LineOfData[LineOfData.find(BetweenThis)+1:LineOfData.find(BetweenThat)]
    #Now Remove non-breaking space 
    CleanLineOfData = Remove_nbsp(CleanLineOfData)
    return CleanLineOfData.decode('utf-8', 'ignore')

#Converts dates in to correct format for use else where
def FormatDate(DateStringObject):
    #check for blank string
    if(DateStringObject=='0'):
        DateStringObject='01/01/1970'
    #check for data with am and remove it from the date
    if(DateStringObject[-2:] =='am'):
        DateStringObject = DateStringObject[:-2]
       #check for data with pm and remove it from the date
    if(DateStringObject[-2:] =='pm'):
        DateStringObject = DateStringObject[:-2]
    #Remove all any spaces from string.    
    DateStringObject = DateStringObject.strip()
    #check that date is using YYYY or YY format
    if(len(DateStringObject)>=9):
        DateObject = datetime.strptime(DateStringObject, '%d/%m/%Y') #Covert date string to Dateformat eg 26/04/03
    else:
        DateObject = datetime.strptime(DateStringObject, '%d/%m/%y') #Covert date string to Dateformat eg 26/04/03
    DateStringObject = DateObject.strftime('%Y%m%d') #Convert Date object to required string format eg 20030426
    return DateStringObject

#Find the inintals of the player
def PlayerInitals(FileNameString):
    #Find the place of the first digit in string
    #As the files have the initals as the first part of the name
     
    for i, DigitLocation in enumerate(FileNameString):
        if DigitLocation.isdigit():
            #print("DigitLocation:",i,FileNameString[0:i],FileNameString)
            Initals=FileNameString[0:i]
            break
    return Initals

#Works out the totals for scordcard
def SetScoreCardTotals():
    #User a function to sum up the totals. 
    #define some numbers varibles and set to zero.
    TPar = TStroke_Index = TGross_Score = TPoints = TPutts = TFairways = TFerrets = TGreen_Regulations =0
    #Lop throughthe values for each value
    for enum,Record in enumerate(PlayerScoreCard['ScoreCard']['Holes']):
        if enum !=0 : #totals should be included in count
            TPar += int(Record["Par"])
            TStroke_Index += int(Record["StokeIndex"])
            TGross_Score += int(Record["GrossScore"])
            TPoints += int(Record["Points"])
            TPutts += int(Record["Putts"])
            TFairways += int(Record["FairwayHit"])
            TFerrets += int(Record["Ferrets"])
            if Record["GreensInRegulation"] != "0":
                TGreen_Regulations += 1
    PlayerScoreCard ["ScoreCard"]["Holes"][0]["HoleNumber"]=''
    #PlayerScoreCard ["ScoreCard"]["Holes"][0]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][0]["Par"]=TPar
    PlayerScoreCard["ScoreCard"]["Holes"][0]["StokeIndex"]=TStroke_Index
    PlayerScoreCard["ScoreCard"]["Holes"][0]["GrossScore"]=TGross_Score
    PlayerScoreCard["ScoreCard"]["Holes"][0]["Points"]=TPoints
    PlayerScoreCard["ScoreCard"]["Holes"][0]["Putts"]=TPutts
    PlayerScoreCard["ScoreCard"]["Holes"][0]["FairwayHit"]=TFairways
    PlayerScoreCard["ScoreCard"]["Holes"][0]["Ferrets"]=str(TFerrets)
    PlayerScoreCard["ScoreCard"]["Holes"][0]["GreensInRegulation"]=TGreen_Regulations
    return

#pm& am were added to orianl file name to inticate second game of the day
def GamesInDay(FileNameStr):
    TimeOfPlay =0
    PM=FileNameStr[:-4]
    if(PM[-2:]=='pm'):
        TimeOfPlay = 2
    elif(PM[-2:]=='m2'):
        TimeOfPlay = 3
    else:
        TimeOfPlay = 1
    
    return TimeOfPlay

#Move converted out out to another directory so to help keep track
def Converted(FileName):
    source_file = RootFolder+'/'+FileName
    desination_file = RootFolder+'/Converted/'+FileName
    os.rename(source_file,desination_file)
    return

# define functions for use else where Not sure still needed!!
def listsum(numList):
	theSum = 0
	for i in numList:
		try:
			int_value = int(i)
		except ValueError:
			pass
		else:
			theSum = theSum + i
	return theSum

#Reads in htlm file and reduces it to just the lines needed 
def ReadInDataFile(HTMLFile):
    # File to be loaded.
    f=""
    CleanList=[]
    # String to match in file.
    body_str = "<!--START OF OUTPUT FROM EXCEL PUBLISH AS WEB PAGE WIZARD"
    td_Tag = '<td'
    td_Tagend = '</td>'
    div_Tag ='<div'
    #Counter in files for line with above string to match
    Marker =0
    ReadFile=RootFolder+'/'+HTMLFile
    with open(ReadFile, 'r') as infile:
		FileInMemory = infile.read()  # Read the contents of the file into memory.
    infile.close()
    # Return a list of the lines, breaking at line boundaries.
    ReduceList=FileInMemory.splitlines()
    # loop to find start of HTLM in file and end of classes
    for i,line in enumerate(ReduceList):
        if body_str in line:
            Marker=i
    #Remove any lines which begin with <col from data 
    #Toggle variable for when end tag no on same line
    Toggle_tag=0
    Toggle_td_tag =0 
    for GoodLine in ReduceList[Marker:]:
        if td_Tag  in GoodLine:
            CleanList.append(GoodLine)
            Toggle_td_tag =1
        if Toggle_tag == 1 and Toggle_td_tag ==1:
            CleanList.append(GoodLine)
            Toggle_tag =0
            Toggle_td_tag =0
        if td_Tagend not in GoodLine and Toggle_td_tag ==1:
            Toggle_tag =1
        if div_Tag in GoodLine:
            CleanList.append(GoodLine)
     #Only return the data from the HTLM and not the classes and CSS details.
    return CleanList

#To find in str contains a number value
def ActualHandicap(HTMLHandicapStr):
    ValidationString = 'x:num"'
    EndString ='">'
    Handicap=0
    if ValidationString in HTMLHandicapStr:
        Start=HTMLHandicapStr.index(ValidationString)+len(ValidationString)
        End=HTMLHandicapStr.index('EndString',Start)
        #start = s.index( first ) + len( first )
        #end = s.index( last, start )
        #return s[start:end]
        Handicap= HTMLHandicapStr[Start:End]
    else:
       Handicap= RemoveData(HTMLHandicapStr)
    return(Handicap)

# Take the data from the HTML format and populate a JSON object 
def PopulateScoreCard(my_list,FileName):
    season=''
    OffSet=0
    #my_list=ReadInDataFile(RootFolder+'/'+ConvertFileName)
    PlayerScoreCard["Event"]["EventUUID"] =uuid.uuid4().hex             #Universally unique identifier for the Event should be the same for each player that played event 
    Season =my_list[0]
    PlayerScoreCard["Event"]["Season"] = Season[Season.find('id="')+4:Season.find('" ')]
    PlayerScoreCard["Event"]['DatePlayed'] = RemoveData(my_list[14+OffSet])
    PlayerScoreCard["Event"]['MajorEventName'] = RemoveData(my_list[21+OffSet])
    PlayerScoreCard["Event"]['EventStanding'] =RemoveData(my_list[20+OffSet])
    PlayerScoreCard["Event"]['PrizeFund'] = RemoveData(my_list[25+OffSet])
    PlayerScoreCard["Event"]["OrderOfTheDay"] = GamesInDay(FileName)
    #If filename has pm then game is second event of the day.
    #Creat the Player Details
    PlayerScoreCard["Player"]["PlayerUUID"] =uuid.uuid4().hex           #Universally unique identifier for the Player should be the same on each score card 
    PlayerScoreCard['Player']['PlayerName']=RemoveData(my_list[2+OffSet])
    Playing_Handicap =my_list[16+OffSet]
    PlayerScoreCard['Player']["PlayingHandicap"]=RemoveData(my_list[16+OffSet])
    PlayerScoreCard['Player']["BeforeHandicap"]=ActualHandicap(my_list[16+OffSet])
    PlayerScoreCard['Player']["AfterHandicap"] = 0
    #Create the Course Details for JSON record
    PlayerScoreCard["CourseDetails"]["CourseUUID"] =uuid.uuid4().hex    #Universally unique identifier for the Course each Tee and couse arrangement should have this the same 
    PlayerScoreCard['CourseDetails']['CourseName'] = RemoveData(my_list[7+OffSet])
    PlayerScoreCard['CourseDetails']['NumberOfFairways'] = RemoveData(my_list[12+OffSet])
    PlayerScoreCard['CourseDetails']['ParSS']=RemoveData(my_list[9+OffSet])
    #Pdate = Pdate[Pdate.find(startP)+1:Pdate.find(EndP)]
    #Pdate=RemoveData(Pdate)
    #Create the Proprties for JSON record
    PlayerScoreCard["Properties"]["ScoreCardUUID"] =uuid.uuid4().hex    #Universally unique identifier for the ScoreCard 
    PlayerScoreCard["Properties"]["FileName"]=FormatDate(PlayerScoreCard["Event"]['DatePlayed'])+'-'+PlayerScoreCard["Properties"]["ScoreCardUUID"]+'.json'
    PlayerScoreCard["Properties"]["OrginalFile"]=FileName
    PlayerScoreCard["Properties"]["FileInitals"]=PlayerInitals(FileName)
    
    #Create the ScoreCardStats for JSON record
    #PlayerScoreCard["ScoreCardStats"]["ScoreCardStats"]
    PlayerScoreCard["ScoreCardStats"]["HoleInOne"]=RemoveData(my_list[44+OffSet])
    #PlayerScoreCard["ScoreCardStats"]["Condor"]=RemoveData(H1)
    PlayerScoreCard["ScoreCardStats"]["Albatross"]=RemoveData(my_list[43+OffSet])
    PlayerScoreCard["ScoreCardStats"]["Eagle"]=RemoveData(my_list[42+OffSet])
    PlayerScoreCard["ScoreCardStats"]["Birdie"]=RemoveData(my_list[41+OffSet])
    PlayerScoreCard["ScoreCardStats"]["Par"]=RemoveData(my_list[40+OffSet])
    PlayerScoreCard["ScoreCardStats"]["Bogey"]=RemoveData(my_list[39+OffSet])
    PlayerScoreCard["ScoreCardStats"]["DoubleBogey"]=RemoveData(my_list[38+OffSet])
    PlayerScoreCard["ScoreCardStats"]["DoubleBogey+"]=RemoveData(my_list[37+OffSet])
    
    #Hole 1
    OffSet=0
    for linenum,line in enumerate(my_list):
        if 'Green Regulation' in line:
            OffSet=linenum+1
    
    for i in range(1,18,1):

        PlayerScoreCard["ScoreCard"]["Holes"][i]["Par"]=RemoveData(my_list[1+OffSet])
        PlayerScoreCard["ScoreCard"]["Holes"][i]["StokeIndex"]=RemoveData(my_list[2+OffSet])
        PlayerScoreCard["ScoreCard"]["Holes"][i]["GrossScore"]=RemoveData(my_list[3+OffSet])
        PlayerScoreCard["ScoreCard"]["Holes"][i]["Points"]=RemoveData(my_list[4+OffSet])
        PlayerScoreCard["ScoreCard"]["Holes"][i]["Putts"]=RemoveData(my_list[5+OffSet])
        PlayerScoreCard["ScoreCard"]["Holes"][i]["FairwayHit"]=RemoveData(my_list[6+OffSet])
        PlayerScoreCard["ScoreCard"]["Holes"][i]["Ferrets"]=RemoveData(my_list[7+OffSet])
        PlayerScoreCard["ScoreCard"]["Holes"][i]["GreensInRegulation"]=RemoveData(my_list[8+OffSet])
        OffSet+=10

    
        #Totals is createing the sum of the 18 holes 
        # # declare totals variables for each page. set counts to zero
    SetScoreCardTotals()
           # print(PlayerScoreCard["ScoreCard"]["Holes"][0])    
    return    

#function to write the scorecard out in HTML format.
def CreateHTMLOutput(JSONScoreCard):
    #Set local varibles
    ScoreCard =JSONScoreCard
    op_line =op_Last_Line=list()
    #print(ScoreCard) 

    # print( TPar,TStroke_Index,TGross_Score,TPoints,TPutts,TFairways,TFerrets)
    #write out new HTML file
    #NewHTMLFile = TargetHTMLFolder+'/'+ConvertFileName
    melbagefile = open(TargetHTMLFolder+'/'+PlayerScoreCard["Properties"]["OrginalFile"]+'l',"wb")

    melbagefile.write( '<html>');
    melbagefile.write( '<head>');
    melbagefile.write( '		<!-- Bring to you by http://www.CSSTableGenerator.com -->');
    melbagefile.write( '		<link rel="stylesheet" href="../../../../CSS/gamedata.css" type="text/css"/>	');
    melbagefile.write( '	</head>');
    melbagefile.write( ' <body>');
        
    melbagefile.write( '		<div class="GameData" style="width:600px;height:150px;">');
    melbagefile.write( '<br>');



    #Write out the header table of information
    melbagefile.write( "<table>");
    melbagefile.write( '<tr><td><h2>Player</h2></td><td><h2>Course</h2></td><td><h2>Date</h2></td><tr>');
    melbagefile.write( '<tr><td><h1>'+ScoreCard['Player']['PlayerName']+'</h1></td><td><h1>'+ScoreCard['CourseDetails']['CourseName']+'</h1></td><td><h1>'+ScoreCard["Event"]['DatePlayed']+'</h1></td><tr>');
    melbagefile.write( '<tr><td>'+'Playing Handicap <h1>'+str(ScoreCard['Player']['BeforeHandicap'])+'</h1></td><td>'+'Par/SS <h1>'+str(ScoreCard['CourseDetails']['ParSS'])+'</h1></td><td>'+'Events Place <h1>'+str(ScoreCard["Event"]['EventStanding'])+" "+str(ScoreCard["Event"]['MajorEventName'])+'</h1></td><tr>');
    melbagefile.write( '<tr><td>'+'Actual Handicap <h1>'+str(ScoreCard['Player']["AfterHandicap"])+'</h></td><td>''Number of Fairway <h1>'+str(ScoreCard['CourseDetails']['NumberOfFairways'])+'</h1></td><td> Prize Money <h1> &pound '+str(ScoreCard["Event"]['PrizeFund'])+'</h1></td><tr>');
    melbagefile.write( '</table>');

    melbagefile.write( '<br>');
    melbagefile.write( '<br>');
    melbagefile.write( '<table>');

    Tab='</td><td>'
    MarkUpOdd ='<tr class ="odd">'
    MarkUpEven = '<tr class ="even">'
    start ='<tr>'
    melbagefile.write( "<table>");
    for enum,Record in enumerate(ScoreCard['ScoreCard']['Holes']):
        if enum ==0:
            op_line ='<tr><td>'+"Hole"+Tab+"Par"+Tab+"Stroke Index"+Tab+"Gross Score"+Tab+"Points"+Tab+"Putts"+Tab+"Fairway"+Tab+"Ferrets"+Tab+"Greens in Regulation" +'</td><tr>';      #Header row
            op_Last_Line = MarkUpOdd+'<td>'+str(Record["HoleNumber"])+Tab+str(Record["Par"])+Tab+str(Record["StokeIndex"])+Tab+str(Record["GrossScore"])+Tab+str(Record["Points"])+Tab+str(Record["Putts"])+Tab+str(Record["FairwayHit"])+Tab+str(Record["Ferrets"])+Tab+str(Record["GreensInRegulation"])+'</td><tr>';
        elif enum % 2 ==0:
            start = MarkUpEven
            op_line = start+'<td>'+str(Record["HoleNumber"])+Tab+str(Record["Par"])+Tab+str(Record["StokeIndex"])+Tab+str(Record["GrossScore"])+Tab+str(Record["Points"])+Tab+str(Record["Putts"])+Tab+str(Record["FairwayHit"])+Tab+str(Record["Ferrets"])+Tab+str(Record["GreensInRegulation"])+'</td><tr>';
        elif enum % 2 >0:
            start = MarkUpOdd
            op_line = start+'<td>'+str(Record["HoleNumber"])+Tab+str(Record["Par"])+Tab+str(Record["StokeIndex"])+Tab+str(Record["GrossScore"])+Tab+str(Record["Points"])+Tab+str(Record["Putts"])+Tab+str(Record["FairwayHit"])+Tab+str(Record["Ferrets"])+Tab+str(Record["GreensInRegulation"])+'</td><tr>';
        melbagefile.write( op_line);
    
    melbagefile.write( op_Last_Line);
    melbagefile.write( '</table>');
    melbagefile.write( '<br>');
    melbagefile.write( '<br>');

    # Write out the Stats out in a table of the bottom
    melbagefile.write( "<table>");
    melbagefile.write( '<tr><td>Double\n Bogey Plus</td><td>Double\n Bogey</td><td>Bogey</td><td>Par</td><td>Birdie</td><td>Eagle</td><td>Albatross</td><td>Condor</td><td>Hole in \nOne</td><tr>');
    melbagefile.write( '<tr><td>'+str(ScoreCard["ScoreCardStats"]["DoubleBogey+"])+'</td><td>'+str(ScoreCard["ScoreCardStats"]["DoubleBogey"])+'</td><td>'+str(ScoreCard["ScoreCardStats"]["Bogey"])+'</td><td>'+str(ScoreCard["ScoreCardStats"]["Par"])+'</td><td>'+str(ScoreCard["ScoreCardStats"]["Birdie"])+'</td><td>'+str(ScoreCard["ScoreCardStats"]["Eagle"])+'</td><td>'+str(ScoreCard["ScoreCardStats"]["Albatross"])+'</td><td>0</td><td>'+str(ScoreCard["ScoreCardStats"]["HoleInOne"])+'</td><tr>');
    melbagefile.write( '</table>');
    melbagefile.write( '</div>');
    melbagefile.write( '<br>');
    melbagefile.write( '	</body>');
    melbagefile.write( '</html>');

    melbagefile.close()
    return

#Function to wrie out score car as JSON file
def CreatJSONOutput(JSONScoreCard):
    with open(TargetJSONFolder+'/'+JSONScoreCard["Properties"]["FileName"],'w') as f:
        json.dump(JSONScoreCard ,f,indent=4, sort_keys=True)  
        f.close()  
    return
        #Move file to converted folder

#Fundtion to log error messages
def LogErr(File,ErrMsg):
    print('Error is: ',File,'-msg: ',ErrMsg)
    with open(TargetJSONFolder+'/Errorlog.log','a') as f:
        f.write(File)
        f.write(" Error -")
        f.write(ErrMsg)
        f.write(" \n")
        f.close()
    return
#Start the coding from here

#write file which have passed for failed.
def FileTracker(File,Status,Message):
    with open('FileTracker.csv','a') as FT:
        FT.write(File+','+Status+','+Message)
    FT.close()
    return

#Set up global varibiles
global PlayerScoreCard
global ConvertFileName
ConvertFileName=''
global OffSet
#Used to adjust the reading RAW data file.
OffSet = 0

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

#Create a list of files to convert
FileList= FindFile2Convert(F224Folder)
SuccessFlag=0
#Loop all files. 
for File in FileList:
    #create Playerscorecard object ready to populate with data.
    print('Starting: ',File)
    PlayerScoreCard=ReadJSONSchema() 
    FileData=ReadInDataFile(File)
    try:
        PopulateScoreCard(FileData,File)
    except ValueError as err:
        LogErr(File,err.message)
        SuccessFlag=1



    CreateHTMLOutput(PlayerScoreCard)
    CreatJSONOutput(PlayerScoreCard)
    Converted(File)
    print('completed: ',File)
    if SuccessFlag==0:
        success="\n mv "+File+" "+File+".old"
        LogErr(File,success)
    elif SuccessFlag == 1:
        SuccessFlag=0
    
    #print ("mv "+File+" "+File+".old")



