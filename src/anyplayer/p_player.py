import time
from abc import ABCMeta, abstractmethod


class Player(metaclass=ABCMeta):
    name = 'player'
    alias = list()

    def __init__(self, audio: str, clk: float = 0.1) -> None:
        self.alive_flg = False
        self.audio = audio
        self.clk = clk

    @abstractmethod
    def _is_available(self) -> bool:
        return False

    def is_available(self) -> bool:
        return self._is_available()

    @abstractmethod
    def _start(self) -> None:
        pass

    def start(self) -> None:
        self.alive_flg = True
        self._start()

    def _is_alive(self) -> bool:
        return self.process.is_alive()

    def is_alive(self) -> bool:
        if self.alive_flg:
            return self._is_alive()
        return False

    def _terminate(self) -> int:
        if not self.is_alive():
            return 0
        self.process.terminate()
        if not self.is_alive():
            return 0
        return 1

    def terminate(self) -> int:
        ans = self._terminate()
        self.alive_flg = False
        return ans

    def _kill(self) -> int:
        if self._terminate() == 0:
            return 0
        time.sleep(self.clk)
        if self.is_alive():
            self.process.kill()
        return 1

    def kill(self) -> int:
        ans = self._kill()
        self.alive_flg = False
        return ans

    def _join(self) -> None:
        while self.is_alive():
            time.sleep(self.clk)

    def join(self) -> None:
        self._join()

    def _wait(self, s: float = -1.) -> float:
        t = time.time()
        try:
            if s < 0:
                self.join()
            else:
                while time.time()-t < s and self.is_alive():
                    time.sleep(self.clk)
        except KeyboardInterrupt:
            pass
        finally:
            self.kill()
            return time.time()-t

    def wait(self, s: float = -1.) -> float:
        return self._wait(s)

    def _run(self) -> float:
        self.start()
        return self.wait()

    def run(self) -> float:
        return self._run()
