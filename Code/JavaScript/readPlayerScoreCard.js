//reads in the HTLM tag for the scorecard and assign it to a variable
var ScoreCardTable = document.getElementById("ScoreCard");

//Read the JSON format ScoreCard from files system
var ourRequest = new XMLHttpRequest();
ourRequest.open('GET','https://melbage.github.io/melbagesite.github.io/Code/JSON/Data/ExampleSc.json');
ourRequest.onload = function(){
    //Read the file in and assin it to a JSON format
    var ourData=JSON.parse(ourRequest.responseText);
    //User a function to create the HTML code to display the table
    renderHTML(ourData);
    //console.log(ourDate.Player.PlayerName,ourDate.Player.BeforeHandicap);
};
ourRequest.send();

function renderHTML(SCData){
  var ScoreCardTable = document.getElementById("ScoreCard");
  //set a HTMLString as the returned data
  console.log(SCData.Player.PlayerName);
  var HTMLString = "";
  //HTMLString += "<p>"+ SCData.Player.PlayerName + "</p>";
  //place the name at the top of the page.
  HTMLString += '<tbody>';
  HTMLString += '<tr height=25 style="height:18.75pt;width:50%;text-align:center">';
  HTMLString += '<td>'+ SCData.Player.PlayerName + '</td></tr>';
  HTMLString += '</tbody>';
  //write the data to HMTL page
  //ScoreCardTable.insertAdjacentHTML('beforeend', HTMLString);
  console.log(HTMLString);
  ScoreCardTable.insertAdjacentHTML('beforeend',HTMLString);

};
