# import sys
# import os
# sys.path.append(os.getcwd())
# print sys.path

import json
import random
import threading

from gevent import pywsgi, sleep
from gevent.pool import Group
from geventwebsocket.handler import WebSocketHandler
from game.game import Game
import json

class GameApp(object):
    def __init__(self, *args, **kwargs):
        self.game = Game(60)
        self.game_thread = threading.Thread(target=self.game.main)
        self.game_thread.daemon = True
        self.game_thread.start()

    def __call__(self, environ, start_response):
        websocket = environ['wsgi.websocket']
        player_id = self.game.on_client_connect(websocket)

        while True:
            recv_data = websocket.receive()

            if recv_data is None:
                break

            message_dict = json.loads(recv_data)
            message_dict['player_id'] = player_id
            self.game.on_message_received(message_dict)

        self.game.on_client_disconnect(player_id)

server = pywsgi.WSGIServer(("", 8000), GameApp(), handler_class=WebSocketHandler)
server.serve_forever()