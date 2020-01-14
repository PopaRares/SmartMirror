let isFace;
let open = false;
let data = {};

function toggleOpacity() {

    isFace = data.isFace;
    if (isFace) {
        if (!open) {
            open = true;
            console.log("MIRROR POWERING UP");
            $(document.body).animate({opacity: 1}, 1000);
        }
    } else {
        if (open) {
            open = false;
            console.log("MIRROR SHUTTING DOWN");
            $(document.body).animate({opacity: 0}, 1000);
        }
    }
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
    if (i < 10) {
        i = "0" + i;
    }// add zero in front of numbers < 10
    return i;
}

function greet() {
    document.getElementById('greet').innerHTML = "Hello " + data.name + "!";
}

function saveData(sharedData) {
    console.log(sharedData);
    data = sharedData;
    if(data.hasOwnProperty("weather_forecast")) {
        updateWeatherOnScreen();
    }
}

function getData() {
    $.getJSON(
        "/data",
        function (sharedData) {
            saveData(sharedData);
        }
    );
}

function updateWeatherOnScreen() {
    var temperature = data.weather_now[0].Temperature.Metric.Value;
    var weatherText = data.weather_now[0].WeatherText;
    var precipitation = data.weather_now[0].PrecipitationType;

    var finalText = '<h2>' + weatherText + ', ' + temperature + 'C°' + '</h2>';

    if(precipitation !== null) finalText += '<h2>It is ' + precipitation + '.';
    if(temperature < 10) finalText += '<h2>Wear a jacket!</h2>';

    finalText += "<ul>";
    forecast = data.weather_forecast;
    var i;
    for (i = 2; i < forecast.length; i += 3) {
        finalText += "<li>";
        var date = new Date(forecast[i].DateTime);
        hours = ("0" + date.getHours()).slice(-2);
        finalText += "<p>" + hours + ":00</p>";
        finalText += "<p>" + forecast[i].IconPhrase + ", " + forecast[i].Temperature.Value +"C°</p>";
        finalText += "<p>Precipitation probability: " + forecast[i].PrecipitationProbability + "%</p>";

        finalText += "</li>";
    }
    finalText += "</ul>";

    document.getElementById('weather').innerHTML = finalText;
}

function updateWeatherData() {
    $.getJSON(
        "/weather",
        function (weatherResponse) {
                if(weatherResponse['update'] === 'SUCCESS') {
                    updateWeatherOnScreen();
                }
                console.log('Weather update: ' + weatherResponse['update']);
        }
    );
}

$(document).ready(setInterval(getData, 500));

$(document).ready(setInterval(toggleOpacity, 1000));
$(document).ready(setInterval(greet, 500));
$(document).ready(setInterval(startTime, 500));
$(document).ready(setInterval(updateWeatherData, 3600000));//one hour

$(document).ready(updateWeatherData);