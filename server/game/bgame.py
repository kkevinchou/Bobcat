import time
from Queue import Queue
from bplayer import BPlayer
from lib.game import Game
from lib.util import get_current_time

RENDER_TIME = 1000 # milliseconds

class BGame(Game):
    def __init__(self):
        self.in_messages = Queue()
        self.players = {}
        self.last_render_time = 0

    def on_client_connect(self, websocket):
        player = BPlayer(websocket)
        self.players[player.id] = player
        return player

    def on_client_disconnect(self, player):
    	self.players.pop(player.id, None)

    def on_message_received(self, message):
        message['timestamp'] = get_current_time()
    	player_id = message['player_id']
    	self.players[player_id].send_message(message)
        self.in_messages.put(message)

    def update(self, delta):
        pass

    def render(self):
        current_time = get_current_time
        if current_time - self.last_render_time > RENDER_TIME:
            self.last_render_time = current_time
            render_message = {
                'render': 'render!'
            }
            # for player in self.players.values():
            #     player.send_message(render_message)
