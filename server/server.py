# import sys
# import os
# sys.path.append(os.getcwd())
# print sys.path

import threading
from game.game  import Game
from lib.network.receiver import Receiver

class Server(object):
    def __init__(self):
        self.game = Game(60)
        self.receiver = Receiver(self.game)
        self.receiver_thread = threading.Thread(target=self.receiver.start)
        self.receiver_thread.daemon = True

    def start(self):
        print '[SERVER] Starting...'
        self.receiver_thread.start()
        self.game.start()

    def test_func(self):
        print 'TEST FUNC'

if __name__ == "__main__":
    server = Server()
    server.start()