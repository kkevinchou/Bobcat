from lib.player import Player

class BPlayer(Player):
    def __init__(self, *args, **kwargs):
        super(BPlayer, self).__init__(*args, **kwargs)
        self.x = 0
        self.y = 0
