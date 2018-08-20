$( document ).ready(function() {
    var ser = $("#search").position();
    // console.log(ser);
    var inf = $("#info").position();
    // console.log(inf);
    var overOpac = 1000;
    var backOpac = 1000;
    var opac = 1;
    var slide = 350;
    var currentMid = -3;
    var movboxwid = $(".movBox").outerWidth();
    $("#movieLib").width(movboxwid*$("#movieLib").children().length);

    function movieto(movieId) {
        var move = $("#movieLib").position();
        if ($("#movieLib").is(":animated")) {
            return;
        }
        if (movieId == currentMid) {
            return;
        }

        $("#movieLib").animate({
            left: move.left - (movboxwid * (movieId)-(movboxwid * currentMid)) + "px"
        }, slide);

        $(".backdrop").each(function (index) {
            if (index == movieId) {
                $(this).fadeTo(backOpac, opac);
            } else {
                $(this).fadeOut(backOpac);
            }
            ;
        });
        $( '.poster' ).each(function( index ) {
            if (index == movieId) {
                $(this).addClass("posterOut");
                $(this).removeClass("posterTurnOut");
                $(this).removeClass("posterTurnIn");
            }else if (index == movieId+1)
            {
                $(this).addClass("posterTurnOut");
            }else if (index == movieId-1)
            {
                $(this).addClass("posterTurnIn");
            }else{
                $(this).removeClass("posterOut");
                $(this).removeClass("posterTurnOut");
                $(this).removeClass("posterTurnIn");
            };
        });
        currentMid = movieId;
        console.log("currentMid "+currentMid);
    }

    $(document).keydown(function(e) {
    // console.log(e);


    switch(e.which) {
        case 39:
            // LEFT
            movieto(currentMid+1);
            break;

            // RIGHT
            case 37:
            movieto(currentMid-1);
            break;

            // UP
            case 38:
                var ser = $("#search").position();
                if(ser.top==-50){
                    $("#search").animate({
                        top: ser.top = 0 + "px"
                    }, slide);
                }else{
                    $("#search").animate({
                        top: ser.top = -50 + "px"
                    }, slide);
                }

                var inf = $("#info").position();
                if(inf.top==720){
                    $("#info").animate({
                        top: inf.top = 670 + "px"
                    }, slide);
                }else{
                    $("#info").animate({
                        top: inf.top = 720 + "px"
                    }, slide);
                }
                $(".ui-menu").css("display", "none");
                $("#tags").val("");
                $( "#tags" ).focus();
            break;

            // ENTER
            case 13:
                // console.log($("#movieLib").outerWidth())
                if ($("#tags").val() == ""){
                    break;
                }else {
                    var ser = $("#search").position();
                    $("#search").animate({
                        top: ser.top = -50 + "px"
                    }, slide);
                    var inf = $("#info").position();
                    $("#info").animate({
                        top: inf.top = 720 + "px"
                    }, slide);


                    var box = $("#tags").val().replace(":", "").replace(/\s/g, "").replace(".", "");
                    // console.log(box);
                    var mid = ($("#" + box).position().left)/350;
                    // console.log("boxpos "+mid)
                    var move = ($("#movieLib").position());
                    // console.log("libpos "+move.left)
                    movieto(mid)
                    // $("#movieLib").animate({
                    //      left: move.left - (boxPos+1050) +"px"
                    // }, 1500);
                    $(".ui-menu").css("display", "none");
                    $("#tags").val("");
                };
            break;
            default: return;
        }
        e.preventDefault();
        });

});
