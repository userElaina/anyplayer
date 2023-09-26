from .p_cl import ClPlayer
from .dicts import add_player


class CmusPlayer(ClPlayer):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__('cmus-remote', '-f', audio, clk)


add_player('cmus', CmusPlayer)
