# import sys
# import os
# sys.path.append(os.getcwd())
# print sys.path

import json
import random
import threading
# from game.player import Player

from gevent import pywsgi, sleep
from gevent.pool import Group
from geventwebsocket.handler import WebSocketHandler
from game.game import Game
import json

class GameApp(object):
    def __init__(self, *args, **kwargs):
        self.game = Game()
        self.game_thread = threading.Thread(target=self.game.main)
        self.game_thread.daemon = True
        self.game_thread.start()

    def __call__(self, environ, start_response):
        websocket = environ['wsgi.websocket']
        player = self.game.on_client_connect(websocket)

        while True:
            recv_data = websocket.receive()

            if recv_data is None:
                break

            message_obj = json.loads(recv_data)
            self.game.receive_message(message_obj)

        self.game.on_client_disconnect(player)

server = pywsgi.WSGIServer(("", 8000), GameApp(), handler_class=WebSocketHandler)
server.serve_forever()