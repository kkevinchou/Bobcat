import time
from Queue import Queue

class Game(object):
    def on_client_connect(self, websocket):
        raise NotImplementedError()

    def on_client_disconnect(self, player):
        raise NotImplementedError()

    def on_message_received(self, message):
        raise NotImplementedError()

    def update(self, delta):
        raise NotImplementedError()

    def render(self):
        raise NotImplementedError()

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
                self.update(fixed_update_dt)

            self.render()

