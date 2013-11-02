$(document).ready(function(){
    var ws = new WebSocket("ws://192.168.64.138:8000/");

    ws.onmessage = function(evt) {
        $('#events').append(evt.data + "\n");
        $('#events').scrollTop($('#events')[0].scrollHeight);
    }

    ws.onopen = function(evt) {
        $('#conn_status').html('<b>Connected</b>');
    }
    ws.onerror = function(evt) {
        $('#conn_status').html('<b>Error</b>');
    }
    ws.onclose = function(evt) {
        $('#conn_status').html('<b>Closed</b>');
    }
});

// function register_input(obj) {
//     obj.keyPress()
// }