from .p_cl import ClPlayer
from .dicts import add_player


class MpvPlayer(ClPlayer):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__('mpv', '--no-video', audio, clk)


add_player('mpv', MpvPlayer)
