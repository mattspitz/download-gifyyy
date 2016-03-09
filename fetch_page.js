var system = require("system");

if (system.args.length != 2) {
    console.log("Usage: phantomjs " + system.args[0] + " URL");
    phantom.exit();
}

var page = require("webpage").create();
page.onResourceRequested = function(request) {
    if (request.url.match(/\/gifs\/images/)) {
        console.log("url="+request.url);

        // Are you serious? https://github.com/ariya/phantomjs/issues/11306
        setTimeout(function() { phantom.exit(0); }, 0);
    }
};

page.open(system.args[1], function(status) {
    if (status != "success") {
        phantom.exit(1);
    }
    setTimeout(function() {
        // no image after 10s -> exit
        phantom.exit(1);
    }, 10000);
});
