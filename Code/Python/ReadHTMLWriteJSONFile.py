import sys
import  os
import json
import uuid
from datetime import datetime

RootFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_Games'
TargetJSONFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_JSON'
TargetHTMLFolder = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/MGA_HTML'

#Rewrite to expect a file and file path to be passed to the program This means we expect the file to be passed 
def FindFile2Convert(SrcFolder):
    FolderList=[]
    for filename in os.listdir(SrcFolder):
        if filename.endswith(".htm"):
            FolderList.append(filename)
  
    return FolderList

def ReadJSONSchema():
    #Read JSON schema.
   with open('/Users/paulcarter/Documents/GITHUB/Melbage/Melbagesite/melbagesite.github.io/Code/JSON/Data/PlayersScoreCardTmplate.json') as Schema:
    SCasJSON= json.load(Schema)
    return SCasJSON

global PlayerScoreCard
PlayerScoreCard=ReadJSONSchema() 
#Assign all the GUID/UUID to JSON files.



def Remove_nbsp(nbsp):
        #Test to see if there is a non-breaking space and if so replace it with zero
    if(nbsp=='&nbsp;'): nbsp = '0'
    return nbsp

def RemoveData(LineOfData):
    #Function to remove the HTML from the data line and return just the data cleaned ready for assihgning to value
    #HTML data is held betwene the following tabs > and </td>
    BetweenThis = '>'
    BetweenThat = '</td>'
    CleanLineOfData = LineOfData[LineOfData.find(BetweenThis)+1:LineOfData.find(BetweenThat)]
    #Now Remove non-breaking space 
    CleanLineOfData = Remove_nbsp(CleanLineOfData)
    return CleanLineOfData.decode('utf-8', 'ignore')

def FormatDate(DateStringObject):
    DateObject = datetime.strptime(DateStringObject, '%d/%m/%y') #Covert date string to Dateformat eg 26/04/03
    DateStringObject = DateObject.strftime('%Y%m%d') #Convert Date object to required string format eg 20030426
    return DateStringObject

def PlayerInitals(FileNameString):
    #Find the place of the first digit in string
    #As the files have the initals as the first part of the name
     
    for i, DigitLocation in enumerate(FileNameString):
        if DigitLocation.isdigit():
            #print("DigitLocation:",i,FileNameString[0:i],FileNameString)
            Initals=FileNameString[0:i]
            break
    return Initals

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
    PlayerScoreCard ["ScoreCard"]["Holes"][0]["HoleNumber"]=RemoveData()
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
    if(len(FileNameStr)>=14):
            PM=FileNameStr[:-4]
            if(PM[-2:]=='pm'):
                TimeOfPlay = 2
            elif(PM[-2:]=='m2'):
                TimeOfPlay = 3
            else:
                TimeOfPlay = 1
    return TimeOfPlay

def Converted(FileName):
    source_file = RootFolder+'/'+FileName
    source_file = RootFolder+'/Converted/'+FileName
    os.rename(source_file,source_file)
    return


FileList= FindFile2Convert(RootFolder)

# for file in FileList:
#     print(file)


    #


# define functions for use else where
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

#print("Filename",ConvertFileName)

data=""
body_str = "<!--START OF OUTPUT FROM EXCEL PUBLISH AS WEB PAGE WIZARD"
from_here_on_in = 0
season ="season"
player = "Player"
course_name = "Course_name"
Par_lable = "Parlab"
Par = "Par"
Fairway_lable = "Fairwaylab"
Fairway_Count = "FairewaysCount"
Date_lable = "Datelab"
Played_Date = "Date"
Handicap_Lable = "Handicaplab"
Handicap = "Handicap"
startP = ">"
EndP = "</td>"
for ConvertFileName in FileList:
    my_list=ReadInDataFile(RootFolder+'/'+ConvertFileName)
    #for i,Raw_line in enumerate(my_list):
        if body_str in Raw_line:
            from_here_on_in = i   #print from_here_on_in
            Season =my_list[ from_here_on_in +3 ]
            Player =my_list[ from_here_on_in +17 ]
            Club =my_list[ from_here_on_in +23 ]
            Par_SS =my_list[ from_here_on_in +27 ]
            Num_Fairways =my_list[ from_here_on_in +30 ]
            Pdate =my_list[ from_here_on_in +34 ]
            Playing_Handicap =my_list[ from_here_on_in +36 ]
            Handicap =my_list[ from_here_on_in +36 ]
            Event_Place =my_list[ from_here_on_in +41 ]
            Major =my_list[ from_here_on_in +42 ]
            Prize_Money =my_list[ from_here_on_in +46 ]
            DB_Plus =my_list[ from_here_on_in +61 ]
            DB =my_list[ from_here_on_in +62 ]
            Bi =my_list[ from_here_on_in +63 ]
            P =my_list[ from_here_on_in +64 ]
            B =my_list[ from_here_on_in +65 ]
            E =my_list[ from_here_on_in +66 ]
            A =my_list[ from_here_on_in +67 ]
            H1 =my_list[ from_here_on_in +68 ]
            Hole1 =my_list[ from_here_on_in +89 ]
            Par1 =my_list[ from_here_on_in +90 ]
            Stroke_Index1 =my_list[ from_here_on_in +91 ]
            Gross_Score1 =my_list[ from_here_on_in +92 ]
            Points1 =my_list[ from_here_on_in +93 ]
            Putts1 =my_list[ from_here_on_in +94 ]
            Fairway1 =my_list[ from_here_on_in +95 ]
            Ferret1 =my_list[ from_here_on_in +96 ]
            Green_Regulation1 =my_list[ from_here_on_in +97 ]
            Hole2 =my_list[ from_here_on_in +100 ]
            Par2 =my_list[ from_here_on_in +101 ]
            Stroke_Index2 =my_list[ from_here_on_in +102 ]
            Gross_Score2 =my_list[ from_here_on_in +103 ]
            Points2 =my_list[ from_here_on_in +104 ]
            Putts2 =my_list[ from_here_on_in +105 ]
            Fairway2 =my_list[ from_here_on_in +106 ]
            Ferret2 =my_list[ from_here_on_in +107 ]
            Green_Regulation2 =my_list[ from_here_on_in +108 ]
            Hole3 =my_list[ from_here_on_in +111 ]
            Par3 =my_list[ from_here_on_in +112 ]
            Stroke_Index3 =my_list[ from_here_on_in +113 ]
            Gross_Score3 =my_list[ from_here_on_in +114 ]
            Points3 =my_list[ from_here_on_in +115 ]
            Putts3 =my_list[ from_here_on_in +116 ]
            Fairway3 =my_list[ from_here_on_in +117 ]
            Ferret3 =my_list[ from_here_on_in +118 ]
            Green_Regulation3 =my_list[ from_here_on_in +119 ]
            Hole4 =my_list[ from_here_on_in +122 ]
            Par4 =my_list[ from_here_on_in +123 ]
            Stroke_Index4 =my_list[ from_here_on_in +124 ]
            Gross_Score4 =my_list[ from_here_on_in +125 ]
            Points4 =my_list[ from_here_on_in +126 ]
            Putts4 =my_list[ from_here_on_in +127 ]
            Fairway4 =my_list[ from_here_on_in +128 ]
            Ferret4 =my_list[ from_here_on_in +129 ]
            Green_Regulation4 =my_list[ from_here_on_in +130 ]
            Hole5 =my_list[ from_here_on_in +133 ]
            Par5 =my_list[ from_here_on_in +134 ]
            Stroke_Index5 =my_list[ from_here_on_in +135 ]
            Gross_Score5 =my_list[ from_here_on_in +136 ]
            Points5 =my_list[ from_here_on_in +137 ]
            Putts5 =my_list[ from_here_on_in +138 ]
            Fairway5 =my_list[ from_here_on_in +139 ]
            Ferret5 =my_list[ from_here_on_in +140 ]
            Green_Regulation5 =my_list[ from_here_on_in +141 ]
            Hole6 =my_list[ from_here_on_in +144 ]
            Par6 =my_list[ from_here_on_in +145 ]
            Stroke_Index6 =my_list[ from_here_on_in +146 ]
            Gross_Score6 =my_list[ from_here_on_in +147 ]
            Points6 =my_list[ from_here_on_in +148 ]
            Putts6 =my_list[ from_here_on_in +149 ]
            Fairway6 =my_list[ from_here_on_in +150 ]
            Ferret6 =my_list[ from_here_on_in +151 ]
            Green_Regulation6 =my_list[ from_here_on_in +152 ]
            Hole7 =my_list[ from_here_on_in +155 ]
            Par7 =my_list[ from_here_on_in +156 ]
            Stroke_Index7 =my_list[ from_here_on_in +157 ]
            Gross_Score7 =my_list[ from_here_on_in +158 ]
            Points7 =my_list[ from_here_on_in +159 ]
            Putts7 =my_list[ from_here_on_in +160 ]
            Fairway7 =my_list[ from_here_on_in +161 ]
            Ferret7 =my_list[ from_here_on_in +162 ]
            Green_Regulation7 =my_list[ from_here_on_in +163 ]
            Hole8 =my_list[ from_here_on_in +166 ]
            Par8 =my_list[ from_here_on_in +167 ]
            Stroke_Index8 =my_list[ from_here_on_in +168 ]
            Gross_Score8 =my_list[ from_here_on_in +169 ]
            Points8 =my_list[ from_here_on_in +170 ]
            Putts8 =my_list[ from_here_on_in +171 ]
            Fairway8 =my_list[ from_here_on_in +172 ]
            Ferret8 =my_list[ from_here_on_in +173 ]
            Green_Regulation8 =my_list[ from_here_on_in +174 ]
            Hole9 =my_list[ from_here_on_in +177 ]
            Par9 =my_list[ from_here_on_in +178 ]
            Stroke_Index9 =my_list[ from_here_on_in +179 ]
            Gross_Score9 =my_list[ from_here_on_in +180 ]
            Points9 =my_list[ from_here_on_in +181 ]
            Putts9 =my_list[ from_here_on_in +182 ]
            Fairway9 =my_list[ from_here_on_in +183 ]
            Ferret9 =my_list[ from_here_on_in +184 ]
            Green_Regulation9 =my_list[ from_here_on_in +185 ]
            Hole10 =my_list[ from_here_on_in +188 ]
            Par10 =my_list[ from_here_on_in +189 ]
            Stroke_Index10 =my_list[ from_here_on_in +190 ]
            Gross_Score10 =my_list[ from_here_on_in +191 ]
            Points10 =my_list[ from_here_on_in +192 ]
            Putts10 =my_list[ from_here_on_in +193 ]
            Fairway10 =my_list[ from_here_on_in +194 ]
            Ferret10 =my_list[ from_here_on_in +195 ]
            Green_Regulation10 =my_list[ from_here_on_in +196 ]
            Hole11 =my_list[ from_here_on_in +199 ]
            Par11 =my_list[ from_here_on_in +200 ]
            Stroke_Index11 =my_list[ from_here_on_in +201 ]
            Gross_Score11 =my_list[ from_here_on_in +202 ]
            Points11 =my_list[ from_here_on_in +203 ]
            Putts11 =my_list[ from_here_on_in +204 ]
            Fairway11 =my_list[ from_here_on_in +205 ]
            Ferret11 =my_list[ from_here_on_in +206 ]
            Green_Regulation11 =my_list[ from_here_on_in +207 ]
            Hole12 =my_list[ from_here_on_in +210 ]
            Par12 =my_list[ from_here_on_in +211 ]
            Stroke_Index12 =my_list[ from_here_on_in +212 ]
            Gross_Score12 =my_list[ from_here_on_in +213 ]
            Points12 =my_list[ from_here_on_in +214 ]
            Putts12 =my_list[ from_here_on_in +215 ]
            Fairway12 =my_list[ from_here_on_in +216 ]
            Ferret12 =my_list[ from_here_on_in +217 ]
            Green_Regulation12 =my_list[ from_here_on_in +218 ]
            Hole13 =my_list[ from_here_on_in +221 ]
            Par13 =my_list[ from_here_on_in +222 ]
            Stroke_Index13 =my_list[ from_here_on_in +223 ]
            Gross_Score13 =my_list[ from_here_on_in +224 ]
            Points13 =my_list[ from_here_on_in +225 ]
            Putts13 =my_list[ from_here_on_in +226 ]
            Fairway13 =my_list[ from_here_on_in +227 ]
            Ferret13 =my_list[ from_here_on_in +228 ]
            Green_Regulation13 =my_list[ from_here_on_in +229 ]
            Hole14 =my_list[ from_here_on_in +232 ]
            Par14 =my_list[ from_here_on_in +233 ]
            Stroke_Index14 =my_list[ from_here_on_in +234 ]
            Gross_Score14 =my_list[ from_here_on_in +235 ]
            Points14 =my_list[ from_here_on_in +236 ]
            Putts14 =my_list[ from_here_on_in +237 ]
            Fairway14 =my_list[ from_here_on_in +238 ]
            Ferret14 =my_list[ from_here_on_in +239 ]
            Green_Regulation14 =my_list[ from_here_on_in +240 ]
            Hole15 =my_list[ from_here_on_in +243 ]
            Par15 =my_list[ from_here_on_in +244 ]
            Stroke_Index15 =my_list[ from_here_on_in +245 ]
            Gross_Score15 =my_list[ from_here_on_in +246 ]
            Points15 =my_list[ from_here_on_in +247 ]
            Putts15 =my_list[ from_here_on_in +248 ]
            Fairway15 =my_list[ from_here_on_in +249 ]
            Ferret15 =my_list[ from_here_on_in +250 ]
            Green_Regulation15 =my_list[ from_here_on_in +251 ]
            Hole16 =my_list[ from_here_on_in +254 ]
            Par16 =my_list[ from_here_on_in +255 ]
            Stroke_Index16 =my_list[ from_here_on_in +256 ]
            Gross_Score16 =my_list[ from_here_on_in +257 ]
            Points16 =my_list[ from_here_on_in +258 ]
            Putts16 =my_list[ from_here_on_in +259 ]
            Fairway16 =my_list[ from_here_on_in +260 ]
            Ferret16 =my_list[ from_here_on_in +261 ]
            Green_Regulation16 =my_list[ from_here_on_in +262 ]
            Hole17 =my_list[ from_here_on_in +265 ]
            Par17 =my_list[ from_here_on_in +266 ]
            Stroke_Index17 =my_list[ from_here_on_in +267 ]
            Gross_Score17 =my_list[ from_here_on_in +268 ]
            Points17 =my_list[ from_here_on_in +269 ]
            Putts17 =my_list[ from_here_on_in +270 ]
            Fairway17 =my_list[ from_here_on_in +271 ]
            Ferret17 =my_list[ from_here_on_in +272 ]
            Green_Regulation17 =my_list[ from_here_on_in +273 ]
            Hole18 =my_list[ from_here_on_in +276 ]
            Par18 =my_list[ from_here_on_in +277 ]
            Stroke_Index18 =my_list[ from_here_on_in +278 ]
            Gross_Score18 =my_list[ from_here_on_in +279 ]
            Points18 =my_list[ from_here_on_in +280 ]
            Putts18 =my_list[ from_here_on_in +281 ]
            Fairway18 =my_list[ from_here_on_in +282 ]
            Ferret18 =my_list[ from_here_on_in +283 ]
            Green_Regulation18 =my_list[ from_here_on_in +284 ]
            Totals =my_list[ from_here_on_in +287 ]
            Tpar =my_list[ from_here_on_in +288 ]
            TGS =my_list[ from_here_on_in +291 ]
            TPO =my_list[ from_here_on_in +293 ]
            TPUT =my_list[ from_here_on_in +295 ]
            TFW =my_list[ from_here_on_in +297 ]
            TF =my_list[ from_here_on_in +299 ]
            TGR =my_list[ from_here_on_in +301 ]
        # Removed unwanted parts of the String
        #Create the Events Details for JSON record
            PlayerScoreCard["Event"]["EventUUID"] =uuid.uuid4().hex             #Universally unique identifier for the Event should be the same for each player that played event 
            PlayerScoreCard["Event"]["Season"] = Season[Season.find('id="')+4:Season.find('" ')]
            PlayerScoreCard["Event"]['DatePlayed'] = RemoveData(Pdate)
            PlayerScoreCard["Event"]['MajorEventName'] = RemoveData(Major)
            PlayerScoreCard["Event"]['EventStanding'] =RemoveData(Event_Place)
            PlayerScoreCard["Event"]['PrizeFund'] = RemoveData(Prize_Money)
            PlayerScoreCard["Event"]["OrderOfTheDay"] = GamesInDay(ConvertFileName)
            #If filename has pm then game is second event of the day.
            #Creat the Player Details
            PlayerScoreCard["Player"]["PlayerUUID"] =uuid.uuid4().hex           #Universally unique identifier for the Player should be the same on each score card 
            PlayerScoreCard['Player']['PlayerName']=RemoveData(Player)
            PlayerScoreCard['Player']["BeforeHandicap"]=RemoveData(Playing_Handicap)
            if Handicap.find('\"') != -1:
                PlayerScoreCard['Player']["AfterHandicap"] = Handicap[Handicap.find('\"')+1:Handicap.find('\"',Handicap.find('\"')+1)]
            else:
                PlayerScoreCard['Player']["AfterHandicap"]= Playing_Handicap
            #Create the Course Details for JSON record
            PlayerScoreCard["CourseDetails"]["CourseUUID"] =uuid.uuid4().hex    #Universally unique identifier for the Course each Tee and couse arrangement should have this the same 
            PlayerScoreCard['CourseDetails']['CourseName'] = RemoveData(Club)
            PlayerScoreCard['CourseDetails']['NumberOfFairways'] = RemoveData(Num_Fairways)
            PlayerScoreCard['CourseDetails']['ParSS']=RemoveData(Par_SS)
            #Pdate = Pdate[Pdate.find(startP)+1:Pdate.find(EndP)]
            #Pdate=RemoveData(Pdate)
            #Create the Proprties for JSON record
            PlayerScoreCard["Properties"]["ScoreCardUUID"] =uuid.uuid4().hex    #Universally unique identifier for the ScoreCard 
            PlayerScoreCard["Properties"]["FileName"]=FormatDate(PlayerScoreCard["Event"]['DatePlayed'])+'-'+PlayerScoreCard["Properties"]["ScoreCardUUID"]+'.json'
            PlayerScoreCard["Properties"]["OrginalFile"]=ConvertFileName
            PlayerScoreCard["Properties"]["FileInitals"]=PlayerInitals(ConvertFileName)
            
            #Create the ScoreCardStats for JSON record
            #PlayerScoreCard["ScoreCardStats"]["ScoreCardStats"]
            PlayerScoreCard["ScoreCardStats"]["HoleInOne"]=RemoveData(H1)
            #PlayerScoreCard["ScoreCardStats"]["Condor"]=RemoveData(H1)
            PlayerScoreCard["ScoreCardStats"]["Albatross"]=RemoveData(A)
            PlayerScoreCard["ScoreCardStats"]["Eagle"]=RemoveData(E)
            PlayerScoreCard["ScoreCardStats"]["Birdie"]=RemoveData(B)
            PlayerScoreCard["ScoreCardStats"]["Par"]=RemoveData(P)
            PlayerScoreCard["ScoreCardStats"]["Bogey"]=RemoveData(Bi)
            PlayerScoreCard["ScoreCardStats"]["DoubleBogey"]=RemoveData(DB)
            PlayerScoreCard["ScoreCardStats"]["DoubleBogey+"]=RemoveData(DB_Plus)
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
            #Hole 1
            #PlayerScoreCard ["ScoreCard"]["Holes"][1]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][1]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][1]["Par"]=RemoveData(Par1)
            PlayerScoreCard["ScoreCard"]["Holes"][1]["StokeIndex"]=RemoveData(Stroke_Index1)
            PlayerScoreCard["ScoreCard"]["Holes"][1]["GrossScore"]=RemoveData(Gross_Score1)
            PlayerScoreCard["ScoreCard"]["Holes"][1]["Points"]=RemoveData(Points1)
            PlayerScoreCard["ScoreCard"]["Holes"][1]["Putts"]=RemoveData(Putts1)
            PlayerScoreCard["ScoreCard"]["Holes"][1]["FairwayHit"]=RemoveData(Fairway1)
            PlayerScoreCard["ScoreCard"]["Holes"][1]["Ferrets"]=RemoveData(Ferret1)
            PlayerScoreCard["ScoreCard"]["Holes"][1]["GreensInRegulation"]=RemoveData(Green_Regulation1)
            #PlayerScoreCard ["ScoreCard"]["Holes"][1]["HandicapStokes"]=RemoveData()
            #Hole2
            #PlayerScoreCard ["ScoreCard"]["Holes"][2]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][2]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][2]["Par"]=RemoveData(Par2)
            PlayerScoreCard["ScoreCard"]["Holes"][2]["StokeIndex"]=RemoveData(Stroke_Index2)
            PlayerScoreCard["ScoreCard"]["Holes"][2]["GrossScore"]=RemoveData(Gross_Score2)
            PlayerScoreCard["ScoreCard"]["Holes"][2]["Points"]=RemoveData(Points2)
            PlayerScoreCard["ScoreCard"]["Holes"][2]["Putts"]=RemoveData(Putts2)
            PlayerScoreCard["ScoreCard"]["Holes"][2]["FairwayHit"]=RemoveData(Fairway2)
            PlayerScoreCard["ScoreCard"]["Holes"][2]["Ferrets"]=RemoveData(Ferret2)
            PlayerScoreCard["ScoreCard"]["Holes"][2]["GreensInRegulation"]=RemoveData(Green_Regulation2)
            #PlayerScoreCard ["ScoreCard"]["Holes"][12]["HandicapStokes"]=RemoveData()
            #Hole 3
            #PlayerScoreCard ["ScoreCard"]["Holes"][3]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][3]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][3]["Par"]=RemoveData(Par3)
            PlayerScoreCard["ScoreCard"]["Holes"][3]["StokeIndex"]=RemoveData(Stroke_Index3)
            PlayerScoreCard["ScoreCard"]["Holes"][3]["GrossScore"]=RemoveData(Gross_Score3)
            PlayerScoreCard["ScoreCard"]["Holes"][3]["Points"]=RemoveData(Points3)
            PlayerScoreCard["ScoreCard"]["Holes"][3]["Putts"]=RemoveData(Putts3)
            PlayerScoreCard["ScoreCard"]["Holes"][3]["FairwayHit"]=RemoveData(Fairway3)
            PlayerScoreCard["ScoreCard"]["Holes"][3]["Ferrets"]=RemoveData(Ferret3)
            PlayerScoreCard["ScoreCard"]["Holes"][3]["GreensInRegulation"]=RemoveData(Green_Regulation3)
            #PlayerScoreCard ["ScoreCard"]["Holes"][3]["HandicapStokes"]=RemoveData()
            #Hole 4
            #PlayerScoreCard ["ScoreCard"]["Holes"][4]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][4]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][4]["Par"]=RemoveData(Par4)
            PlayerScoreCard["ScoreCard"]["Holes"][4]["StokeIndex"]=RemoveData(Stroke_Index4)
            PlayerScoreCard["ScoreCard"]["Holes"][4]["GrossScore"]=RemoveData(Gross_Score4)
            PlayerScoreCard["ScoreCard"]["Holes"][4]["Points"]=RemoveData(Points4)
            PlayerScoreCard["ScoreCard"]["Holes"][4]["Putts"]=RemoveData(Putts4)
            PlayerScoreCard["ScoreCard"]["Holes"][4]["FairwayHit"]=RemoveData(Fairway4)
            PlayerScoreCard["ScoreCard"]["Holes"][4]["Ferrets"]=RemoveData(Ferret4)
            PlayerScoreCard["ScoreCard"]["Holes"][4]["GreensInRegulation"]=RemoveData(Green_Regulation4)
            #PlayerScoreCard ["ScoreCard"]["Holes"][4]["HandicapStokes"]=RemoveData()
            #Hole 5
            #PlayerScoreCard ["ScoreCard"]["Holes"][5]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][5]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][5]["Par"]=RemoveData(Par5)
            PlayerScoreCard["ScoreCard"]["Holes"][5]["StokeIndex"]=RemoveData(Stroke_Index5)
            PlayerScoreCard["ScoreCard"]["Holes"][5]["GrossScore"]=RemoveData(Gross_Score5)
            PlayerScoreCard["ScoreCard"]["Holes"][5]["Points"]=RemoveData(Points5)
            PlayerScoreCard["ScoreCard"]["Holes"][5]["Putts"]=RemoveData(Putts5)
            PlayerScoreCard["ScoreCard"]["Holes"][5]["FairwayHit"]=RemoveData(Fairway5)
            PlayerScoreCard["ScoreCard"]["Holes"][5]["Ferrets"]=RemoveData(Ferret5)
            PlayerScoreCard["ScoreCard"]["Holes"][5]["GreensInRegulation"]=RemoveData(Green_Regulation5)
            #PlayerScoreCard ["ScoreCard"]["Holes"][5]["HandicapStokes"]=RemoveData()
            #Hole 6
            #PlayerScoreCard ["ScoreCard"]["Holes"][6]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][6]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][6]["Par"]=RemoveData(Par6)
            PlayerScoreCard["ScoreCard"]["Holes"][6]["StokeIndex"]=RemoveData(Stroke_Index6)
            PlayerScoreCard["ScoreCard"]["Holes"][6]["GrossScore"]=RemoveData(Gross_Score6)
            PlayerScoreCard["ScoreCard"]["Holes"][6]["Points"]=RemoveData(Points6)
            PlayerScoreCard["ScoreCard"]["Holes"][6]["Putts"]=RemoveData(Putts6)
            PlayerScoreCard["ScoreCard"]["Holes"][6]["FairwayHit"]=RemoveData(Fairway6)
            PlayerScoreCard["ScoreCard"]["Holes"][6]["Ferrets"]=RemoveData(Ferret6)
            PlayerScoreCard["ScoreCard"]["Holes"][6]["GreensInRegulation"]=RemoveData(Green_Regulation6)
            #PlayerScoreCard ["ScoreCard"]["Holes"][6]["HandicapStokes"]=RemoveData()
            #Hole 7
            #PlayerScoreCard ["ScoreCard"]["Holes"][7]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][7]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][7]["Par"]=RemoveData(Par7)
            PlayerScoreCard["ScoreCard"]["Holes"][7]["StokeIndex"]=RemoveData(Stroke_Index7)
            PlayerScoreCard["ScoreCard"]["Holes"][7]["GrossScore"]=RemoveData(Gross_Score7)
            PlayerScoreCard["ScoreCard"]["Holes"][7]["Points"]=RemoveData(Points7)
            PlayerScoreCard["ScoreCard"]["Holes"][7]["Putts"]=RemoveData(Putts7)
            PlayerScoreCard["ScoreCard"]["Holes"][7]["FairwayHit"]=RemoveData(Fairway7)
            PlayerScoreCard["ScoreCard"]["Holes"][7]["Ferrets"]=RemoveData(Ferret7)
            PlayerScoreCard["ScoreCard"]["Holes"][7]["GreensInRegulation"]=RemoveData(Green_Regulation7)
            #PlayerScoreCard ["ScoreCard"]["Holes"][7]["HandicapStokes"]=RemoveData()
            #Hole 8
            #PlayerScoreCard ["ScoreCard"]["Holes"][8]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][8]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][8]["Par"]=RemoveData(Par8)
            PlayerScoreCard["ScoreCard"]["Holes"][8]["StokeIndex"]=RemoveData(Stroke_Index8)
            PlayerScoreCard["ScoreCard"]["Holes"][8]["GrossScore"]=RemoveData(Gross_Score8)
            PlayerScoreCard["ScoreCard"]["Holes"][8]["Points"]=RemoveData(Points8)
            PlayerScoreCard["ScoreCard"]["Holes"][8]["Putts"]=RemoveData(Putts8)
            PlayerScoreCard["ScoreCard"]["Holes"][8]["FairwayHit"]=RemoveData(Fairway8)
            PlayerScoreCard["ScoreCard"]["Holes"][8]["Ferrets"]=RemoveData(Ferret8)
            PlayerScoreCard["ScoreCard"]["Holes"][8]["GreensInRegulation"]=RemoveData(Green_Regulation8)
            #PlayerScoreCard ["ScoreCard"]["Holes"][8]["HandicapStokes"]=RemoveData()
            #Hole 9
            #PlayerScoreCard ["ScoreCard"]["Holes"][9]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][9]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][9]["Par"]=RemoveData(Par9)
            PlayerScoreCard["ScoreCard"]["Holes"][9]["StokeIndex"]=RemoveData(Stroke_Index9)
            PlayerScoreCard["ScoreCard"]["Holes"][9]["GrossScore"]=RemoveData(Gross_Score9)
            PlayerScoreCard["ScoreCard"]["Holes"][9]["Points"]=RemoveData(Points9)
            PlayerScoreCard["ScoreCard"]["Holes"][9]["Putts"]=RemoveData(Putts9)
            PlayerScoreCard["ScoreCard"]["Holes"][9]["FairwayHit"]=RemoveData(Fairway9)
            PlayerScoreCard["ScoreCard"]["Holes"][9]["Ferrets"]=RemoveData(Ferret9)
            PlayerScoreCard["ScoreCard"]["Holes"][9]["GreensInRegulation"]=RemoveData(Green_Regulation9)
            #PlayerScoreCard ["ScoreCard"]["Holes"][9]["HandicapStokes"]=RemoveData()
            #Hole 10
            #PlayerScoreCard ["ScoreCard"]["Holes"][10]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][10]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][10]["Par"]=RemoveData(Par10)
            PlayerScoreCard["ScoreCard"]["Holes"][10]["StokeIndex"]=RemoveData(Stroke_Index10)
            PlayerScoreCard["ScoreCard"]["Holes"][10]["GrossScore"]=RemoveData(Gross_Score10)
            PlayerScoreCard["ScoreCard"]["Holes"][10]["Points"]=RemoveData(Points10)
            PlayerScoreCard["ScoreCard"]["Holes"][10]["Putts"]=RemoveData(Putts10)
            PlayerScoreCard["ScoreCard"]["Holes"][10]["FairwayHit"]=RemoveData(Fairway10)
            PlayerScoreCard["ScoreCard"]["Holes"][10]["Ferrets"]=RemoveData(Ferret10)
            PlayerScoreCard["ScoreCard"]["Holes"][10]["GreensInRegulation"]=RemoveData(Green_Regulation10)
            #PlayerScoreCard ["ScoreCard"]["Holes"][10]["HandicapStokes"]=RemoveData()
            #Hole 11
            #PlayerScoreCard ["ScoreCard"]["Holes"][11]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][11]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][11]["Par"]=RemoveData(Par11)
            PlayerScoreCard["ScoreCard"]["Holes"][11]["StokeIndex"]=RemoveData(Stroke_Index11)
            PlayerScoreCard["ScoreCard"]["Holes"][11]["GrossScore"]=RemoveData(Gross_Score11)
            PlayerScoreCard["ScoreCard"]["Holes"][11]["Points"]=RemoveData(Points11)
            PlayerScoreCard["ScoreCard"]["Holes"][11]["Putts"]=RemoveData(Putts11)
            PlayerScoreCard["ScoreCard"]["Holes"][11]["FairwayHit"]=RemoveData(Fairway11)
            PlayerScoreCard["ScoreCard"]["Holes"][11]["Ferrets"]=RemoveData(Ferret11)
            PlayerScoreCard["ScoreCard"]["Holes"][11]["GreensInRegulation"]=RemoveData(Green_Regulation11)
            #PlayerScoreCard ["ScoreCard"]["Holes"][11]["HandicapStokes"]=RemoveData()
            #Hole 12
            #PlayerScoreCard ["ScoreCard"]["Holes"][12]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][12]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][12]["Par"]=RemoveData(Par12)
            PlayerScoreCard["ScoreCard"]["Holes"][12]["StokeIndex"]=RemoveData(Stroke_Index12)
            PlayerScoreCard["ScoreCard"]["Holes"][12]["GrossScore"]=RemoveData(Gross_Score12)
            PlayerScoreCard["ScoreCard"]["Holes"][12]["Points"]=RemoveData(Points12)
            PlayerScoreCard["ScoreCard"]["Holes"][12]["Putts"]=RemoveData(Putts12)
            PlayerScoreCard["ScoreCard"]["Holes"][12]["FairwayHit"]=RemoveData(Fairway12)
            PlayerScoreCard["ScoreCard"]["Holes"][12]["Ferrets"]=RemoveData(Ferret12)
            PlayerScoreCard["ScoreCard"]["Holes"][12]["GreensInRegulation"]=RemoveData(Green_Regulation12)
            #PlayerScoreCard ["ScoreCard"]["Holes"][12]["HandicapStokes"]=RemoveData()
            #Hole 13
            #PlayerScoreCard ["ScoreCard"]["Holes"][13]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][13]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][13]["Par"]=RemoveData(Par13)
            PlayerScoreCard["ScoreCard"]["Holes"][13]["StokeIndex"]=RemoveData(Stroke_Index13)
            PlayerScoreCard["ScoreCard"]["Holes"][13]["GrossScore"]=RemoveData(Gross_Score13)
            PlayerScoreCard["ScoreCard"]["Holes"][13]["Points"]=RemoveData(Points13)
            PlayerScoreCard["ScoreCard"]["Holes"][13]["Putts"]=RemoveData(Putts13)
            PlayerScoreCard["ScoreCard"]["Holes"][13]["FairwayHit"]=RemoveData(Fairway13)
            PlayerScoreCard["ScoreCard"]["Holes"][13]["Ferrets"]=RemoveData(Ferret13)
            PlayerScoreCard["ScoreCard"]["Holes"][13]["GreensInRegulation"]=RemoveData(Green_Regulation13)
            #PlayerScoreCard ["ScoreCard"]["Holes"][13]["HandicapStokes"]=RemoveData()
            #Hole 14
            #PlayerScoreCard ["ScoreCard"]["Holes"][14]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][14]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][14]["Par"]=RemoveData(Par14)
            PlayerScoreCard["ScoreCard"]["Holes"][14]["StokeIndex"]=RemoveData(Stroke_Index14)
            PlayerScoreCard["ScoreCard"]["Holes"][14]["GrossScore"]=RemoveData(Gross_Score14)
            PlayerScoreCard["ScoreCard"]["Holes"][14]["Points"]=RemoveData(Points14)
            PlayerScoreCard["ScoreCard"]["Holes"][14]["Putts"]=RemoveData(Putts14)
            PlayerScoreCard["ScoreCard"]["Holes"][14]["FairwayHit"]=RemoveData(Fairway14)
            PlayerScoreCard["ScoreCard"]["Holes"][14]["Ferrets"]=RemoveData(Ferret14)
            PlayerScoreCard["ScoreCard"]["Holes"][14]["GreensInRegulation"]=RemoveData(Green_Regulation14)
            #PlayerScoreCard ["ScoreCard"]["Holes"][14]["HandicapStokes"]=RemoveData()
            #Hole 15
            #PlayerScoreCard ["ScoreCard"]["Holes"][15]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][15]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][15]["Par"]=RemoveData(Par15)
            PlayerScoreCard["ScoreCard"]["Holes"][15]["StokeIndex"]=RemoveData(Stroke_Index15)
            PlayerScoreCard["ScoreCard"]["Holes"][15]["GrossScore"]=RemoveData(Gross_Score15)
            PlayerScoreCard["ScoreCard"]["Holes"][15]["Points"]=RemoveData(Points15)
            PlayerScoreCard["ScoreCard"]["Holes"][15]["Putts"]=RemoveData(Putts15)
            PlayerScoreCard["ScoreCard"]["Holes"][15]["FairwayHit"]=RemoveData(Fairway15)
            PlayerScoreCard["ScoreCard"]["Holes"][15]["Ferrets"]=RemoveData(Ferret15)
            PlayerScoreCard["ScoreCard"]["Holes"][15]["GreensInRegulation"]=RemoveData(Green_Regulation15)
            #PlayerScoreCard ["ScoreCard"]["Holes"][15]["HandicapStokes"]=RemoveData()
            #Hole 16
            #PlayerScoreCard ["ScoreCard"]["Holes"][16]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][16]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][16]["Par"]=RemoveData(Par16)
            PlayerScoreCard["ScoreCard"]["Holes"][16]["StokeIndex"]=RemoveData(Stroke_Index16)
            PlayerScoreCard["ScoreCard"]["Holes"][16]["GrossScore"]=RemoveData(Gross_Score16)
            PlayerScoreCard["ScoreCard"]["Holes"][16]["Points"]=RemoveData(Points16)
            PlayerScoreCard["ScoreCard"]["Holes"][16]["Putts"]=RemoveData(Putts16)
            PlayerScoreCard["ScoreCard"]["Holes"][16]["FairwayHit"]=RemoveData(Fairway16)
            PlayerScoreCard["ScoreCard"]["Holes"][16]["Ferrets"]=RemoveData(Ferret16)
            PlayerScoreCard["ScoreCard"]["Holes"][16]["GreensInRegulation"]=RemoveData(Green_Regulation16)
            #PlayerScoreCard ["ScoreCard"]["Holes"][16]["HandicapStokes"]=RemoveData()
            #Hole 17
            #PlayerScoreCard ["ScoreCard"]["Holes"][17]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][17]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][17]["Par"]=RemoveData(Par17)
            PlayerScoreCard["ScoreCard"]["Holes"][17]["StokeIndex"]=RemoveData(Stroke_Index17)
            PlayerScoreCard["ScoreCard"]["Holes"][17]["GrossScore"]=RemoveData(Gross_Score17)
            PlayerScoreCard["ScoreCard"]["Holes"][17]["Points"]=RemoveData(Points17)
            PlayerScoreCard["ScoreCard"]["Holes"][17]["Putts"]=RemoveData(Putts17)
            PlayerScoreCard["ScoreCard"]["Holes"][17]["FairwayHit"]=RemoveData(Fairway17)
            PlayerScoreCard["ScoreCard"]["Holes"][17]["Ferrets"]=RemoveData(Ferret17)
            PlayerScoreCard["ScoreCard"]["Holes"][17]["GreensInRegulation"]=RemoveData(Green_Regulation17)
            #PlayerScoreCard ["ScoreCard"]["Holes"][17]["HandicapStokes"]=RemoveData()
            #Hole 18
            #PlayerScoreCard ["ScoreCard"]["Holes"][18]["HoleNumber"]=RemoveData()
            #PlayerScoreCard ["ScoreCard"]["Holes"][18]["Yardage"]=RemoveData()
            PlayerScoreCard["ScoreCard"]["Holes"][18]["Par"]=RemoveData(Par18)
            PlayerScoreCard["ScoreCard"]["Holes"][18]["StokeIndex"]=RemoveData(Stroke_Index18)
            PlayerScoreCard["ScoreCard"]["Holes"][18]["GrossScore"]=RemoveData(Gross_Score18)
            PlayerScoreCard["ScoreCard"]["Holes"][18]["Points"]=RemoveData(Points18)
            PlayerScoreCard["ScoreCard"]["Holes"][18]["Putts"]=RemoveData(Putts18)
            PlayerScoreCard["ScoreCard"]["Holes"][18]["FairwayHit"]=RemoveData(Fairway18)
            PlayerScoreCard["ScoreCard"]["Holes"][18]["Ferrets"]=RemoveData(Ferret18)
            PlayerScoreCard["ScoreCard"]["Holes"][18]["GreensInRegulation"]=RemoveData(Green_Regulation18)
            #PlayerScoreCard ["ScoreCard"]["Holes"][18]["HandicapStokes"]=RemoveData()
            
            #Totals is createing the sum of the 18 holes 
            # # declare totals variables for each page. set counts to zero
            SetScoreCardTotals()
            print(PlayerScoreCard["ScoreCard"]["Holes"][0])        
 

        op_line =op_Last_Line=list()
        print(PlayerScoreCard) 

       # print( TPar,TStroke_Index,TGross_Score,TPoints,TPutts,TFairways,TFerrets)
        #write out new HTML file
        melbagefile = open(TargetHTMLFolder+'/'+ConvertFileName,"wb")

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
        melbagefile.write( '<tr><td><h1>'+PlayerScoreCard['Player']['PlayerName']+'</h1></td><td><h1>'+PlayerScoreCard['CourseDetails']['CourseName']+'</h1></td><td><h1>'+PlayerScoreCard["Event"]['DatePlayed']+'</h1></td><tr>');
        melbagefile.write( '<tr><td>'+'Playing Handicap <h1>'+str(PlayerScoreCard['Player']['BeforeHandicap'])+'</h1></td><td>'+'Par/SS <h1>'+str(PlayerScoreCard['CourseDetails']['ParSS'])+'</h1></td><td>'+'Events Place <h1>'+str(PlayerScoreCard["Event"]['EventStanding'])+" "+str(PlayerScoreCard["Event"]['MajorEventName'])+'</h1></td><tr>');
        melbagefile.write( '<tr><td>'+'Actual Handicap <h1>'+str(PlayerScoreCard['Player']["AfterHandicap"])+'</h></td><td>''Number of Fairway <h1>'+str(PlayerScoreCard['CourseDetails']['NumberOfFairways'])+'</h1></td><td> Prize Money <h1> &pound '+str(PlayerScoreCard["Event"]['PrizeFund'])+'</h1></td><tr>');
        melbagefile.write( '</table>');

        melbagefile.write( '<br>');
        melbagefile.write( '<br>');
        melbagefile.write( '<table>');

        Tab='</td><td>'
        MarkUpOdd ='<tr class ="odd">'
        MarkUpEven = '<tr class ="even">'
        start ='<tr>'
        melbagefile.write( "<table>");
        for enum,Record in enumerate(PlayerScoreCard['ScoreCard']['Holes']):
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
        melbagefile.write( '<tr><td>'+str(PlayerScoreCard["ScoreCardStats"]["DoubleBogey+"])+'</td><td>'+str(PlayerScoreCard["ScoreCardStats"]["DoubleBogey"])+'</td><td>'+str(PlayerScoreCard["ScoreCardStats"]["Bogey"])+'</td><td>'+str(PlayerScoreCard["ScoreCardStats"]["Par"])+'</td><td>'+str(PlayerScoreCard["ScoreCardStats"]["Birdie"])+'</td><td>'+str(PlayerScoreCard["ScoreCardStats"]["Eagle"])+'</td><td>'+str(PlayerScoreCard["ScoreCardStats"]["Albatross"])+'</td><td>0</td><td>'+str(PlayerScoreCard["ScoreCardStats"]["HoleInOne"])+'</td><tr>');
        melbagefile.write( '</table>');
        melbagefile.write( '</div>');
        melbagefile.write( '<br>');
        melbagefile.write( '	</body>');
        melbagefile.write( '</html>');

        melbagefile.close()

        #Create JSON Object
        print("File",TargetJSONFolder+'/'+PlayerScoreCard["Properties"]["FileName"])
        print("FileName",PlayerScoreCard["Properties"]["FileName"])
        print("FileName",PlayerScoreCard["Properties"])
        #PlayerScoreCard["Properties"]["FileName"]
        with open(TargetJSONFolder+'/'+PlayerScoreCard["Properties"]["FileName"],'w') as f:
            json.dump(PlayerScoreCard ,f,indent=4, sort_keys=True)    
        
        #Move file to converted folder
        Converted(ConvertFileName)
            
           
