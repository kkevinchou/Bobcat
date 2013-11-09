import time
from Queue import Queue
from bplayer import BPlayer
from lib.game import Game

class BGame(Game):
    players = {}

    def __init__(self):
        self.in_messages = Queue()

    def on_client_connect(self, websocket):
        player = BPlayer(websocket)
        self.players[player.id] = player
        return player

    def on_client_disconnect(self, player):
    	self.players.pop(player.id, None)

    def on_message_received(self, message):
    	player_id = message['player_id']
    	self.players[player_id].send_message(message)
        self.in_messages.put(message)

    def update(self, delta):
        pass

    def render(self):
        pass
