var projects =     {"1":["/static/img/dropbox.png", "this is the description"],
                    "2":["/static/img/mobie.png", "this is the description of my second project"],
                    "3":["/static/img/mobie.png", "this is the description of my third project"],
                    "4":["/static/img/mobie.png", "this is the description of my fourth project"]
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
            $(this).append("<img src=" + source[0] + "><div><p>" + String(description) + "</p></div></img>");
        }
    }
});

$('.project').mouseleave(function() {
    // remove image tag
    $(this).empty();
    // add color class
    $(this).addClass('blue');
});