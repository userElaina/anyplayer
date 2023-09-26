from .p_process import ProcessPlayer
from .dicts import add_player


class PyAudioPlayer(ProcessPlayer):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(audio, clk)

    def is_available(self) -> bool:
        try:
            import wave
            import pyaudio
        except ImportError:
            return False
        return True

    def run(self) -> int:
        import wave
        import pyaudio
        CHUNK = 1024
        with wave.open(self.audio, 'rb') as wf:
            p = pyaudio.PyAudio()
            stream = p.open(
                format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True
            )
            data = wf.readframes(CHUNK)
            while len(data):
                stream.write(data)
                data = wf.readframes(CHUNK)
            stream.close()
            p.terminate()


add_player('pyaudio', PyAudioPlayer)
