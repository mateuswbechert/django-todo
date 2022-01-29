console.log("JS running")
// AJAX CALL
function cardView(str) {
    console.log("Function cardView")
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
      document.getElementById("loadView").innerHTML = 
      this.responseText;
    }
    xhttp.open("GET", "view/"+str);
    xhttp.send();
  }