/**
 * Created by johanna on 2/27/15.
 */
var projects = {"1":"/static/img/dropbox.png", "2":"/static/img/mobie.png"};
var source;
var htmlString = "<img src=" + source + "><div><p>What's it about</p></div></img>";

$('#1').hover(function() {
    console.log('in function');
    var id = (this.id);
    // get matching image source
    for (var key in projects) {
        if (key !== id) {
        } else {
            source = projects[key];
            console.log(source);
        }
    }
    // remove color class
    $(this).removeClass('blue light_green');
    // add html
    $(this).text(htmlString);
});