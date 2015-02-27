var projects =     {"1":["/static/img/zlm.png", "Zen License Manager, simple and easy to use license manager"],
                    "2":["/static/img/kit.png", "Landing page for Kit"],
                    "3":["/static/img/explore.png", "personal project, online travel book"],
                    "4":["/static/img/tikky.png", "personal project, ticket tracker"],
                    "5":["/static/img/battlefit.png", "Fitness battles among friends and peers"]
                    };
var source;
var description;

$('.project').mouseenter(function() {
    var id = (this.id);
    // get matching image source
    for (var key in projects) {
        if (key !== id) {
        } else {
            source = projects[key[0]];
            description = source[1];
            // remove color class
            $(this).removeClass('blue light_green');
            // add html
            $(this).append("<img src=" + source[0] + "><div class='description'><p>" + String(description) + "</p></div></img>");
        }
    }
});

$('.project').mouseleave(function() {
    // remove image tag
    $(this).empty();
    // add color class
    $(this).addClass('blue');
});