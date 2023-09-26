from .p_process import ProcessPlayer
from .dicts import add_player


class PydubPlayer(ProcessPlayer):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(audio, clk)

    def is_available(self) -> bool:
        try:
            from pydub import AudioSegment, playback
            self.i_as = AudioSegment
            self.i_pb = playback
        except ImportError:
            return False
        return True

    def run(self) -> int:
        self.i_pb.play(self.i_as.from_file(self.audio))


add_player('pydub', PydubPlayer)
