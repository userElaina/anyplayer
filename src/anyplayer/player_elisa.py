from .p_cl import ClPlayer
from .dicts import add_player

ELISA = 'elisa'


class ElisaPlayer(ClPlayer):
    name = ELISA
    alias = list()

    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(ELISA, '', audio, clk)


add_player(ElisaPlayer)
