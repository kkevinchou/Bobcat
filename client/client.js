$(document).ready(function(){
    // Open up a connection to our server
    var ws = new WebSocket("ws://192.168.64.138:8000/");
    // var ws = new WebSocket("ws://192.168.64.129:8000/");

    // What do we do when we get a message?
    ws.onmessage = function(evt) {
        console.log(evt.data);
        // $("#placeholder").append(evt.data + '<br>');
    }
    // Just update our conn_status field with the connection status
    ws.onopen = function(evt) {
        $('#conn_status').html('<b>Connected</b>');
    }
    ws.onerror = function(evt) {
        $('#conn_status').html('<b>Error</b>');
    }
    ws.onclose = function(evt) {
        $('#conn_status').html('<b>Closed</b>');
    }

    $('#btn_send').click(function() {
        var message_text = $('#name').val() + ': ' + $('#message').val()
        send_data = {'message_text': message_text}
        ws.send(JSON.stringify(send_data));
        $('#message').val('');
    });

    $('#message').keypress(function(event) {
        if (event.which == 13) {
            event.preventDefault();
            $('#btn_send').click();
        }
    });
});

