from .p_process import ProcessPlayer
from .dicts import add_player


class PlaysoundPlayer(ProcessPlayer):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(audio, clk)

    def is_available(self) -> bool:
        try:
            import playsound
        except ImportError:
            return False
        return True

    def run(self) -> int:
        import playsound
        playsound.playsound(self.audio)


add_player('playsound', PlaysoundPlayer)
