// Bunch of function to help display the information on  months page

// function CheckURL() {
//     var selectedMonth = GetURLParameter("selectedMonth");
//     if (selectedMonth) {
//         DisplayRows(selectedMonth); 
//         console.log(selectedMonth)
//     }
// });

// function GetURLParameter(sParam)
// {
//     var sPageURL = window.location.search.substring(1);
//     console.log(sPageURL)
//     var sURLVariables = sPageURL.split('&');
//     for (var i = 0; i < sURLVariables.length; i++)
//     {
//         var sParameterName = sURLVariables[i].split('=');
//         if (sParameterName[0] == sParam)
//         {
//             return sParameterName[1];
//         }
//     }
// }
// const ChangeMonth = document.querySelector("Month-select");
const ChangeMonth = document.getElementById("Month-select");
console.log(`${ChangeMonth.value}`, "bib")
ChangeMonth.addEventListener("change", (event) => {
    //   console.log(${event.target.value} )
      UpdateDisplayType(event.target.value )
   
    });




// function DisplayRows(DisplayType) {
//     // don't display any rows
//     Array.from(document.getElementsByClassName("performanceScore")).forEach(
//         function(el){
//             el.style.display = 'none'
//         }
//         );
    // Array.from(document.getElementsByClassName("performanceStokes")).forEach(
    //     function(el){
    //         el.style.display = 'none'
//         }
//         );
//     Array.from(document.getElementsByClassName("performancePutts")).forEach(
//         function(el){
//             el.style.display = 'none'
//         }
        // );
    // document.getElementsByClassName(".performanceScore").style='display:none;';
    // document.getElementsByClassName(".performanceStokes").style='display:none;';
    // document.getElementsByClassName(".performancePutts").style='display:none;';
    // Display only the ones from the button
//    var DisplayRowsStyle =document.getElementsByClassName(DisplayType);
//    console.log(DisplayType,DisplayRowsStyle)
   //loop in array and change each  rows style
//    Array.from(DisplayRowsStyle).forEach(
//     function(el){
//         el.style.display = 'table-row'
//     }
//    )
//    DisplayRowsStyle.forEach(e => e.style.display = "contents");
//    DisplayRowsStyle.style.display = 'table-row';
//    DisplayRowsStyle.style.display = 'revert';
//    console.log(DisplayType,DisplayRowsStyle.display, DisplayRowsStyle)
//    subRow.style.display = subRow.style.display === 'none' ? 'table-row' : 'none';    

//   }
//   Array.from(document.getElementsByClassName("myclass")).forEach(
//     function(element, index, array) {
//         // do stuff
//     }
// );
var potentials = document.querySelectorAll("[class^=performancePutts]");
console.log(potentials.length);

  


    document.querySelectorAll("[class^=performanceP]").forEach(
    function(dontDisplay){
        dontDisplay.style.display = 'none'
    });
    document.querySelectorAll("[class^=performanceStokes]").forEach(
        function(dontDisplay){
            dontDisplay.style.display = 'none'
        });



function UpdateDisplayType(DisplayIt ) {
    // const MonthsClass = ["performanceScore202301","performanceScore202302","performanceScore202303","performanceScore202204","performanceScore202205","performanceScore202206","performanceScore202207","performanceScore202208","performanceScore202209","performanceScore202210","performanceScore202211", "performanceScore202212"];
    // const MonthsClass1 = ChangeMonth.value()
    let selectElement = document.querySelectorAll('[name=Month-select]');
let MonthSelectValues = [...selectElement[0].options].map(o => o.value)
console.log(MonthSelectValues)
    // console.log(MonthsClass)
    // --MonthsClass.forEach(
        MonthSelectValues.forEach(
        function(cls){
            console.log(cls)
            Array.from(document.getElementsByClassName(cls)).forEach(
                function(el){
                el.style.display = 'none'
            });
        });
    
    Array.from(document.getElementsByClassName(DisplayIt)).forEach(
        function(el){
            el.style.display = 'table-row'
    Array.from(document.getElementsByClassName("performanceStokes")).forEach(
                function(el){
                    el.style.display = 'none'
        });
    });

}