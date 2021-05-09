$(function() {
    $('#test').bind('click', function() {
        $.getJSON('/run', function(data) {
            console.log("test")
        });
    });
});

$(function() {
    $('#sendBtn').bind('click', function() {
        var value = document.getElementByID("msg").value
        $.getJSON('/run',
//        {val:value},
        function(data) {

        });
    });
});

function validate(name) {
    if (name.length >= 2) {
        return true;
    }
    return false;
}