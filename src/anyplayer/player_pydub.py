from .p_process import ProcessPlayer
from .dicts import add_player


class PydubPlayer(ProcessPlayer):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(audio, clk)

    def is_available(self) -> bool:
        try:
            import pydub
        except ImportError:
            return False
        return True

    def run(self) -> int:
        from pydub import AudioSegment, playback
        playback.play(AudioSegment.from_file(self.audio))


add_player('pydub', PydubPlayer)
