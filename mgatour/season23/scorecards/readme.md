# ScoreCard folder

## Description:
This is were each score a player records is held and displayed. It is a simple one file to hold all score cards, which uses the id tags as a bookmark.

## Prerequisites:
Each player must have a scorecard html file. The file name is SC_ then the sheet name(tab) of the player in the season spreaadsheet. If a play does not have a file them copy the SC_Blank.html and change the filename, replace the word Blank with the players spreadsheet tab name. It is also wroth changing the title of the page. Replace the word Player with the spreadsheet tab name, between the title tags.

Before add a new score card to the scorecard file, please copy the last article and paste it in the next space before the <\body > tab. This ensure that there is always one available to paste into.  

## Method:
After the score has been added too the players tab with the Season spreadsheet (cells A11 to I37 example of 1st game), the speadsheet creates the HTML for  the scorecard in cells CU11 to CU37 (Scorecard_data). The top row is highlighted in blue. 
The Scorecard_data call be copied from the spreadsheet and pasted in to the players SC_(tab).html file, over the text which reads  <!- Place score data here ->


```html
<article>
    <table class="scorecard">
        <!-- Place score data here -->
    </table>
</article>
```
That it done. 

## HTML & CSS
The scorecard page is one page to hold all score cards for a season, inbedded in the caption tag is the id which referrences the unqic scorcard. All the CSS used to format teh page is .scorecard, It is based on the look of the old spreadsheet card. 




