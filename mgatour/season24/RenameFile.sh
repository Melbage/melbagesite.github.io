#!/bin/bash
# Processing stats pages
# Months
if [  -f ./'Season24 MGA Playing Rounds (Responses) - Months.csv'  ]
then
    echo "Rename Season24 MGA Playing Rounds (Responses) - Months.csv file to Months.html"
    mv ./'Season24 MGA Playing Rounds (Responses) - Months.csv' ./Months.html
else
    echo "No Months data file to process" 
fi
# TourStats
if [  -f ./'Season24 MGA Playing Rounds (Responses) - TourStats.csv'  ]
then
    echo "Rename Season24 MGA Playing Rounds (Responses) - TourStats.csv file to TourStats.html"
    mv ./'Season24 MGA Playing Rounds (Responses) - TourStats.csv' ./TourStats.html
else
    echo "No TourStats data file to process" 
fi
# Handicaps
if [  -f ./'Season24 MGA Playing Rounds (Responses) - Handicaps.csv'  ]
then
    echo "Rename Season24 MGA Playing Rounds (Responses) - Handicaps.csv file to Handicaps.html"
    mv ./'Season24 MGA Playing Rounds (Responses) - Handicaps.csv' ./Handicaps.html
    sed -i '' 's/"document/document/g' ./Handicaps.html
    sed -i '' 's/);"/);/g' ./Handicaps.html
else
    echo "No Handicaps data file to process" 
fi
# Processing player data
PlayersList=(PB PEC DAR ST KG JD RD JC DW DR ANB AB RT MC)
for i in "${PlayersList[@]}"
do
	# echo "$i"
    # echo "Season24 MGA Playing Rounds (Responses) - $i.csv "
    PersonalFileName="Season24 MGA Playing Rounds (Responses) - $i.csv"
    ScoreCardsFileName="Season24 MGA Playing Rounds (Responses) - $i (1).csv"
    if [ -f "$PersonalFileName" ]
    then    
        echo "Processing $PersonalFileName"
        grep -q "<title> ScoreCards</title>" "$PersonalFileName"
        HasTitleScoreCardSet=$?
        echo $HasTitleScoreCardSet
        if [ $HasTitleScoreCardSet -eq 0 ] 
        then 
            echo "processing $PersonalFileName as ScoreCard"
            mv "$PersonalFileName" "SC_$i.html"
            echo "</body>" >> ./SC_DR.html
            echo "</html>" >> ./SC_DR.html
        else
            grep "\S" "$PersonalFileName" > "$i.html"
            sed -i '' 's/"</</g' "$i.html"
            sed -i '' 's/>"/>/g' "$i.html"
            sed -i '' 's/""/"/g' "$i.html"
            echo "</tbody>" >> "$i.html"
            echo "</table>" >> "$i.html"
            echo "</body>" >> "$i.html"
            echo "</html>" >> "$i.html"
            rm "$PersonalFileName"
        fi
    else
        echo "No file $PersonalFileName "
    fi
    if [ -f "$ScoreCardsFileName" ]
    then    
        echo "Processing $ScoreCardsFileName"
        grep -q "<title> ScoreCards</title>" "$ScoreCardsFileName"
        HasTitleScoreCardSet=$?
        if [ $HasTitleScoreCardSet -eq 0 ] 
        then 
            echo "processing $PersonalFileName as ScoreCard"
            mv "$ScoreCardsFileName" "SC_$i.html"
            echo "</body>" >> ./SC_DR.html
            echo "</html>" >> ./SC_DR.html
        else
            grep "\S" "$ScoreCardsFileName" > "$i.html"
            sed -i '' 's/"</</g' "$i.html"
            sed -i '' 's/>"/>/g' "$i.html"
            sed -i '' 's/""/"/g' "$i.html"
            echo "</tbody>" >> "$i.html"
            echo "</table>" >> "$i.html"
            echo "</body>" >> "$i.html"
            echo "</html>" >> "$i.html"
            rm "$ScoreCardsFileName"
        fi
    else
        echo "No file Season24 MGA Playing Rounds (Responses) - $i (1).csv "
    fi
done