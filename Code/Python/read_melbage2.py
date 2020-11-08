############################################################
# Program Name :     read_melbage2.py                       #
# Description                                              #
#   This file opens a excel created .htm file and find the #
# header statement                                         #
############################################################
# Version  Date     Author  Description                    #
#   0.1a   26Jan14  Pcarter	Creations of program.          #
#   0.2	   03Aug17	pcarter	Loaded code in VsCode to use a IDE                                                       #
#                                                          #
#                                                          #
#                                                          #
############################################################

#!/usr/bin/python
import time 
from datetime import date 
import sys
#use sys to read in file lines 

#define the variables 
# file name is the name of the file. Including path
file_name = "ab020405copy.htm"
open_file = open(file_name,"r")
head_line = open_file.readline()
#str I am looking for 
body_str = "<!--START OF OUTPUT FROM EXCEL PUBLISH AS WEB PAGE WIZARD"
lc = 0 # line counter
slc =0 # split line counter for loop
event_date =0
str_match = 0
Raw_line =0
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
from_here_on_in =0

#later I may look at charge directory and splitting the file_name and path_name 
# path_name =
# import os 
# os.chdir() the function
with open(file_name) as f:
	for i, Raw_line in enumerate(f):
		print "row number",i
    	if Raw_line.find(body_str) != -1:
    		from_here_on_in = i
    		print from_here_on_in
    	if  (from_here_on_in + 3)==i:
    		season = Raw_line 
    		print season
    	if (from_here_on_in + 17)==i:
			player = Raw_line 
			print player
		if (from_here_on_in + 23)==i:
			course_name = Raw_line 
			print course_name 
		if i == from_here_on_in +26:
			Par_lable = Raw_line 
			print Par_lable 
		if i == from_here_on_in +27:
			Par = Raw_line 
			print Par 
		if i == from_here_on_in +28:
			Fairway_lable = Raw_line 
			print Fairway_lable 
		if i == from_here_on_in +30:
			Fairway_Count = Raw_line 
			print Fairway_Count 
		if i == from_here_on_in +33:
			Date_lable = Raw_line 
			print Date_lable 
		if i == from_here_on_in +34:
			Played_Date = Raw_line 
			print Played_Date 
		if i == from_here_on_in +35:
			Handicap_Lable = Raw_line 
			print Handicap_Lable 
		if i == from_here_on_in +36:
			Handicap = Raw_line 
			print Handicap 
		
open_file.close() 	
		
print "season ",season 
print "player ",player 
print "course_name ",course_name 
print "Par_lable ",Par_lable 
print "Par ",Par 
print "Fairway_lable ",Fairway_lable 
print "Fairway_Count ",Fairway_Count 
print "Date_lable ",Date_lable 
print "Played_Date ",Played_Date 
print "Handicap_Lable ",Handicap_Lable 
print "Handicap ",Handicap 
    
'''		slc = 0
		print "Line number: %s is %s value %s" %(lc,head_line,len(head_line))
		
	Value = head_line
		startP = Value.find(">") + 1
		EndP = Value.find("</td>")
		RawVal1 = Value[startP:EndP]
		EndP = startP -2
		startP = Value.find(body_str)+7
		RawVal2 = Value[startP:EndP]
		
		print "RawVal1 =", RawVal1 
		print "RawVal2 =", RawVal2 
		
#		for value in head_line.split(">"):
#			print slc, value, len(value)
#			print head_line[57:10]
#			slc += 1
#			event_date = value[0:10]
#			if  time.strptime(event_date,"%d %m %Y"):
#				event_date = time.strptime(value[0:10],"%d %m %Y")
#				print " Event date : %d" %event_date	
		
p# rint " Event date : %s" %event_date		
'''

#open_file.close() 