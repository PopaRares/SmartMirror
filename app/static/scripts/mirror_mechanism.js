let isFace;
let open = false;
let data = {};

function toggleOpacity() {

    $.getJSON(
        "/getData",
        function (data) {
            isFace = data.isFace;
            if(isFace) {
                if(!open) {
                    open = true;
                    console.log("MIRROR POWERING UP");
                    $(document.body).animate({opacity: 1}, 1000);
                }
            } else {
                if(open){
                    open = false;
                    console.log("MIRROR SHUTTING DOWN");
                    $(document.body).animate({opacity: 0}, 1000);
                }
            }
        }
    );
}


function startTime() {
  var today = new Date();
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('clock').innerHTML =
  h + ":" + m + ":" + s;
}

function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}

function greet() {
  $.getJSON(
        "/getData",
        function (data) {
            var nume = data.name
            document.getElementById('greet').innerHTML = "Hello " + nume + "!";
        }
    );
}

function saveData(sharedData) {
    console.log(sharedData);
    data = sharedData;
}

function getData() {
  $.getJSON(
        "/getData",
        function (sharedData) {
            saveData(sharedData);
        }
    );
}

$(document).ready(setInterval(getData, 500));

$(document).ready(setInterval(toggleOpacity, 1000));
$(document).ready(setInterval(greet, 500));
$(document).ready(setInterval(startTime, 500));