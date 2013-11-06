$(document).ready(function(){
    var socket = new WebSocket("ws://192.168.64.140:8000/");



    socket.onmessage = function(evt) {
        $('#events').append(evt.data + "\n");
        $('#events').scrollTop($('#events')[0].scrollHeight);
    }

    socket.onopen = function(evt) {
        $('#conn_status').html('<b>Connected</b>');
    }
    socket.onerror = function(evt) {
        $('#conn_status').html('<b>Error</b>');
    }
    socket.onclose = function(evt) {
        $('#conn_status').html('<b>Closed</b>');
    }

    register_input($(this), socket);
});

function register_input(obj, socket) {
    KEY_UP = 38
    KEY_DOWN = 40
    KEY_LEFT = 37
    KEY_RIGHT = 39
    KEY_W = 87
    KEY_S = 83
    KEY_A = 65
    KEY_D = 68

    keys_down = {}

    obj.keydown(function(event) {
        var keypress_message = {
            'type': 'keypress',
        }

        keys_down[event.keyCode]

        var key = null;

        if (event.keyCode == KEY_UP || event.keyCode == KEY_W) {
            key = 'UP';
        } else if (event.keyCode == KEY_DOWN || event.keyCode == KEY_S) {
            key = 'DOWN';
        } else if (event.keyCode == KEY_LEFT || event.keyCode == KEY_A) {
            key = 'LEFT';
        }else if (event.keyCode == KEY_RIGHT || event.keyCode == KEY_D) {
            key = 'RIGHT';
        }

        if (key != null) {
            keypress_message['key'] = key;
            socket.send(JSON.stringify(keypress_message));
        }
    })

    obj.keyup(function(event) {
        var keypress_message = {
            'type': 'keypress',
        }

        var key = null;

        if (event.keyCode == KEY_UP || event.keyCode == KEY_W) {
            key = 'UP';
        } else if (event.keyCode == KEY_DOWN || event.keyCode == KEY_S) {
            key = 'DOWN';
        } else if (event.keyCode == KEY_LEFT || event.keyCode == KEY_A) {
            key = 'LEFT';
        }else if (event.keyCode == KEY_RIGHT || event.keyCode == KEY_D) {
            key = 'RIGHT';
        }

        if (key != null) {
            keypress_message['key'] = key;
            socket.send(JSON.stringify(keypress_message));
        }
    })
}
