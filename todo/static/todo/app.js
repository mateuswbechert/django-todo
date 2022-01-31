// Ajax cardView
function cardView(str) {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
      document.getElementById("loadView").innerHTML = 
      this.responseText;
    }
    xhttp.open("GET", "view/"+str);
    xhttp.send();
  }