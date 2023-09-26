import multiprocessing

from .p_player import Player


class ProcessPlayer(Player):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(audio, clk)

    def start(self) -> None:
        self.process = multiprocessing.Process(target=self.run)
        self.process.start()

    def is_alive(self) -> bool:
        return super().is_alive()

    def terminate(self) -> int:
        return super().terminate()
