import time
from Queue import Queue
from bplayer import BPlayer
from lib.game import Game
from lib.util import get_current_time

RENDER_TIME = 1000 # milliseconds

class BGame(Game):
    def __init__(self, fps):
        super(BGame, self).__init__(fps)

        self.in_messages = Queue()
        self.players = {}

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
        # print 'render'
        pass