import time
from Queue import Queue
from player import Player

class Game(object):
    players = []

    def __init__(self):
        self.in_messages = Queue()

    def on_client_connect(self, websocket):
        player = Player(websocket)
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

    def main(self):
        max_frame_time = 0.25
        fixed_update_dt = 0.01
        accumulated_time = 0
        current_time = time.time()

        while True:
            new_time = time.time()
            frame_time = new_time - current_time
            if frame_time >= max_frame_time:
                frame_time = max_frame_time
            current_time = time.time()

            accumulated_time += frame_time

            while accumulated_time >= fixed_update_dt:
                accumulated_time -= fixed_update_dt
                # update(fixed_update_dt)

            # render() aka, update clients
            if not self.in_messages.empty():
                while not self.in_messages.empty():
                    m = self.in_messages.get()
                    self.send_to_all(m)

