let isFace;
let opacity;

function toggleOpacity() {
    $.getJSON(
        "/getFace",
        function (data) {
            isFace = data.isFace;
            opacity = $(document.body).css("opacity");
            if(isFace && opacity === 1) {
                console.log("[INFO] MIRROR POWERING UP");
               $(document.body).animate({opacity: 1}, 1000);
            }
            if(!isFace && opacity === 0){
                console.log("[INFO] MIRROR SHUTTING DOWN");
                $(document.body).animate({opacity: 0}, 1000);
            }
        }
    );
}

$(document).ready(setInterval(toggleOpacity, 1000));