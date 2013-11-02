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

    def main(self):
        max_frame_time = 0.25
        fixed_update_dt = 0.01
        accumulated_time = 0
        current_time = time.time()
        propogations = 0

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
            if propogations < 10 and self.players:
                print 'send'
                propogations += 1
                self.propogate_game_state()

