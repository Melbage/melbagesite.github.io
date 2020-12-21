import sys
import  os
import json
import uuid
from datetime import datetime

#Create a list of HTML files to be converted. 
def FindFile2Convert(SrcFolder):
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
    td_Tag = "<td"
    div_Tag ="<div"
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
    for GoodLine in ReduceList[Marker:]:
        if td_Tag  in GoodLine:
            CleanList.append(GoodLine)
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
    #my_list=ReadInDataFile(RootFolder+'/'+ConvertFileName)
    PlayerScoreCard["Event"]["EventUUID"] =uuid.uuid4().hex             #Universally unique identifier for the Event should be the same for each player that played event 
    Season =my_list[3]
    PlayerScoreCard["Event"]["Season"] = Season[Season.find('id="')+4:Season.find('" ')]
    PlayerScoreCard["Event"]['DatePlayed'] = RemoveData(my_list[26])
    PlayerScoreCard["Event"]['MajorEventName'] = RemoveData(my_list[34])
    PlayerScoreCard["Event"]['EventStanding'] =RemoveData(my_list[33])
    PlayerScoreCard["Event"]['PrizeFund'] = RemoveData(my_list[37])
    PlayerScoreCard["Event"]["OrderOfTheDay"] = GamesInDay(FileName)
    #If filename has pm then game is second event of the day.
    #Creat the Player Details
    PlayerScoreCard["Player"]["PlayerUUID"] =uuid.uuid4().hex           #Universally unique identifier for the Player should be the same on each score card 
    PlayerScoreCard['Player']['PlayerName']=RemoveData(my_list[10])
    Playing_Handicap =my_list[28]
    PlayerScoreCard['Player']["PlayingHandicap"]=RemoveData(my_list[28])
    PlayerScoreCard['Player']["BeforeHandicap"]=ActualHandicap(my_list[28])
    PlayerScoreCard['Player']["AfterHandicap"] = 0
    #Create the Course Details for JSON record
    PlayerScoreCard["CourseDetails"]["CourseUUID"] =uuid.uuid4().hex    #Universally unique identifier for the Course each Tee and couse arrangement should have this the same 
    PlayerScoreCard['CourseDetails']['CourseName'] = RemoveData(my_list[16])
    PlayerScoreCard['CourseDetails']['NumberOfFairways'] = RemoveData(my_list[22])
    PlayerScoreCard['CourseDetails']['ParSS']=RemoveData(my_list[20])
    #Pdate = Pdate[Pdate.find(startP)+1:Pdate.find(EndP)]
    #Pdate=RemoveData(Pdate)
    #Create the Proprties for JSON record
    PlayerScoreCard["Properties"]["ScoreCardUUID"] =uuid.uuid4().hex    #Universally unique identifier for the ScoreCard 
    PlayerScoreCard["Properties"]["FileName"]=FormatDate(PlayerScoreCard["Event"]['DatePlayed'])+'-'+PlayerScoreCard["Properties"]["ScoreCardUUID"]+'.json'
    PlayerScoreCard["Properties"]["OrginalFile"]=FileName
    PlayerScoreCard["Properties"]["FileInitals"]=PlayerInitals(FileName)
    
    #Create the ScoreCardStats for JSON record
    #PlayerScoreCard["ScoreCardStats"]["ScoreCardStats"]
    PlayerScoreCard["ScoreCardStats"]["HoleInOne"]=RemoveData(my_list[59])
    #PlayerScoreCard["ScoreCardStats"]["Condor"]=RemoveData(H1)
    PlayerScoreCard["ScoreCardStats"]["Albatross"]=RemoveData(my_list[58])
    PlayerScoreCard["ScoreCardStats"]["Eagle"]=RemoveData(my_list[57])
    PlayerScoreCard["ScoreCardStats"]["Birdie"]=RemoveData(my_list[56])
    PlayerScoreCard["ScoreCardStats"]["Par"]=RemoveData(my_list[55])
    PlayerScoreCard["ScoreCardStats"]["Bogey"]=RemoveData(my_list[54])
    PlayerScoreCard["ScoreCardStats"]["DoubleBogey"]=RemoveData(my_list[53])
    PlayerScoreCard["ScoreCardStats"]["DoubleBogey+"]=RemoveData(my_list[52])
    
    #Hole 1
    #PlayerScoreCard ["ScoreCard"]["Holes"][1]["HoleNumber"]=RemoveData(my_list[76])
    #PlayerScoreCard ["ScoreCard"]["Holes"][1]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][1]["Par"]=RemoveData(my_list[77])
    PlayerScoreCard["ScoreCard"]["Holes"][1]["StokeIndex"]=RemoveData(my_list[78])
    PlayerScoreCard["ScoreCard"]["Holes"][1]["GrossScore"]=RemoveData(my_list[79])
    PlayerScoreCard["ScoreCard"]["Holes"][1]["Points"]=RemoveData(my_list[80])
    PlayerScoreCard["ScoreCard"]["Holes"][1]["Putts"]=RemoveData(my_list[81])
    PlayerScoreCard["ScoreCard"]["Holes"][1]["FairwayHit"]=RemoveData(my_list[82])
    PlayerScoreCard["ScoreCard"]["Holes"][1]["Ferrets"]=RemoveData(my_list[83])
    PlayerScoreCard["ScoreCard"]["Holes"][1]["GreensInRegulation"]=RemoveData(my_list[84])
    #PlayerScoreCard ["ScoreCard"]["Holes"][1]["HandicapStokes"]=RemoveData()
    #Hole2
    #PlayerScoreCard ["ScoreCard"]["Holes"][2]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][2]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][2]["Par"]=RemoveData(my_list[88])
    PlayerScoreCard["ScoreCard"]["Holes"][2]["StokeIndex"]=RemoveData(my_list[89])
    PlayerScoreCard["ScoreCard"]["Holes"][2]["GrossScore"]=RemoveData(my_list[90])
    PlayerScoreCard["ScoreCard"]["Holes"][2]["Points"]=RemoveData(my_list[91])
    PlayerScoreCard["ScoreCard"]["Holes"][2]["Putts"]=RemoveData(my_list[92])
    PlayerScoreCard["ScoreCard"]["Holes"][2]["FairwayHit"]=RemoveData(my_list[93])
    PlayerScoreCard["ScoreCard"]["Holes"][2]["Ferrets"]=RemoveData(my_list[94])
    PlayerScoreCard["ScoreCard"]["Holes"][2]["GreensInRegulation"]=RemoveData(my_list[95])
    #PlayerScoreCard ["ScoreCard"]["Holes"][12]["HandicapStokes"]=RemoveData()
    #Hole 3
    #PlayerScoreCard ["ScoreCard"]["Holes"][3]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][3]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][3]["Par"]=RemoveData(my_list[99])
    PlayerScoreCard["ScoreCard"]["Holes"][3]["StokeIndex"]=RemoveData(my_list[100])
    PlayerScoreCard["ScoreCard"]["Holes"][3]["GrossScore"]=RemoveData(my_list[101])
    PlayerScoreCard["ScoreCard"]["Holes"][3]["Points"]=RemoveData(my_list[102])
    PlayerScoreCard["ScoreCard"]["Holes"][3]["Putts"]=RemoveData(my_list[103])
    PlayerScoreCard["ScoreCard"]["Holes"][3]["FairwayHit"]=RemoveData(my_list[104])
    PlayerScoreCard["ScoreCard"]["Holes"][3]["Ferrets"]=RemoveData(my_list[105])
    PlayerScoreCard["ScoreCard"]["Holes"][3]["GreensInRegulation"]=RemoveData(my_list[106])
    #PlayerScoreCard ["ScoreCard"]["Holes"][3]["HandicapStokes"]=RemoveData()
    #Hole 4
    #PlayerScoreCard ["ScoreCard"]["Holes"][4]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][4]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][4]["Par"]=RemoveData(my_list[110])
    PlayerScoreCard["ScoreCard"]["Holes"][4]["StokeIndex"]=RemoveData(my_list[111])
    PlayerScoreCard["ScoreCard"]["Holes"][4]["GrossScore"]=RemoveData(my_list[112])
    PlayerScoreCard["ScoreCard"]["Holes"][4]["Points"]=RemoveData(my_list[113])
    PlayerScoreCard["ScoreCard"]["Holes"][4]["Putts"]=RemoveData(my_list[114])
    PlayerScoreCard["ScoreCard"]["Holes"][4]["FairwayHit"]=RemoveData(my_list[115])
    PlayerScoreCard["ScoreCard"]["Holes"][4]["Ferrets"]=RemoveData(my_list[116])
    PlayerScoreCard["ScoreCard"]["Holes"][4]["GreensInRegulation"]=RemoveData(my_list[117])
    #PlayerScoreCard ["ScoreCard"]["Holes"][4]["HandicapStokes"]=RemoveData()
    #Hole 5
    #PlayerScoreCard ["ScoreCard"]["Holes"][5]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][5]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][5]["Par"]=RemoveData(my_list[121])
    PlayerScoreCard["ScoreCard"]["Holes"][5]["StokeIndex"]=RemoveData(my_list[122])
    PlayerScoreCard["ScoreCard"]["Holes"][5]["GrossScore"]=RemoveData(my_list[123])
    PlayerScoreCard["ScoreCard"]["Holes"][5]["Points"]=RemoveData(my_list[124])
    PlayerScoreCard["ScoreCard"]["Holes"][5]["Putts"]=RemoveData(my_list[125])
    PlayerScoreCard["ScoreCard"]["Holes"][5]["FairwayHit"]=RemoveData(my_list[126])
    PlayerScoreCard["ScoreCard"]["Holes"][5]["Ferrets"]=RemoveData(my_list[127])
    PlayerScoreCard["ScoreCard"]["Holes"][5]["GreensInRegulation"]=RemoveData(my_list[128])
    #PlayerScoreCard ["ScoreCard"]["Holes"][5]["HandicapStokes"]=RemoveData()
    #Hole 6
    #PlayerScoreCard ["ScoreCard"]["Holes"][6]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][6]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][6]["Par"]=RemoveData(my_list[132])
    PlayerScoreCard["ScoreCard"]["Holes"][6]["StokeIndex"]=RemoveData(my_list[133])
    PlayerScoreCard["ScoreCard"]["Holes"][6]["GrossScore"]=RemoveData(my_list[134])
    PlayerScoreCard["ScoreCard"]["Holes"][6]["Points"]=RemoveData(my_list[135])
    PlayerScoreCard["ScoreCard"]["Holes"][6]["Putts"]=RemoveData(my_list[136])
    PlayerScoreCard["ScoreCard"]["Holes"][6]["FairwayHit"]=RemoveData(my_list[137])
    PlayerScoreCard["ScoreCard"]["Holes"][6]["Ferrets"]=RemoveData(my_list[138])
    PlayerScoreCard["ScoreCard"]["Holes"][6]["GreensInRegulation"]=RemoveData(my_list[139])
    #PlayerScoreCard ["ScoreCard"]["Holes"][6]["HandicapStokes"]=RemoveData()
    #Hole 7
    #PlayerScoreCard ["ScoreCard"]["Holes"][7]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][7]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][7]["Par"]=RemoveData(my_list[143])
    PlayerScoreCard["ScoreCard"]["Holes"][7]["StokeIndex"]=RemoveData(my_list[144])
    PlayerScoreCard["ScoreCard"]["Holes"][7]["GrossScore"]=RemoveData(my_list[145])
    PlayerScoreCard["ScoreCard"]["Holes"][7]["Points"]=RemoveData(my_list[146])
    PlayerScoreCard["ScoreCard"]["Holes"][7]["Putts"]=RemoveData(my_list[147])
    PlayerScoreCard["ScoreCard"]["Holes"][7]["FairwayHit"]=RemoveData(my_list[148])
    PlayerScoreCard["ScoreCard"]["Holes"][7]["Ferrets"]=RemoveData(my_list[149])
    PlayerScoreCard["ScoreCard"]["Holes"][7]["GreensInRegulation"]=RemoveData(my_list[150])
    #PlayerScoreCard ["ScoreCard"]["Holes"][7]["HandicapStokes"]=RemoveData()
    #Hole 8
    #PlayerScoreCard ["ScoreCard"]["Holes"][8]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][8]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][8]["Par"]=RemoveData(my_list[154])
    PlayerScoreCard["ScoreCard"]["Holes"][8]["StokeIndex"]=RemoveData(my_list[155])
    PlayerScoreCard["ScoreCard"]["Holes"][8]["GrossScore"]=RemoveData(my_list[156])
    PlayerScoreCard["ScoreCard"]["Holes"][8]["Points"]=RemoveData(my_list[157])
    PlayerScoreCard["ScoreCard"]["Holes"][8]["Putts"]=RemoveData(my_list[158])
    PlayerScoreCard["ScoreCard"]["Holes"][8]["FairwayHit"]=RemoveData(my_list[159])
    PlayerScoreCard["ScoreCard"]["Holes"][8]["Ferrets"]=RemoveData(my_list[160])
    PlayerScoreCard["ScoreCard"]["Holes"][8]["GreensInRegulation"]=RemoveData(my_list[161])
    #PlayerScoreCard ["ScoreCard"]["Holes"][8]["HandicapStokes"]=RemoveData()
    #Hole 9
    #PlayerScoreCard ["ScoreCard"]["Holes"][9]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][9]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][9]["Par"]=RemoveData(my_list[165])
    PlayerScoreCard["ScoreCard"]["Holes"][9]["StokeIndex"]=RemoveData(my_list[166])
    PlayerScoreCard["ScoreCard"]["Holes"][9]["GrossScore"]=RemoveData(my_list[167])
    PlayerScoreCard["ScoreCard"]["Holes"][9]["Points"]=RemoveData(my_list[168])
    PlayerScoreCard["ScoreCard"]["Holes"][9]["Putts"]=RemoveData(my_list[169])
    PlayerScoreCard["ScoreCard"]["Holes"][9]["FairwayHit"]=RemoveData(my_list[170])
    PlayerScoreCard["ScoreCard"]["Holes"][9]["Ferrets"]=RemoveData(my_list[171])
    PlayerScoreCard["ScoreCard"]["Holes"][9]["GreensInRegulation"]=RemoveData(my_list[172])
    #PlayerScoreCard ["ScoreCard"]["Holes"][9]["HandicapStokes"]=RemoveData()
    #Hole 10
    #PlayerScoreCard ["ScoreCard"]["Holes"][10]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][10]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][10]["Par"]=RemoveData(my_list[176])
    PlayerScoreCard["ScoreCard"]["Holes"][10]["StokeIndex"]=RemoveData(my_list[177])
    PlayerScoreCard["ScoreCard"]["Holes"][10]["GrossScore"]=RemoveData(my_list[178])
    PlayerScoreCard["ScoreCard"]["Holes"][10]["Points"]=RemoveData(my_list[179])
    PlayerScoreCard["ScoreCard"]["Holes"][10]["Putts"]=RemoveData(my_list[180])
    PlayerScoreCard["ScoreCard"]["Holes"][10]["FairwayHit"]=RemoveData(my_list[181])
    PlayerScoreCard["ScoreCard"]["Holes"][10]["Ferrets"]=RemoveData(my_list[182])
    PlayerScoreCard["ScoreCard"]["Holes"][10]["GreensInRegulation"]=RemoveData(my_list[183])
    #PlayerScoreCard ["ScoreCard"]["Holes"][10]["HandicapStokes"]=RemoveData()
    #Hole 11
    #PlayerScoreCard ["ScoreCard"]["Holes"][11]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][11]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][11]["Par"]=RemoveData(my_list[187])
    PlayerScoreCard["ScoreCard"]["Holes"][11]["StokeIndex"]=RemoveData(my_list[188])
    PlayerScoreCard["ScoreCard"]["Holes"][11]["GrossScore"]=RemoveData(my_list[189])
    PlayerScoreCard["ScoreCard"]["Holes"][11]["Points"]=RemoveData(my_list[190])
    PlayerScoreCard["ScoreCard"]["Holes"][11]["Putts"]=RemoveData(my_list[191])
    PlayerScoreCard["ScoreCard"]["Holes"][11]["FairwayHit"]=RemoveData(my_list[192])
    PlayerScoreCard["ScoreCard"]["Holes"][11]["Ferrets"]=RemoveData(my_list[193])
    PlayerScoreCard["ScoreCard"]["Holes"][11]["GreensInRegulation"]=RemoveData(my_list[194])
    #PlayerScoreCard ["ScoreCard"]["Holes"][11]["HandicapStokes"]=RemoveData()
    #Hole 12
    #PlayerScoreCard ["ScoreCard"]["Holes"][12]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][12]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][12]["Par"]=RemoveData(my_list[198])
    PlayerScoreCard["ScoreCard"]["Holes"][12]["StokeIndex"]=RemoveData(my_list[199])
    PlayerScoreCard["ScoreCard"]["Holes"][12]["GrossScore"]=RemoveData(my_list[200])
    PlayerScoreCard["ScoreCard"]["Holes"][12]["Points"]=RemoveData(my_list[201])
    PlayerScoreCard["ScoreCard"]["Holes"][12]["Putts"]=RemoveData(my_list[202])
    PlayerScoreCard["ScoreCard"]["Holes"][12]["FairwayHit"]=RemoveData(my_list[203])
    PlayerScoreCard["ScoreCard"]["Holes"][12]["Ferrets"]=RemoveData(my_list[204])
    PlayerScoreCard["ScoreCard"]["Holes"][12]["GreensInRegulation"]=RemoveData(my_list[205])
    #PlayerScoreCard ["ScoreCard"]["Holes"][12]["HandicapStokes"]=RemoveData()
    #Hole 13
    #PlayerScoreCard ["ScoreCard"]["Holes"][13]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][13]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][13]["Par"]=RemoveData(my_list[209])
    PlayerScoreCard["ScoreCard"]["Holes"][13]["StokeIndex"]=RemoveData(my_list[210])
    PlayerScoreCard["ScoreCard"]["Holes"][13]["GrossScore"]=RemoveData(my_list[211])
    PlayerScoreCard["ScoreCard"]["Holes"][13]["Points"]=RemoveData(my_list[212])
    PlayerScoreCard["ScoreCard"]["Holes"][13]["Putts"]=RemoveData(my_list[213])
    PlayerScoreCard["ScoreCard"]["Holes"][13]["FairwayHit"]=RemoveData(my_list[214])
    PlayerScoreCard["ScoreCard"]["Holes"][13]["Ferrets"]=RemoveData(my_list[215])
    PlayerScoreCard["ScoreCard"]["Holes"][13]["GreensInRegulation"]=RemoveData(my_list[216])
    #PlayerScoreCard ["ScoreCard"]["Holes"][13]["HandicapStokes"]=RemoveData()
    #Hole 14
    #PlayerScoreCard ["ScoreCard"]["Holes"][14]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][14]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][14]["Par"]=RemoveData(my_list[220])
    PlayerScoreCard["ScoreCard"]["Holes"][14]["StokeIndex"]=RemoveData(my_list[221])
    PlayerScoreCard["ScoreCard"]["Holes"][14]["GrossScore"]=RemoveData(my_list[222])
    PlayerScoreCard["ScoreCard"]["Holes"][14]["Points"]=RemoveData(my_list[223])
    PlayerScoreCard["ScoreCard"]["Holes"][14]["Putts"]=RemoveData(my_list[224])
    PlayerScoreCard["ScoreCard"]["Holes"][14]["FairwayHit"]=RemoveData(my_list[225])
    PlayerScoreCard["ScoreCard"]["Holes"][14]["Ferrets"]=RemoveData(my_list[226])
    PlayerScoreCard["ScoreCard"]["Holes"][14]["GreensInRegulation"]=RemoveData(my_list[227])
    #PlayerScoreCard ["ScoreCard"]["Holes"][14]["HandicapStokes"]=RemoveData()
    #Hole 15
    #PlayerScoreCard ["ScoreCard"]["Holes"][15]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][15]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][15]["Par"]=RemoveData(my_list[231])
    PlayerScoreCard["ScoreCard"]["Holes"][15]["StokeIndex"]=RemoveData(my_list[232])
    PlayerScoreCard["ScoreCard"]["Holes"][15]["GrossScore"]=RemoveData(my_list[233])
    PlayerScoreCard["ScoreCard"]["Holes"][15]["Points"]=RemoveData(my_list[234])
    PlayerScoreCard["ScoreCard"]["Holes"][15]["Putts"]=RemoveData(my_list[235])
    PlayerScoreCard["ScoreCard"]["Holes"][15]["FairwayHit"]=RemoveData(my_list[236])
    PlayerScoreCard["ScoreCard"]["Holes"][15]["Ferrets"]=RemoveData(my_list[237])
    PlayerScoreCard["ScoreCard"]["Holes"][15]["GreensInRegulation"]=RemoveData(my_list[238])
    #PlayerScoreCard ["ScoreCard"]["Holes"][15]["HandicapStokes"]=RemoveData()
    #Hole 16
    #PlayerScoreCard ["ScoreCard"]["Holes"][16]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][16]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][16]["Par"]=RemoveData(my_list[242])
    PlayerScoreCard["ScoreCard"]["Holes"][16]["StokeIndex"]=RemoveData(my_list[243])
    PlayerScoreCard["ScoreCard"]["Holes"][16]["GrossScore"]=RemoveData(my_list[244])
    PlayerScoreCard["ScoreCard"]["Holes"][16]["Points"]=RemoveData(my_list[245])
    PlayerScoreCard["ScoreCard"]["Holes"][16]["Putts"]=RemoveData(my_list[246])
    PlayerScoreCard["ScoreCard"]["Holes"][16]["FairwayHit"]=RemoveData(my_list[247])
    PlayerScoreCard["ScoreCard"]["Holes"][16]["Ferrets"]=RemoveData(my_list[248])
    PlayerScoreCard["ScoreCard"]["Holes"][16]["GreensInRegulation"]=RemoveData(my_list[249])
    #PlayerScoreCard ["ScoreCard"]["Holes"][16]["HandicapStokes"]=RemoveData()
    #Hole 17
    #PlayerScoreCard ["ScoreCard"]["Holes"][17]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][17]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][17]["Par"]=RemoveData(my_list[253])
    PlayerScoreCard["ScoreCard"]["Holes"][17]["StokeIndex"]=RemoveData(my_list[254])
    PlayerScoreCard["ScoreCard"]["Holes"][17]["GrossScore"]=RemoveData(my_list[255])
    PlayerScoreCard["ScoreCard"]["Holes"][17]["Points"]=RemoveData(my_list[256])
    PlayerScoreCard["ScoreCard"]["Holes"][17]["Putts"]=RemoveData(my_list[257])
    PlayerScoreCard["ScoreCard"]["Holes"][17]["FairwayHit"]=RemoveData(my_list[258])
    PlayerScoreCard["ScoreCard"]["Holes"][17]["Ferrets"]=RemoveData(my_list[259])
    PlayerScoreCard["ScoreCard"]["Holes"][17]["GreensInRegulation"]=RemoveData(my_list[260])
    #PlayerScoreCard ["ScoreCard"]["Holes"][17]["HandicapStokes"]=RemoveData()
    #Hole 18
    #PlayerScoreCard ["ScoreCard"]["Holes"][18]["HoleNumber"]=RemoveData()
    #PlayerScoreCard ["ScoreCard"]["Holes"][18]["Yardage"]=RemoveData()
    PlayerScoreCard["ScoreCard"]["Holes"][18]["Par"]=RemoveData(my_list[264])
    PlayerScoreCard["ScoreCard"]["Holes"][18]["StokeIndex"]=RemoveData(my_list[265])
    PlayerScoreCard["ScoreCard"]["Holes"][18]["GrossScore"]=RemoveData(my_list[266])
    PlayerScoreCard["ScoreCard"]["Holes"][18]["Points"]=RemoveData(my_list[267])
    PlayerScoreCard["ScoreCard"]["Holes"][18]["Putts"]=RemoveData(my_list[268])
    PlayerScoreCard["ScoreCard"]["Holes"][18]["FairwayHit"]=RemoveData(my_list[269])
    PlayerScoreCard["ScoreCard"]["Holes"][18]["Ferrets"]=RemoveData(my_list[270])
    PlayerScoreCard["ScoreCard"]["Holes"][18]["GreensInRegulation"]=RemoveData(my_list[271])
    #PlayerScoreCard ["ScoreCard"]["Holes"][18]["HandicapStokes"]=RemoveData()
        
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
    
#Start the coding from here

#Set up global varibiles
global PlayerScoreCard
global ConvertFileName
ConvertFileName=''
#Static Varibiles
global RootFolder 
global TargetJSONFolder
global TargetHTMLFolder 
#Set static Varibiles
RootFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_Games'
TargetJSONFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_JSON'
TargetHTMLFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_HTML'
#Following folder were found to have different lenght data files. so slip them into groups.
223Folder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/RAW/223'
224Folder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/RAW/224'
OtherFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/RAW/other'

#Create a list of files to convert
FileList= FindFile2Convert(223Folder)
#Loop all files. 
for File in FileList:
    #create Playerscorecard object ready to populate with data.
    PlayerScoreCard=ReadJSONSchema() 
    FileData=ReadInDataFile(File)
    PopulateScoreCard(FileData,File)
    CreateHTMLOutput(PlayerScoreCard)
    CreatJSONOutput(PlayerScoreCard)
    Converted(File)



# for file in FileList:
#     print(file)


#print("Filename",ConvertFileName)

#data=""

    #


   
    
            
           

    #Season =my_list[3]
            #Player =my_list[17]
            #Club =my_list[23]
            #Par_SS =my_list[27]
            #Num_Fairways =my_list[30]
            #Pdate =my_list[34]
            #Playing_Handicap =my_list[36]
            #Handicap =my_list[36]
            #Event_Place =my_list[41]
            #Major =my_list[42]
            #Prize_Money =my_list[46]
            #DB_Plus =my_list[61]
            #DB =my_list[62]
            #Bi =my_list[63]
            #P =my_list[64]
            #B =my_list[65]
            #E =my_list[66]
            #A =my_list[67]
            #H1 =my_list[68]
            #Hole1 =my_list[89]
            #Par1 =my_list[90]
            # Stroke_Index1 =my_list[91]
            # Gross_Score1 =my_list[92]
            # Points1 =my_list[93]
            # Putts1 =my_list[94]
            # Fairway1 =my_list[95]
            # Ferret1 =my_list[96]
            # Green_Regulation1 =my_list[97]
            # Hole2 =my_list[100]
            # Par2 =my_list[101]
            # Stroke_Index2 =my_list[102]
            # Gross_Score2 =my_list[103]
            # Points2 =my_list[104]
            # Putts2 =my_list[105]
            # Fairway2 =my_list[106]
            # Ferret2 =my_list[107]
            # Green_Regulation2 =my_list[108]
            # Hole3 =my_list[111]
            # Par3 =my_list[112]
            # Stroke_Index3 =my_list[113]
            # Gross_Score3 =my_list[114]
            # Points3 =my_list[115]
            # Putts3 =my_list[116]
            # Fairway3 =my_list[117]
            # Ferret3 =my_list[118]
            # Green_Regulation3 =my_list[119]
            # Hole4 =my_list[122]
            # Par4 =my_list[123]
            # Stroke_Index4 =my_list[124]
            # Gross_Score4 =my_list[125]
            # Points4 =my_list[126]
            # Putts4 =my_list[127]
            # Fairway4 =my_list[128]
            # Ferret4 =my_list[129]
            # Green_Regulation4 =my_list[130]
            # Hole5 =my_list[133]
            # Par5 =my_list[134]
            # Stroke_Index5 =my_list[135]
            # Gross_Score5 =my_list[136]
            # Points5 =my_list[137]
            # Putts5 =my_list[138]
            # Fairway5 =my_list[139]
            # Ferret5 =my_list[140]
            # Green_Regulation5 =my_list[141]
            # Hole6 =my_list[144]
            # Par6 =my_list[145]
            # Stroke_Index6 =my_list[146]
            # Gross_Score6 =my_list[147]
            # Points6 =my_list[148]
            # Putts6 =my_list[149]
            # Fairway6 =my_list[150]
            # Ferret6 =my_list[151]
            # Green_Regulation6 =my_list[152]
            # Hole7 =my_list[155]
            # Par7 =my_list[156]
            # Stroke_Index7 =my_list[157]
            # Gross_Score7 =my_list[158]
            # Points7 =my_list[159]
            # Putts7 =my_list[160]
            # Fairway7 =my_list[161]
            # Ferret7 =my_list[162]
            # Green_Regulation7 =my_list[163]
            # Hole8 =my_list[166]
            # Par8 =my_list[167]
            # Stroke_Index8 =my_list[168]
            # Gross_Score8 =my_list[169]
            # Points8 =my_list[170]
            # Putts8 =my_list[171]
            # Fairway8 =my_list[172]
            # Ferret8 =my_list[173]
            # Green_Regulation8 =my_list[174]
            # Hole9 =my_list[177]
            # Par9 =my_list[178]
            # Stroke_Index9 =my_list[179]
            # Gross_Score9 =my_list[180]
            # Points9 =my_list[181]
            # Putts9 =my_list[182]
            # Fairway9 =my_list[183]
            # Ferret9 =my_list[184]
            # Green_Regulation9 =my_list[185]
            # Hole10 =my_list[188]
            # Par10 =my_list[189]
            # Stroke_Index10 =my_list[190]
            # Gross_Score10 =my_list[191]
            # Points10 =my_list[192]
            # Putts10 =my_list[193]
            # Fairway10 =my_list[194]
            # Ferret10 =my_list[195]
            # Green_Regulation10 =my_list[196]
            # Hole11 =my_list[199]
            # Par11 =my_list[200]
            # Stroke_Index11 =my_list[201]
            # Gross_Score11 =my_list[202]
            # Points11 =my_list[203]
            # Putts11 =my_list[204]
            # Fairway11 =my_list[205]
            # Ferret11 =my_list[206]
            # Green_Regulation11 =my_list[207]
            # Hole12 =my_list[210]
            # Par12 =my_list[211]
            # Stroke_Index12 =my_list[212]
            # Gross_Score12 =my_list[213]
            # Points12 =my_list[214]
            # Putts12 =my_list[215]
            # Fairway12 =my_list[216]
            # Ferret12 =my_list[217]
            # Green_Regulation12 =my_list[218]
            # Hole13 =my_list[221]
            # Par13 =my_list[222]
            # Stroke_Index13 =my_list[223]
            # Gross_Score13 =my_list[224]
            # Points13 =my_list[225]
            # Putts13 =my_list[226]
            # Fairway13 =my_list[227]
            # Ferret13 =my_list[228]
            # Green_Regulation13 =my_list[229]
            # Hole14 =my_list[232]
            # Par14 =my_list[233]
            # Stroke_Index14 =my_list[234]
            # Gross_Score14 =my_list[235]
            # Points14 =my_list[236]
            # Putts14 =my_list[237]
            # Fairway14 =my_list[238]
            # Ferret14 =my_list[239]
            # Green_Regulation14 =my_list[240]
            # Hole15 =my_list[243]
            # Par15 =my_list[244]
            # Stroke_Index15 =my_list[245]
            # Gross_Score15 =my_list[246]
            # Points15 =my_list[247]
            # Putts15 =my_list[248]
            # Fairway15 =my_list[249]
            # Ferret15 =my_list[250]
            # Green_Regulation15 =my_list[251]
            # Hole16 =my_list[254]
            # Par16 =my_list[255]
            # Stroke_Index16 =my_list[256]
            # Gross_Score16 =my_list[257]
            # Points16 =my_list[258]
            # Putts16 =my_list[259]
            # Fairway16 =my_list[260]
            # Ferret16 =my_list[261]
            # Green_Regulation16 =my_list[262]
            # Hole17 =my_list[265]
            # Par17 =my_list[266]
            # Stroke_Index17 =my_list[267]
            # Gross_Score17 =my_list[268]
            # Points17 =my_list[269]
            # Putts17 =my_list[270]
            # Fairway17 =my_list[271]
            # Ferret17 =my_list[272]
            # Green_Regulation17 =my_list[273]
            # Hole18 =my_list[276]
            # Par18 =my_list[277]
            # Stroke_Index18 =my_list[278]
            # Gross_Score18 =my_list[279]
            # Points18 =my_list[280]
            # Putts18 =my_list[281]
            # Fairway18 =my_list[282]
            # Ferret18 =my_list[283]
            # Green_Regulation18 =my_list[284]
            
        # Removed unwanted parts of the String
        #Create the Events Details for JSON record
       # from_here_on_in = 0
# season ="season"
# player = "Player"
# course_name = "Course_name"
# Par_lable = "Parlab"
# Par = "Par"
# Fairway_lable = "Fairwaylab"
# Fairway_Count = "FairewaysCount"
# Date_lable = "Datelab"
# Played_Date = "Date"
# Handicap_Lable = "Handicaplab"
# Handicap = "Handicap"
# startP = ">"
# EndP = "</td>"
#Create scordcard for JSON record
        #0 in array is the Totals so hole numbers match array numbers
        # PlayerScoreCard ["ScoreCard"]["Holes"][0]["HoleNumber"]=RemoveData()
        # PlayerScoreCard ["ScoreCard"]["Holes"][0]["Yardage"]=RemoveData()
        # PlayerScoreCard ["ScoreCard"]["Holes"][0]["Par"]=RemoveData()
        # PlayerScoreCard ["ScoreCard"]["Holes"][0]["StokeIndex"]=RemoveData()
        # PlayerScoreCard ["ScoreCard"]["Holes"][0]["GrossScore"]=RemoveData()
        # PlayerScoreCard ["ScoreCard"]["Holes"][0]["Points"]=RemoveData()
        # PlayerScoreCard ["ScoreCard"]["Holes"][0]["Putts"]=RemoveData()
        # PlayerScoreCard ["ScoreCard"]["Holes"][0]["FairwayHit"]=RemoveData()
        # PlayerScoreCard ["ScoreCard"]["Holes"][0]["Ferrets"]=RemoveData()
        # PlayerScoreCard ["ScoreCard"]["Holes"][0]["GreensInRegulation"]=RemoveData()
        # PlayerScoreCard ["ScoreCard"]["Holes"][0]["HandicapStokes"]=RemoveData()