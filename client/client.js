$(document).ready(function(){
    var socket = new WebSocket("ws://127.0.0.1:8000/");

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
        var action_message = {
            'type': 'action',
            'event': 'keydown',
            'key': null
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

        if (key != null && !keys_down[event.keyCode]) {
            action_message['key'] = key;
            socket.send(JSON.stringify(action_message));
        }

        keys_down[event.keyCode] = true;
    })

    obj.keyup(function(event) {
        var action_message = {
            'type': 'action',
            'event': 'keyup',
            'key': null
        }

        delete keys_down[event.keyCode];

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
            action_message['key'] = key;
            socket.send(JSON.stringify(action_message));
        }
    })
}
