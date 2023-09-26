from .p_cl import ClPlayer
from .dicts import add_player


class VlcPlayer(ClPlayer):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__('cvlc', '', audio, clk)


add_player('vlc', VlcPlayer, 'cvlc')
