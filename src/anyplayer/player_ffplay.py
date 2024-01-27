from .p_cl import ClPlayer
from .dicts import add_player

FFPLAY = 'ffplay'


class FFplayPlayer(ClPlayer):
    name = FFPLAY
    alias = ['ffmpeg', 'avplay']

    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(
            FFPLAY,
            ['-nodisp', '-autoexit', '-hide_banner',],  # -v quiet
            audio,
            clk
        )


add_player(FFplayPlayer)
