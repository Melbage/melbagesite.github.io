import sys
from os import walk
StartPath = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgatour/season5/apr03/TestCase/'
EndPath = '/Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgatour/season5/apr03/Converted'
f = []
for (dirpath, dirnames, filenames) in walk(StartPath):
	f.extend(filenames)
	break

# check file are of the right type
FileList = list()
for i in f:
	if i.find('.htm') != -1:
		print( i)
		FileList.append(i)

# Filelist should be all the right type of melbage files with htm extension.


# Open the file for reading.
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
data=""
for ConvertFileName in FileList:
	with open(StartPath+'/'+ConvertFileName, 'r') as infile:
		data = infile.read()  # Read the contents of the file into memory.
print("got here")
# Return a list of the lines, breaking at line boundaries.
my_list = data.splitlines()


print(type(my_list),len(my_list) )
for C,line in enumerate(my_list):
    if body_str in line:
        print("line:",C,line)
#    else:
       # print("line is",line)


for i,Raw_line in enumerate(my_list):
	#if Raw_line.find(body_str):
    if body_str in Raw_line:
        print( i,Raw_line)
        from_here_on_in = i   #print from_here_on_in
        print(from_here_on_in,my_list[from_here_on_in])  # assign a variable to each line 
        Season =my_list[ from_here_on_in +3 ]
        print(Season)
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
        print("line TGR",TGR)

# Removed unwanted parts of the String
        print("Before",Season)
        #Season = Season[Season.find('\"')+1:Season.find('\"',season.find('\"')+1)]
        print("after",Season)
        Season = Season[Season.find('id="')+4:Season.find('" ')]
        print("after find",Season)
        Player = Player[Player.find(startP)+1:Player.find(EndP)]
        Club = Club[Club.find(startP)+1:Club.find(EndP)]
        Par_SS = Par_SS[Par_SS.find(startP)+1:Par_SS.find(EndP)]
        Num_Fairways = Num_Fairways[Num_Fairways.find(startP)+1:Num_Fairways.find(EndP)]
        Pdate = Pdate[Pdate.find(startP)+1:Pdate.find(EndP)]
        Playing_Handicap = Playing_Handicap[Playing_Handicap.find(startP)+1:Playing_Handicap.find(EndP)]
# Handicap = Handicap[Handicap.find('\"')+1:Handicap.find('\"',Handicap.find('\"')+1)]
        if Handicap.find('\"') != -1:
            Handicap = Handicap[Handicap.find('\"')+1:Handicap.find('\"',Handicap.find('\"')+1)]
        else:
            Handicap = Playing_Handicap

        Event_Place = Event_Place[Event_Place.find(startP)+1:Event_Place.find(EndP)]
        Major = Major[Major.find(startP)+1:Major.find(EndP)]
        Prize_Money = Prize_Money[Prize_Money.find(startP)+2:Prize_Money.find(EndP)]
        DB_Plus = DB_Plus[DB_Plus.find(startP)+1:DB_Plus.find(EndP)]
        DB = DB[DB.find(startP)+1:DB.find(EndP)]
        Bi = Bi[Bi.find(startP)+1:Bi.find(EndP)]
        P = P[P.find(startP)+1:P.find(EndP)]
        B = B[B.find(startP)+1:B.find(EndP)]
        E = E[E.find(startP)+1:E.find(EndP)]
        A = A[A.find(startP)+1:A.find(EndP)]
        H1 = H1[H1.find(startP)+1:H1.find(EndP)]
        Hole1 = Hole1[Hole1.find(startP)+1:Hole1.find(EndP)]
        Par1 = Par1[Par1.find(startP)+1:Par1.find(EndP)]
        Stroke_Index1 = Stroke_Index1[Stroke_Index1.find(startP)+1:Stroke_Index1.find(EndP)]
        Gross_Score1 = Gross_Score1[Gross_Score1.find(startP)+1:Gross_Score1.find(EndP)]
        Points1 = Points1[Points1.find(startP)+1:Points1.find(EndP)]
        Putts1 = Putts1[Putts1.find(startP)+1:Putts1.find(EndP)]
        Fairway1 = Fairway1[Fairway1.find(startP)+1:Fairway1.find(EndP)]
        Ferret1 = Ferret1[Ferret1.find(startP)+1:Ferret1.find(EndP)]
        Green_Regulation1 = Green_Regulation1[Green_Regulation1.find(startP)+1:Green_Regulation1.find(EndP)]
        Hole2 = Hole2[Hole2.find(startP)+1:Hole2.find(EndP)]
        Par2 = Par2[Par2.find(startP)+1:Par2.find(EndP)]
        Stroke_Index2 = Stroke_Index2[Stroke_Index2.find(startP)+1:Stroke_Index2.find(EndP)]
        Gross_Score2 = Gross_Score2[Gross_Score2.find(startP)+1:Gross_Score2.find(EndP)]
        Points2 = Points2[Points2.find(startP)+1:Points2.find(EndP)]
        Putts2 = Putts2[Putts2.find(startP)+1:Putts2.find(EndP)]
        Fairway2 = Fairway2[Fairway2.find(startP)+1:Fairway2.find(EndP)]
        Ferret2 = Ferret2[Ferret2.find(startP)+1:Ferret2.find(EndP)]
        Green_Regulation2 = Green_Regulation2[Green_Regulation2.find(startP)+1:Green_Regulation2.find(EndP)]
        Hole3 = Hole3[Hole3.find(startP)+1:Hole3.find(EndP)]
        Par3 = Par3[Par3.find(startP)+1:Par3.find(EndP)]
        Stroke_Index3 = Stroke_Index3[Stroke_Index3.find(startP)+1:Stroke_Index3.find(EndP)]
        Gross_Score3 = Gross_Score3[Gross_Score3.find(startP)+1:Gross_Score3.find(EndP)]
        Points3 = Points3[Points3.find(startP)+1:Points3.find(EndP)]
        Putts3 = Putts3[Putts3.find(startP)+1:Putts3.find(EndP)]
        Fairway3 = Fairway3[Fairway3.find(startP)+1:Fairway3.find(EndP)]
        Ferret3 = Ferret3[Ferret3.find(startP)+1:Ferret3.find(EndP)]
        Green_Regulation3 = Green_Regulation3[Green_Regulation3.find(startP)+1:Green_Regulation3.find(EndP)]
        Hole4 = Hole4[Hole4.find(startP)+1:Hole4.find(EndP)]
        Par4 = Par4[Par4.find(startP)+1:Par4.find(EndP)]
        Stroke_Index4 = Stroke_Index4[Stroke_Index4.find(startP)+1:Stroke_Index4.find(EndP)]
        Gross_Score4 = Gross_Score4[Gross_Score4.find(startP)+1:Gross_Score4.find(EndP)]
        Points4 = Points4[Points4.find(startP)+1:Points4.find(EndP)]
        Putts4 = Putts4[Putts4.find(startP)+1:Putts4.find(EndP)]
        Fairway4 = Fairway4[Fairway4.find(startP)+1:Fairway4.find(EndP)]
        Ferret4 = Ferret4[Ferret4.find(startP)+1:Ferret4.find(EndP)]
        Green_Regulation4 = Green_Regulation4[Green_Regulation4.find(startP)+1:Green_Regulation4.find(EndP)]
        Hole5 = Hole5[Hole5.find(startP)+1:Hole5.find(EndP)]
        Par5 = Par5[Par5.find(startP)+1:Par5.find(EndP)]
        Stroke_Index5 = Stroke_Index5[Stroke_Index5.find(startP)+1:Stroke_Index5.find(EndP)]
        Gross_Score5 = Gross_Score5[Gross_Score5.find(startP)+1:Gross_Score5.find(EndP)]
        Points5 = Points5[Points5.find(startP)+1:Points5.find(EndP)]
        Putts5 = Putts5[Putts5.find(startP)+1:Putts5.find(EndP)]
        Fairway5 = Fairway5[Fairway5.find(startP)+1:Fairway5.find(EndP)]
        Ferret5 = Ferret5[Ferret5.find(startP)+1:Ferret5.find(EndP)]
        Green_Regulation5 = Green_Regulation5[Green_Regulation5.find(startP)+1:Green_Regulation5.find(EndP)]
        Hole6 = Hole6[Hole6.find(startP)+1:Hole6.find(EndP)]
        Par6 = Par6[Par6.find(startP)+1:Par6.find(EndP)]
        Stroke_Index6 = Stroke_Index6[Stroke_Index6.find(startP)+1:Stroke_Index6.find(EndP)]
        Gross_Score6 = Gross_Score6[Gross_Score6.find(startP)+1:Gross_Score6.find(EndP)]
        Points6 = Points6[Points6.find(startP)+1:Points6.find(EndP)]
        Putts6 = Putts6[Putts6.find(startP)+1:Putts6.find(EndP)]
        Fairway6 = Fairway6[Fairway6.find(startP)+1:Fairway6.find(EndP)]
        Ferret6 = Ferret6[Ferret6.find(startP)+1:Ferret6.find(EndP)]
        Green_Regulation6 = Green_Regulation6[Green_Regulation6.find(startP)+1:Green_Regulation6.find(EndP)]
        Hole7 = Hole7[Hole7.find(startP)+1:Hole7.find(EndP)]
        Par7 = Par7[Par7.find(startP)+1:Par7.find(EndP)]
        Stroke_Index7 = Stroke_Index7[Stroke_Index7.find(startP)+1:Stroke_Index7.find(EndP)]
        Gross_Score7 = Gross_Score7[Gross_Score7.find(startP)+1:Gross_Score7.find(EndP)]
        Points7 = Points7[Points7.find(startP)+1:Points7.find(EndP)]
        Putts7 = Putts7[Putts7.find(startP)+1:Putts7.find(EndP)]
        Fairway7 = Fairway7[Fairway7.find(startP)+1:Fairway7.find(EndP)]
        Ferret7 = Ferret7[Ferret7.find(startP)+1:Ferret7.find(EndP)]
        Green_Regulation7 = Green_Regulation7[Green_Regulation7.find(startP)+1:Green_Regulation7.find(EndP)]
        Hole8 = Hole8[Hole8.find(startP)+1:Hole8.find(EndP)]
        Par8 = Par8[Par8.find(startP)+1:Par8.find(EndP)]
        Stroke_Index8 = Stroke_Index8[Stroke_Index8.find(startP)+1:Stroke_Index8.find(EndP)]
        Gross_Score8 = Gross_Score8[Gross_Score8.find(startP)+1:Gross_Score8.find(EndP)]
        Points8 = Points8[Points8.find(startP)+1:Points8.find(EndP)]
        Putts8 = Putts8[Putts8.find(startP)+1:Putts8.find(EndP)]
        Fairway8 = Fairway8[Fairway8.find(startP)+1:Fairway8.find(EndP)]
        Ferret8 = Ferret8[Ferret8.find(startP)+1:Ferret8.find(EndP)]
        Green_Regulation8 = Green_Regulation8[Green_Regulation8.find(startP)+1:Green_Regulation8.find(EndP)]
        Hole9 = Hole9[Hole9.find(startP)+1:Hole9.find(EndP)]
        Par9 = Par9[Par9.find(startP)+1:Par9.find(EndP)]
        Stroke_Index9 = Stroke_Index9[Stroke_Index9.find(startP)+1:Stroke_Index9.find(EndP)]
        Gross_Score9 = Gross_Score9[Gross_Score9.find(startP)+1:Gross_Score9.find(EndP)]
        Points9 = Points9[Points9.find(startP)+1:Points9.find(EndP)]
        Putts9 = Putts9[Putts9.find(startP)+1:Putts9.find(EndP)]
        Fairway9 = Fairway9[Fairway9.find(startP)+1:Fairway9.find(EndP)]
        Ferret9 = Ferret9[Ferret9.find(startP)+1:Ferret9.find(EndP)]
        Green_Regulation9 = Green_Regulation9[Green_Regulation9.find(startP)+1:Green_Regulation9.find(EndP)]
        Hole10 = Hole10[Hole10.find(startP)+1:Hole10.find(EndP)]
        Par10 = Par10[Par10.find(startP)+1:Par10.find(EndP)]
        Stroke_Index10 = Stroke_Index10[Stroke_Index10.find(startP)+1:Stroke_Index10.find(EndP)]
        Gross_Score10 = Gross_Score10[Gross_Score10.find(startP)+1:Gross_Score10.find(EndP)]
        Points10 = Points10[Points10.find(startP)+1:Points10.find(EndP)]
        Putts10 = Putts10[Putts10.find(startP)+1:Putts10.find(EndP)]
        Fairway10 = Fairway10[Fairway10.find(startP)+1:Fairway10.find(EndP)]
        Ferret10 = Ferret10[Ferret10.find(startP)+1:Ferret10.find(EndP)]
        Green_Regulation10 = Green_Regulation10[Green_Regulation10.find(startP)+1:Green_Regulation10.find(EndP)]
        Hole11 = Hole11[Hole11.find(startP)+1:Hole11.find(EndP)]
        Par11 = Par11[Par11.find(startP)+1:Par11.find(EndP)]
        Stroke_Index11 = Stroke_Index11[Stroke_Index11.find(startP)+1:Stroke_Index11.find(EndP)]
        Gross_Score11 = Gross_Score11[Gross_Score11.find(startP)+1:Gross_Score11.find(EndP)]
        Points11 = Points11[Points11.find(startP)+1:Points11.find(EndP)]
        Putts11 = Putts11[Putts11.find(startP)+1:Putts11.find(EndP)]
        Fairway11 = Fairway11[Fairway11.find(startP)+1:Fairway11.find(EndP)]
        Ferret11 = Ferret11[Ferret11.find(startP)+1:Ferret11.find(EndP)]
        Green_Regulation11 = Green_Regulation11[Green_Regulation11.find(startP)+1:Green_Regulation11.find(EndP)]
        Hole12 = Hole12[Hole12.find(startP)+1:Hole12.find(EndP)]
        Par12 = Par12[Par12.find(startP)+1:Par12.find(EndP)]
        Stroke_Index12 = Stroke_Index12[Stroke_Index12.find(startP)+1:Stroke_Index12.find(EndP)]
        Gross_Score12 = Gross_Score12[Gross_Score12.find(startP)+1:Gross_Score12.find(EndP)]
        Points12 = Points12[Points12.find(startP)+1:Points12.find(EndP)]
        Putts12 = Putts12[Putts12.find(startP)+1:Putts12.find(EndP)]
        Fairway12 = Fairway12[Fairway12.find(startP)+1:Fairway12.find(EndP)]
        Ferret12 = Ferret12[Ferret12.find(startP)+1:Ferret12.find(EndP)]
        Green_Regulation12 = Green_Regulation12[Green_Regulation12.find(startP)+1:Green_Regulation12.find(EndP)]
        Hole13 = Hole13[Hole13.find(startP)+1:Hole13.find(EndP)]
        Par13 = Par13[Par13.find(startP)+1:Par13.find(EndP)]
        Stroke_Index13 = Stroke_Index13[Stroke_Index13.find(startP)+1:Stroke_Index13.find(EndP)]
        Gross_Score13 = Gross_Score13[Gross_Score13.find(startP)+1:Gross_Score13.find(EndP)]
        Points13 = Points13[Points13.find(startP)+1:Points13.find(EndP)]
        Putts13 = Putts13[Putts13.find(startP)+1:Putts13.find(EndP)]
        Fairway13 = Fairway13[Fairway13.find(startP)+1:Fairway13.find(EndP)]
        Ferret13 = Ferret13[Ferret13.find(startP)+1:Ferret13.find(EndP)]
        Green_Regulation13 = Green_Regulation13[Green_Regulation13.find(startP)+1:Green_Regulation13.find(EndP)]
        Hole14 = Hole14[Hole14.find(startP)+1:Hole14.find(EndP)]
        Par14 = Par14[Par14.find(startP)+1:Par14.find(EndP)]
        Stroke_Index14 = Stroke_Index14[Stroke_Index14.find(startP)+1:Stroke_Index14.find(EndP)]
        Gross_Score14 = Gross_Score14[Gross_Score14.find(startP)+1:Gross_Score14.find(EndP)]
        Points14 = Points14[Points14.find(startP)+1:Points14.find(EndP)]
        Putts14 = Putts14[Putts14.find(startP)+1:Putts14.find(EndP)]
        Fairway14 = Fairway14[Fairway14.find(startP)+1:Fairway14.find(EndP)]
        Ferret14 = Ferret14[Ferret14.find(startP)+1:Ferret14.find(EndP)]
        Green_Regulation14 = Green_Regulation14[Green_Regulation14.find(startP)+1:Green_Regulation14.find(EndP)]
        Hole15 = Hole15[Hole15.find(startP)+1:Hole15.find(EndP)]
        Par15 = Par15[Par15.find(startP)+1:Par15.find(EndP)]
        Stroke_Index15 = Stroke_Index15[Stroke_Index15.find(startP)+1:Stroke_Index15.find(EndP)]
        Gross_Score15 = Gross_Score15[Gross_Score15.find(startP)+1:Gross_Score15.find(EndP)]
        Points15 = Points15[Points15.find(startP)+1:Points15.find(EndP)]
        Putts15 = Putts15[Putts15.find(startP)+1:Putts15.find(EndP)]
        Fairway15 = Fairway15[Fairway15.find(startP)+1:Fairway15.find(EndP)]
        Ferret15 = Ferret15[Ferret15.find(startP)+1:Ferret15.find(EndP)]
        Green_Regulation15 = Green_Regulation15[Green_Regulation15.find(startP)+1:Green_Regulation15.find(EndP)]
        Hole16 = Hole16[Hole16.find(startP)+1:Hole16.find(EndP)]
        Par16 = Par16[Par16.find(startP)+1:Par16.find(EndP)]
        Stroke_Index16 = Stroke_Index16[Stroke_Index16.find(startP)+1:Stroke_Index16.find(EndP)]
        Gross_Score16 = Gross_Score16[Gross_Score16.find(startP)+1:Gross_Score16.find(EndP)]
        Points16 = Points16[Points16.find(startP)+1:Points16.find(EndP)]
        Putts16 = Putts16[Putts16.find(startP)+1:Putts16.find(EndP)]
        Fairway16 = Fairway16[Fairway16.find(startP)+1:Fairway16.find(EndP)]
        Ferret16 = Ferret16[Ferret16.find(startP)+1:Ferret16.find(EndP)]
        Green_Regulation16 = Green_Regulation16[Green_Regulation16.find(startP)+1:Green_Regulation16.find(EndP)]
        Hole17 = Hole17[Hole17.find(startP)+1:Hole17.find(EndP)]
        Par17 = Par17[Par17.find(startP)+1:Par17.find(EndP)]
        Stroke_Index17 = Stroke_Index17[Stroke_Index17.find(startP)+1:Stroke_Index17.find(EndP)]
        Gross_Score17 = Gross_Score17[Gross_Score17.find(startP)+1:Gross_Score17.find(EndP)]
        Points17 = Points17[Points17.find(startP)+1:Points17.find(EndP)]
        Putts17 = Putts17[Putts17.find(startP)+1:Putts17.find(EndP)]
        Fairway17 = Fairway17[Fairway17.find(startP)+1:Fairway17.find(EndP)]
        Ferret17 = Ferret17[Ferret17.find(startP)+1:Ferret17.find(EndP)]
        Green_Regulation17 = Green_Regulation17[Green_Regulation17.find(startP)+1:Green_Regulation17.find(EndP)]
        Hole18 = Hole18[Hole18.find(startP)+1:Hole18.find(EndP)]
        Par18 = Par18[Par18.find(startP)+1:Par18.find(EndP)]
        Stroke_Index18 = Stroke_Index18[Stroke_Index18.find(startP)+1:Stroke_Index18.find(EndP)]
        Gross_Score18 = Gross_Score18[Gross_Score18.find(startP)+1:Gross_Score18.find(EndP)]
        Points18 = Points18[Points18.find(startP)+1:Points18.find(EndP)]
        Putts18 = Putts18[Putts18.find(startP)+1:Putts18.find(EndP)]
        Fairway18 = Fairway18[Fairway18.find(startP)+1:Fairway18.find(EndP)]
        Ferret18 = Ferret18[Ferret18.find(startP)+1:Ferret18.find(EndP)]
        Green_Regulation18 = Green_Regulation18[Green_Regulation18.find(startP)+1:Green_Regulation18.find(EndP)]
        Totals = Totals[Totals.find(startP)+1:Totals.find(EndP)]
        Tpar = Tpar[Tpar.find(startP)+1:Tpar.find(EndP)]
        TGS = TGS[TGS.find(startP)+1:TGS.find(EndP)]
        TPO = TPO[TPO.find(startP)+1:TPO.find(EndP)]
        TPUT = TPUT[TPUT.find(startP)+1:TPUT.find(EndP)]
        TFW = TFW[TFW.find(startP)+1:TFW.find(EndP)]
        TF = TF[TF.find(startP)+1:TF.find(EndP)]
        TGR = TGR[TGR.find(startP)+1:TGR.find(EndP)]

# Remove any &nbsp string and replace with 0
        if(Season=='&nbsp;'): Season = 0
        if(Player=='&nbsp;'): Player = 0
        if(Club=='&nbsp;'): Club = 0
        if(Par_SS=='&nbsp;'): Par_SS = 0
        if(Num_Fairways=='&nbsp;'): Num_Fairways = 0
        if(Pdate=='&nbsp;'): Pdate = 0
        if(Playing_Handicap=='&nbsp;'): Playing_Handicap = 0
        if(Handicap=='&nbsp;'): Handicap = 0
        if(Event_Place=='&nbsp;'): Event_Place = 0
        if(Major=='&nbsp;'): 
            Major = ' ' 
        else: Major ='Major'
        if(Prize_Money=='&nbsp;'): Prize_Money = 0
        if(DB_Plus=='&nbsp;'): DB_Plus = 0
        if(DB=='&nbsp;'): DB = 0
        if(Bi=='&nbsp;'): Bi = 0
        if(P=='&nbsp;'): P = 0
        if(B=='&nbsp;'): B = 0
        if(E=='&nbsp;'): E = 0
        if(A=='&nbsp;'): A = 0
        if(H1=='&nbsp;'): H1 = 0
        if(Hole1=='&nbsp;'): Hole1 = 0
        if(Par1=='&nbsp;'): Par1 = 0
        if(Stroke_Index1=='&nbsp;'): Stroke_Index1 = 0
        if(Gross_Score1=='&nbsp;'): Gross_Score1 = 0
        if(Points1=='&nbsp;'): Points1 = 0
        if(Putts1=='&nbsp;'): Putts1 = 0
        if(Fairway1=='&nbsp;'): Fairway1 = 0
        if(Ferret1=='&nbsp;'): Ferret1 = 0
        if(Green_Regulation1=='&nbsp;'): Green_Regulation1 = 0
        if(Hole2=='&nbsp;'): Hole2 = 0
        if(Par2=='&nbsp;'): Par2 = 0
        if(Stroke_Index2=='&nbsp;'): Stroke_Index2 = 0
        if(Gross_Score2=='&nbsp;'): Gross_Score2 = 0
        if(Points2=='&nbsp;'): Points2 = 0
        if(Putts2=='&nbsp;'): Putts2 = 0
        if(Fairway2=='&nbsp;'): Fairway2 = 0
        if(Ferret2=='&nbsp;'): Ferret2 = 0
        if(Green_Regulation2=='&nbsp;'): Green_Regulation2 = 0
        if(Hole3=='&nbsp;'): Hole3 = 0
        if(Par3=='&nbsp;'): Par3 = 0
        if(Stroke_Index3=='&nbsp;'): Stroke_Index3 = 0
        if(Gross_Score3=='&nbsp;'): Gross_Score3 = 0
        if(Points3=='&nbsp;'): Points3 = 0
        if(Putts3=='&nbsp;'): Putts3 = 0
        if(Fairway3=='&nbsp;'): Fairway3 = 0
        if(Ferret3=='&nbsp;'): Ferret3 = 0
        if(Green_Regulation3=='&nbsp;'): Green_Regulation3 = 0
        if(Hole4=='&nbsp;'): Hole4 = 0
        if(Par4=='&nbsp;'): Par4 = 0
        if(Stroke_Index4=='&nbsp;'): Stroke_Index4 = 0
        if(Gross_Score4=='&nbsp;'): Gross_Score4 = 0
        if(Points4=='&nbsp;'): Points4 = 0
        if(Putts4=='&nbsp;'): Putts4 = 0
        if(Fairway4=='&nbsp;'): Fairway4 = 0
        if(Ferret4=='&nbsp;'): Ferret4 = 0
        if(Green_Regulation4=='&nbsp;'): Green_Regulation4 = 0
        if(Hole5=='&nbsp;'): Hole5 = 0
        if(Par5=='&nbsp;'): Par5 = 0
        if(Stroke_Index5=='&nbsp;'): Stroke_Index5 = 0
        if(Gross_Score5=='&nbsp;'): Gross_Score5 = 0
        if(Points5=='&nbsp;'): Points5 = 0
        if(Putts5=='&nbsp;'): Putts5 = 0
        if(Fairway5=='&nbsp;'): Fairway5 = 0
        if(Ferret5=='&nbsp;'): Ferret5 = 0
        if(Green_Regulation5=='&nbsp;'): Green_Regulation5 = 0
        if(Hole6=='&nbsp;'): Hole6 = 0
        if(Par6=='&nbsp;'): Par6 = 0
        if(Stroke_Index6=='&nbsp;'): Stroke_Index6 = 0
        if(Gross_Score6=='&nbsp;'): Gross_Score6 = 0
        if(Points6=='&nbsp;'): Points6 = 0
        if(Putts6=='&nbsp;'): Putts6 = 0
        if(Fairway6=='&nbsp;'): Fairway6 = 0
        if(Ferret6=='&nbsp;'): Ferret6 = 0
        if(Green_Regulation6=='&nbsp;'): Green_Regulation6 = 0
        if(Hole7=='&nbsp;'): Hole7 = 0
        if(Par7=='&nbsp;'): Par7 = 0
        if(Stroke_Index7=='&nbsp;'): Stroke_Index7 = 0
        if(Gross_Score7=='&nbsp;'): Gross_Score7 = 0
        if(Points7=='&nbsp;'): Points7 = 0
        if(Putts7=='&nbsp;'): Putts7 = 0
        if(Fairway7=='&nbsp;'): Fairway7 = 0
        if(Ferret7=='&nbsp;'): Ferret7 = 0
        if(Green_Regulation7=='&nbsp;'): Green_Regulation7 = 0
        if(Hole8=='&nbsp;'): Hole8 = 0
        if(Par8=='&nbsp;'): Par8 = 0
        if(Stroke_Index8=='&nbsp;'): Stroke_Index8 = 0
        if(Gross_Score8=='&nbsp;'): Gross_Score8 = 0
        if(Points8=='&nbsp;'): Points8 = 0
        if(Putts8=='&nbsp;'): Putts8 = 0
        if(Fairway8=='&nbsp;'): Fairway8 = 0
        if(Ferret8=='&nbsp;'): Ferret8 = 0
        if(Green_Regulation8=='&nbsp;'): Green_Regulation8 = 0
        if(Hole9=='&nbsp;'): Hole9 = 0
        if(Par9=='&nbsp;'): Par9 = 0
        if(Stroke_Index9=='&nbsp;'): Stroke_Index9 = 0
        if(Gross_Score9=='&nbsp;'): Gross_Score9 = 0
        if(Points9=='&nbsp;'): Points9 = 0
        if(Putts9=='&nbsp;'): Putts9 = 0
        if(Fairway9=='&nbsp;'): Fairway9 = 0
        if(Ferret9=='&nbsp;'): Ferret9 = 0
        if(Green_Regulation9=='&nbsp;'): Green_Regulation9 = 0
        if(Hole10=='&nbsp;'): Hole10 = 0
        if(Par10=='&nbsp;'): Par10 = 0
        if(Stroke_Index10=='&nbsp;'): Stroke_Index10 = 0
        if(Gross_Score10=='&nbsp;'): Gross_Score10 = 0
        if(Points10=='&nbsp;'): Points10 = 0
        if(Putts10=='&nbsp;'): Putts10 = 0
        if(Fairway10=='&nbsp;'): Fairway10 = 0
        if(Ferret10=='&nbsp;'): Ferret10 = 0
        if(Green_Regulation10=='&nbsp;'): Green_Regulation10 = 0
        if(Hole11=='&nbsp;'): Hole11 = 0
        if(Par11=='&nbsp;'): Par11 = 0
        if(Stroke_Index11=='&nbsp;'): Stroke_Index11 = 0
        if(Gross_Score11=='&nbsp;'): Gross_Score11 = 0
        if(Points11=='&nbsp;'): Points11 = 0
        if(Putts11=='&nbsp;'): Putts11 = 0
        if(Fairway11=='&nbsp;'): Fairway11 = 0
        if(Ferret11=='&nbsp;'): Ferret11 = 0
        if(Green_Regulation11=='&nbsp;'): Green_Regulation11 = 0
        if(Hole12=='&nbsp;'): Hole12 = 0
        if(Par12=='&nbsp;'): Par12 = 0
        if(Stroke_Index12=='&nbsp;'): Stroke_Index12 = 0
        if(Gross_Score12=='&nbsp;'): Gross_Score12 = 0
        if(Points12=='&nbsp;'): Points12 = 0
        if(Putts12=='&nbsp;'): Putts12 = 0
        if(Fairway12=='&nbsp;'): Fairway12 = 0
        if(Ferret12=='&nbsp;'): Ferret12 = 0
        if(Green_Regulation12=='&nbsp;'): Green_Regulation12 = 0
        if(Hole13=='&nbsp;'): Hole13 = 0
        if(Par13=='&nbsp;'): Par13 = 0
        if(Stroke_Index13=='&nbsp;'): Stroke_Index13 = 0
        if(Gross_Score13=='&nbsp;'): Gross_Score13 = 0
        if(Points13=='&nbsp;'): Points13 = 0
        if(Putts13=='&nbsp;'): Putts13 = 0
        if(Fairway13=='&nbsp;'): Fairway13 = 0
        if(Ferret13=='&nbsp;'): Ferret13 = 0
        if(Green_Regulation13=='&nbsp;'): Green_Regulation13 = 0
        if(Hole14=='&nbsp;'): Hole14 = 0
        if(Par14=='&nbsp;'): Par14 = 0
        if(Stroke_Index14=='&nbsp;'): Stroke_Index14 = 0
        if(Gross_Score14=='&nbsp;'): Gross_Score14 = 0
        if(Points14=='&nbsp;'): Points14 = 0
        if(Putts14=='&nbsp;'): Putts14 = 0
        if(Fairway14=='&nbsp;'): Fairway14 = 0
        if(Ferret14=='&nbsp;'): Ferret14 = 0
        if(Green_Regulation14=='&nbsp;'): Green_Regulation14 = 0
        if(Hole15=='&nbsp;'): Hole15 = 0
        if(Par15=='&nbsp;'): Par15 = 0
        if(Stroke_Index15=='&nbsp;'): Stroke_Index15 = 0
        if(Gross_Score15=='&nbsp;'): Gross_Score15 = 0
        if(Points15=='&nbsp;'): Points15 = 0
        if(Putts15=='&nbsp;'): Putts15 = 0
        if(Fairway15=='&nbsp;'): Fairway15 = 0
        if(Ferret15=='&nbsp;'): Ferret15 = 0
        if(Green_Regulation15=='&nbsp;'): Green_Regulation15 = 0
        if(Hole16=='&nbsp;'): Hole16 = 0
        if(Par16=='&nbsp;'): Par16 = 0
        if(Stroke_Index16=='&nbsp;'): Stroke_Index16 = 0
        if(Gross_Score16=='&nbsp;'): Gross_Score16 = 0
        if(Points16=='&nbsp;'): Points16 = 0
        if(Putts16=='&nbsp;'): Putts16 = 0
        if(Fairway16=='&nbsp;'): Fairway16 = 0
        if(Ferret16=='&nbsp;'): Ferret16 = 0
        if(Green_Regulation16=='&nbsp;'): Green_Regulation16 = 0
        if(Hole17=='&nbsp;'): Hole17 = 0
        if(Par17=='&nbsp;'): Par17 = 0
        if(Stroke_Index17=='&nbsp;'): Stroke_Index17 = 0
        if(Gross_Score17=='&nbsp;'): Gross_Score17 = 0
        if(Points17=='&nbsp;'): Points17 = 0
        if(Putts17=='&nbsp;'): Putts17 = 0
        if(Fairway17=='&nbsp;'): Fairway17 = 0
        if(Ferret17=='&nbsp;'): Ferret17 = 0
        if(Green_Regulation17=='&nbsp;'): Green_Regulation17 = 0
        if(Hole18=='&nbsp;'): Hole18 = 0
        if(Par18=='&nbsp;'): Par18 = 0
        if(Stroke_Index18=='&nbsp;'): Stroke_Index18 = 0
        if(Gross_Score18=='&nbsp;'): Gross_Score18 = 0
        if(Points18=='&nbsp;'): Points18 = 0
        if(Putts18=='&nbsp;'): Putts18 = 0
        if(Fairway18=='&nbsp;'): Fairway18 = 0
        if(Ferret18=='&nbsp;'): Ferret18 = 0
        if(Green_Regulation18=='&nbsp;'): Green_Regulation18 = 0
        if(Totals=='&nbsp;'): Totals = 0
        if(Tpar=='&nbsp;'): Tpar = 0
        if(TGS=='&nbsp;'): TGS = 0
        if(TPO=='&nbsp;'): TPO = 0
        if(TPUT=='&nbsp;'): TPUT = 0
        if(TFW=='&nbsp;'): TFW = 0
        if(TF=='&nbsp;'): TF = 0
        if(TGR=='&nbsp;'): TGR = 0


        print(Par1)
        # make up lists for each hole.
        Hole = ['Hole',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,"Totals"]
        Par = ['Par',int(Par1),int(Par2),int(Par3),int(Par4),int(Par5),int(Par6),int(Par7),int(Par8),int(Par9),int(Par10),int(Par11),int(Par12),int(Par13),int(Par14),int(Par15),int(Par16),int(Par17),int(Par18),int(Tpar)]
        Stroke_Index = ['Stroke\nIndex',int(Stroke_Index1),int(Stroke_Index2),int(Stroke_Index3),int(Stroke_Index4),int(Stroke_Index5),int(Stroke_Index6),int(Stroke_Index7),int(Stroke_Index8),int(Stroke_Index9),int(Stroke_Index10),int(Stroke_Index11),int(Stroke_Index12),int(Stroke_Index13),int(Stroke_Index14),int(Stroke_Index15),int(Stroke_Index16),int(Stroke_Index17),int(Stroke_Index18),'']
        Gross_Score = ['Gross\nScore',int(Gross_Score1),int(Gross_Score2),int(Gross_Score3),int(Gross_Score4),int(Gross_Score5),int(Gross_Score6),int(Gross_Score7),int(Gross_Score8),int(Gross_Score9),int(Gross_Score10),int(Gross_Score11),int(Gross_Score12),int(Gross_Score13),int(Gross_Score14),int(Gross_Score15),int(Gross_Score16),int(Gross_Score17),int(Gross_Score18),int(TGS)]
        Points = ['Points',int(Points1),int(Points2),int(Points3),int(Points4),int(Points5),int(Points6),int(Points7),int(Points8),int(Points9),int(Points10),int(Points11),int(Points12),int(Points13),int(Points14),int(Points15),int(Points16),int(Points17),int(Points18),int(TPO)]
        Putts = ['Putts',int(Putts1),int(Putts2),int(Putts3),int(Putts4),int(Putts5),int(Putts6),int(Putts7),int(Putts8),int(Putts9),int(Putts10),int(Putts11),int(Putts12),int(Putts13),int(Putts14),int(Putts15),int(Putts16),int(Putts17),int(Putts18),int(TPUT)]
        Fairways = ['Fairway',int(Fairway1),int(Fairway2),int(Fairway3),int(Fairway4),int(Fairway5),int(Fairway6),int(Fairway7),int(Fairway8),int(Fairway9),int(Fairway10),int(Fairway11),int(Fairway12),int(Fairway13),int(Fairway14),int(Fairway15),int(Fairway16),int(Fairway17),int(Fairway18),int(TFW)]
        Ferrets = ['Ferret',int(Ferret1),int(Ferret2),int(Ferret3),int(Ferret4),int(Ferret5),int(Ferret6),int(Ferret7),int(Ferret8),int(Ferret9),int(Ferret10),int(Ferret11),int(Ferret12),int(Ferret13),int(Ferret14),int(Ferret15),int(Ferret16),int(Ferret17),int(Ferret18),int(TF)]
        Green_Regulations = ['Greens in \nRegulation',Green_Regulation1,Green_Regulation2,Green_Regulation3,Green_Regulation4,Green_Regulation5,Green_Regulation6,Green_Regulation7,Green_Regulation8,Green_Regulation9,Green_Regulation10,Green_Regulation11,Green_Regulation12,Green_Regulation13,Green_Regulation14,Green_Regulation15,Green_Regulation16,Green_Regulation17,Green_Regulation18,TGR]


        # declare totals variables for each page. set counts to zero
        Totals = 'Totals'
        TPar = 0
        TStroke_Index = 0
        TGross_Score = 0
        TPoints = 0
        TPutts = 0
        TFairways = 0
        TFerrets = 0
        TGreen_Regulations =0

        # Use locally define function listsum() to count totals 
        TPar = listsum(Par)
        TStroke_Index = listsum(Stroke_Index)
        TGross_Score = listsum(Gross_Score)
        TPoints = listsum(Points)
        TPutts = listsum(Putts)
        TFairways = listsum(Fairways)
        TFerrets = listsum(Ferrets)

        op_line =list()
                

        print( TPar,TStroke_Index,TGross_Score,TPoints,TPutts,TFairways,TFerrets)
        #write out new HTML file
        melbagefile = open(EndPath+'/'+ConvertFileName,"wb")

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
        melbagefile.write( '<tr><td><h1>'+Player+'</h1></td><td><h1>'+Club+'</h1></td><td><h1>'+Pdate+'</h1></td><tr>');
        melbagefile.write( '<tr><td>'+'Playing Handicap <h1>'+Playing_Handicap+'</h1></td><td>'+'Par/SS <h1>'+Par_SS+'</h1></td><td>'+'Events Place <h1>'+Event_Place+Major+'</h1></td><tr>');
        melbagefile.write( '<tr><td>'+'Actual Handicap <h1>'+Handicap+'</h></td><td>''Number of Fairway <h1>'+Num_Fairways+'</h1></td><td> Prize Money <h1> &pound '+Prize_Money+'</h1></td><tr>');
        melbagefile.write( '</table>');

        melbagefile.write( '<br>');
        melbagefile.write( '<br>');
        melbagefile.write( '<table>');


        MarkUpOdd ='<tr class ="odd">'
        MarkUpEven = '<tr class ="even">'
        start ='<tr>'
        melbagefile.write( "<table>");
        hc =0
        for i in Hole:
            if hc == 0:
                start ='<tr>'
            elif hc % 2 ==0:
                start = MarkUpEven
            elif hc % 2 >0:
                start = MarkUpOdd
                
            op_line =  start+'<td>'+str(Hole[hc])+'</td><td>'+ str(Par[hc])+'</td><td>'+str(Stroke_Index[hc])+'</td><td>'+str(Gross_Score[hc])+'</td><td>'+str(Points[hc])+'</td><td>'+str(Putts[hc])+'</td><td>'+str(Fairways[hc])+'</td><td>'+str(Ferrets[hc])+'</td><td>'+str(Green_Regulations[hc])+'</td><tr>'
            melbagefile.write( op_line);
            hc = hc +1
            
        melbagefile.write( '</table>');
        melbagefile.write( '<br>');
        melbagefile.write( '<br>');

        # Write out the Stats out in a table of the bottom
        melbagefile.write( "<table>");
        melbagefile.write( '<tr><td>Double\n Bogey Plus</td><td>Double\n Bogey</td><td>Bogey</td><td>Par</td><td>Birdie</td><td>Eagle</td><td>Albatross</td><td>Condor</td><td>Hole in \nOne</td><tr>');
        melbagefile.write( '<tr><td>'+DB_Plus+'</td><td>'+DB+'</td><td>'+Bi+'</td><td>'+P+'</td><td>'+B+'</td><td>'+E+'</td><td>'+A+'</td><td>0</td><td>'+H1+'</td><tr>');
        melbagefile.write( '</table>');
        melbagefile.write( '</div>');
        melbagefile.write( '<br>');
        melbagefile.write( '	</body>');
        melbagefile.write( '</html>');

        melbagefile.close()

