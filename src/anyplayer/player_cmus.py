import os

from .p_cl import ClPlayer
from .dicts import add_player


class CmusPlayer(ClPlayer):
    name = 'cmus'
    alias = list()

    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__('cmus-remote', '-f', audio, clk)

    def _is_alive(self) -> bool:
        return True

    def _terminate(self) -> int:
        os.system("cmus-remote -s")
        return 0

    def _join(self) -> None:
        pass


add_player(CmusPlayer)
