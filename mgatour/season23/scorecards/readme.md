# ScoreCard folder

## Description

This is were each score a player records is held and displayed. It is a simple one file to hold all score cards, which uses the id attribute as a bookmark. 

## Prerequisites

Working understanding of Google sheets and how to copy and paste data.

## id attribute

The id attribute is used to specify a unique id for an HTML element. As the id for each rounds is also unique these make good sense to be the same. The format is [date including AM or PM - File Reference Name]. [File Reference Name] is the column "File Reference Name" in the handicap table in Handicap tab in Google sheets. Date format is YYYYMMDD. 

Example
```html
<caption id='20220404AM-JC' ><strong>Jeff Colbrook</strong> </caption>
```

## Method

Using Google sheets filter from row 13 on column Q (Q13) for any non blank. Then copy all the cell on display in column Q and paste them into a file SC_[File Reference Name].html. 
It is important to take all the column as the top row (1-12) are the HTML file header details.

## HTML & CSS

The scorecard page is one page to hold all score cards for a season, imbedded in the caption tag is the id which references the unique scorecard. All the CSS used to format the page is .scorecard class in the main.css file. It's formatting is  is based on the look of the old spreadsheet card.

[Back](../../season23/readme.md)

