import time
from Queue import Queue
from player import Player
from lib.game import Game as BaseGame

from panda import Application

class Game(BaseGame):
    def __init__(self, fps):
        super(Game, self).__init__(fps)

        self.in_messages = Queue()
        self.players = {}
        self.a = Application()

    def on_client_connect(self, websocket):
        player = Player(websocket)
        self.players[player.id] = player
        return player.id

    def on_client_disconnect(self, player_id):
    	self.players.pop(player_id, None)

    def on_message_received(self, message):
        message['timestamp'] = time.time()
    	player_id = message['player_id']
    	self.players[player_id].send_message(message)
        self.in_messages.put(message)

    def update(self, delta):
        self.a.taskMgr.step()
        pass

    def render(self):
        # print 'render'
        pass