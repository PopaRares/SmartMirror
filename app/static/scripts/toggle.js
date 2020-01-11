let isFace;
let open = true;

function toggleOpacity() {

    $.getJSON(
        "/getFace",
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

$(document).ready(setInterval(toggleOpacity, 1000));