from .p_cl import ClPlayer
from .dicts import add_player

MPG123 = 'mpg123'


class Mpg123Player(ClPlayer):
    name = MPG123
    alias = ['mpg']

    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(MPG123, '', audio, clk)  # '-q'


add_player(Mpg123Player)
