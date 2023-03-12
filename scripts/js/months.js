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


function sortTable() {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("Months");
    switching = true;
    /*Make a loop that will continue until
    no switching has been done:*/
    while (switching) {
        //start by saying: no switching is done:
        switching = false;
        rows = table.rows;
        /*Loop through all table rows (except the
        first, which contains table headers):*/
        for (i = 1; i < (rows.length - 1); i++) {
        //start by saying there should be no switching:
        shouldSwitch = false;
        /*Get the two elements you want to compare,
        one from current row and one from the next:*/
        x = rows[i].getElementsByTagName("TD")[0];
        y = rows[i + 1].getElementsByTagName("TD")[0];
        //check if the two rows should switch place:
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
            //if so, mark as a switch and break the loop:
            shouldSwitch = true;
            break;
        }
        }
        if (shouldSwitch) {
        /*If a switch has been marked, make the switch
        and mark that a switch has been done:*/
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        }
    }
    }