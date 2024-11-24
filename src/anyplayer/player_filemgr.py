from .p_cl import ClPlayer
from .dicts import add_player
from .utils import which


class FilemgrPlayer(ClPlayer):
    name = 'filemgr'
    alias = ['explorer', 'dolphin', 'open']

    def __init__(self, audio: str, clk: float = 0.1) -> None:
        for i in ['explorer', 'dolphin', 'xdg-open']:
            if which(i):
                break
        super().__init__(i, '', audio, clk)

    def _is_alive(self) -> bool:
        if self.executable == 'xdg-open':
            return self.is_available()
        return super()._is_alive()


add_player(FilemgrPlayer)
