let isFace = 0

function toggleOpacity() {
    $.getJSON(
        "/getFace",
        function (data) {
            isFace = data.isFace;
            console.log(isFace)
            if(isFace) {
               $(document.body).animate({opacity: 1}, 1000);
            } else {
                $(document.body).animate({opacity: 0}, 1000);
            }
        }
    );
}

$(document).ready(setInterval(toggleOpacity, 2000));