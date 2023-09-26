from .p_cl import ClPlayer
from .dicts import add_player


class FFplayPlayer(ClPlayer):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(
            'ffplay',
            ['-nodisp', '-autoexit', '-hide_banner',],
            audio,
            clk
        )


add_player('ffplay', FFplayPlayer, 'ffmpeg')
