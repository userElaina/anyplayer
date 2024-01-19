import time
from abc import ABCMeta, abstractmethod


class Player(metaclass=ABCMeta):
    name = 'player'
    alias = list()

    def __init__(self, audio: str, clk: float = 0.1) -> None:
        self.audio = audio
        self.clk = clk

    @abstractmethod
    def is_available(self) -> bool:
        return False

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def run(self) -> int:
        self.start()
        self.wait()

    @abstractmethod
    def is_alive(self) -> bool:
        return self.process.is_alive()

    @abstractmethod
    def terminate(self) -> int:
        if not self.is_alive():
            return 0
        self.process.terminate()
        if not self.is_alive():
            return 0
        time.sleep(self.clk)
        if not self.is_alive():
            return 0
        self.process.kill()
        return 1

    def kill(self) -> int:
        return self.terminate()

    def wait(self, s: float = -1.) -> int:
        try:
            if s < 0:
                while self.is_alive():
                    time.sleep(self.clk)
            else:
                t = time.time()
                while time.time()-t < s and self.is_alive():
                    time.sleep(self.clk)
        except KeyboardInterrupt:
            pass
        finally:
            return self.terminate()
