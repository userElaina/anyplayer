from .p_cl import ClPlayer
from .dicts import add_player


class Mpg123Player(ClPlayer):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__('mpg123', '', audio, clk)


add_player('mpg123', Mpg123Player)
