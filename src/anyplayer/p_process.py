import multiprocessing

from .p_player import Player
from abc import abstractmethod


class ProcessPlayer(Player):
    def __init__(self, audio: str, clk: float = 0.1) -> None:
        super().__init__(audio, clk)

    def start(self) -> None:
        self.process = multiprocessing.Process(target=self.run)
        self.process.start()

    def join(self) -> None:
        self.process.join()

    @abstractmethod
    def run(self) -> float:
        return 0.
