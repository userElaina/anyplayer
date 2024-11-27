from .p_cl import ClPlayer
from .dicts import add_player

APLAY = 'aplay'


class AplayPlayer(ClPlayer):
    name = APLAY
    alias = ['alsa']

    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(APLAY, '', audio, clk)


add_player(AplayPlayer)
