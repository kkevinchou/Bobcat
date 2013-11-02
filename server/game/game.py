import time
from player import Player

class Game(object):
    players = []

    def on_client_connect(self, websocket):
        player = Player(websocket)
        self.players.append(player)
        return player

    def on_client_disconnect(self, player):
        self.players.remove(player)

    def send_messages(self, message):
        for player in self.players:
            player.websocket.send(message)

    def receive_message(self, message):
        self.send_messages(message['message_text'])

    def main(self):
        while True:
            time.sleep(1)
