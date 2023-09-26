from .p_process import ProcessPlayer
from .dicts import add_player


class PlaysoundPlayer(ProcessPlayer):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(audio, clk)

    def is_available(self) -> bool:
        try:
            from playsound import playsound
            import os
            if os.name == 'posix':
                import gi
                gi.require_version('Gst', '1.0')
                from gi.repository import Gst
            self.i_ps = playsound
        except ImportError:
            return False
        return True

    def run(self) -> int:
        self.i_ps(self.audio)


add_player('playsound', PlaysoundPlayer)
