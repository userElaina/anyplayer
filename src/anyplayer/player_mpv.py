from .p_cl import ClPlayer
from .dicts import add_player

MPV = 'mpv'


class MpvPlayer(ClPlayer):
    name = MPV
    alias = list()

    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(MPV, '--no-video', audio, clk)  # --no-terminal


add_player(MpvPlayer)
