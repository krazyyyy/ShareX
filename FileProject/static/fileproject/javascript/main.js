

function Search() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tablerow = document.getElementsByClassName("files-table-row");
    tr = table.getElementsByClassName("search_cells");
    for (i = 0; i < tr.length; i++) {
      
      td = tr[i];
      if (td.innerHTML) {
        txtValue = td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tablerow[i].style.display = "";
        } else {
          tablerow[i].style.display = "none";
        }
      }       
    }
  }


  var up = document.querySelector('#uploadSection')
  var allfiles = document.querySelector('#allFiles')
  var uploads_icon = document.querySelector('#uploads')
  var page_icon = document.querySelector('#page')
  uploads_icon.onclick = function () {
      if (up.classList.contains('deactive')) {
          up.classList.remove('deactive')
      }
      allfiles.classList.add('deactive')
      up.classList.add('active')
      
  }

  page_icon.onclick = function () {
      if (allfiles.classList.contains('deactive')) {
          allfiles.classList.remove('deactive')
      }
      up.classList.add('deactive')
      allfiles.classList.add('active')
  }

  var show = document.querySelector('#show_left')
  var hide = document.querySelector('#hide_left')
  var left = document.querySelector('.left-area')
  show.onclick = function () {
    left.classList.add('show_bar')
  }
  hide.onclick = function () {
    left.classList.remove('show_bar')
  }
  