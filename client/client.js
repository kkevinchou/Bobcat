$(document).ready(function(){
    var socket = new WebSocket("ws://127.0.0.1:8000/");

    socket.onmessage = function(event) {
        message_obj = $.parseJSON(event.data);
        handle_message(message_obj);
    }

    socket.onopen = function(event) {
        $('#conn_status').html('<b>Connected</b>');
    }
    socket.onerror = function(event) {
        $('#conn_status').html('<b>Error</b>');
    }
    socket.onclose = function(event) {
        $('#conn_status').html('<b>Closed</b>');
    }

    register_input($(this), socket);
});

function handle_message(event) {
    $('#events').append(JSON.stringify(message_obj, null, 4) + "\n");
    $('#events').scrollTop($('#events')[0].scrollHeight);
}

function convert_keycode_to_key(key_code) {
    if (key_code == KEY_UP || key_code == KEY_W) {
        return 'UP';
    } else if (key_code == KEY_DOWN || key_code == KEY_S) {
        return 'DOWN';
    } else if (key_code == KEY_LEFT || key_code == KEY_A) {
        return 'LEFT';
    }else if (key_code == KEY_RIGHT || key_code == KEY_D) {
        return 'RIGHT';
    } else {
        return null;
    }
}

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
            'event': 'key_down',
            'key': null
        }

        console.log(event.keyCode);

        var key = convert_keycode_to_key(event.keyCode);
        if (key != null && !keys_down[event.keyCode]) {
            action_message['key'] = key;
            socket.send(JSON.stringify(action_message));
        }

        keys_down[event.keyCode] = true;
    })

    obj.keyup(function(event) {
        var action_message = {
            'type': 'action',
            'event': 'key_up',
            'key': null
        }

        delete keys_down[event.keyCode];

        var key = convert_keycode_to_key(event.keyCode);

        if (key != null) {
            action_message['key'] = key;
            socket.send(JSON.stringify(action_message));
        }
    })
}
