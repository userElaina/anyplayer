from .p_player import Player
from .dicts import add_player


class SimpleaudioPlayer(Player):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(audio, clk)

    def is_available(self) -> bool:
        try:
            import simpleaudio
        except ImportError:
            return False
        return True

    def start(self) -> None:
        import simpleaudio as sa
        self.process = sa.WaveObject.from_wave_file(self.audio).play()

    def run(self) -> int:
        return super().run()

    def is_alive(self) -> bool:
        return self.process.is_playing()

    def terminate(self) -> int:
        if self.is_alive():
            self.process.stop()
        return 0


add_player('simpleaudio', SimpleaudioPlayer)
