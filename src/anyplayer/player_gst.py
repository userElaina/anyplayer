from .p_cl import ClPlayer
from .dicts import add_player

class GstPlayer(ClPlayer):
    name = 'gst'
    alias = list()

    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__('gst-play-1.0', '', audio, clk)


add_player(GstPlayer)
