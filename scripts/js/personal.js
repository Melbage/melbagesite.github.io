// $('.performanceScore').click(function() {
//     $(this).nextUntil('.performanceScore').toggle("slow");       
// });

function DisplayRows(DisplayType) {
    // don't display any rows
    Array.from(document.getElementsByClassName("performanceScore")).forEach(
        function(el){
            el.style.display = 'none'
        }
        );
    Array.from(document.getElementsByClassName("performanceStokes")).forEach(
        function(el){
            el.style.display = 'none'
        }
        );
    Array.from(document.getElementsByClassName("performancePutts")).forEach(
        function(el){
            el.style.display = 'none'
        }
        );
    // document.getElementsByClassName(".performanceScore").style='display:none;';
    // document.getElementsByClassName(".performanceStokes").style='display:none;';
    // document.getElementsByClassName(".performancePutts").style='display:none;';
    // Display only the ones from the button
   var DisplayRowsStyle =document.getElementsByClassName(DisplayType);
   console.log(DisplayType,DisplayRowsStyle)
   //loop in array and change each  rows style
   Array.from(DisplayRowsStyle).forEach(
    function(el){
        el.style.display = 'table-row'
    }
   )
//    DisplayRowsStyle.forEach(e => e.style.display = "contents");
//    DisplayRowsStyle.style.display = 'table-row';
//    DisplayRowsStyle.style.display = 'revert';
   console.log(DisplayType,DisplayRowsStyle.display, DisplayRowsStyle)
//    subRow.style.display = subRow.style.display === 'none' ? 'table-row' : 'none';    

  }
//   Array.from(document.getElementsByClassName("myclass")).forEach(
//     function(element, index, array) {
//         // do stuff
//     }
// );
function UpdateDisplayType(DisplayIt, DonotDisplayit1, DonotDisplayit2 ) {
    Array.from(document.getElementsByClassName(DisplayIt)).forEach(
        function(el){
            el.style.display = 'table-row'
        }
        );
    Array.from(document.getElementsByClassName(DonotDisplayit1)).forEach(
        function(el){
            el.style.display = 'none'
        }
        );
    Array.from(document.getElementsByClassName(DonotDisplayit2)).forEach(
        function(el){
            el.style.display = 'none'
        }
        );
    };