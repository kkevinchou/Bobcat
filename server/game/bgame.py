import time
from Queue import Queue
from bplayer import BPlayer
from lib.game import Game

class BGame(Game):
    players = []

    def __init__(self):
        self.in_messages = Queue()

    def on_client_connect(self, websocket):
        player = BPlayer(websocket)
        self.players.append(player)
        return player

    def on_client_disconnect(self, player):
        self.players.remove(player)

    def on_message_received(self, message):
        self.in_messages.put(message)

    def propogate_game_state(self):
        message = {
            'type': 'update',
            'players': []
        }

        for player in self.players:
            player_info = {
                'id': player.id,
                'x': player.x,
                'y': player.y
            }
            message['players'].append(player_info)

        for player in self.players:
            player.send_message(message)

    def send_to_all(self, message):
        for player in self.players:
            player.send_message(message)

    def update(self, delta):
        pass

    def render(self):
        # render() aka, update clients
        if not self.in_messages.empty():
            while not self.in_messages.empty():
                m = self.in_messages.get()
                self.send_to_all(m)
