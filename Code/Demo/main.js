var ourRequest = new XMLHttpRequest();
ourRequest.open('GET','https://melbage.github.io/melbagesite.github.io//Code/JSON/Data/ExampleSc.json');
//ourRequest.open('GET','https://learnwebcode.github.io/json-example/animals-1.json');
ourRequest.onload = function(){
    var ourDate=JSON.parse(ourRequest.responseText);
    console.log(ourDate.Player.PlayerName,ourDate.Player.BeforeHandicap);
};
ourRequest.send();


//ourRequest.open('GET','https://melbage.github.io/melbagesite.github.io//Code/JSON/Data/ExampleSc.json');