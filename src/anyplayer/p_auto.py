import time

from .p_player import Player
from .dicts import get_names, get_player, add_player

AUTO = 'auto'


class AutoPlayer(Player):
    name = AUTO
    alias = ['', 'default', 0, '0']

    def __init__(
        self,
        audio: str,
        max_wait: float = 0.5,
        clk: float = 0.1
    ) -> None:
        self.max_wait = max_wait
        super().__init__(audio, clk)

    def is_available(self) -> bool:
        return True

    def start(self) -> None:
        for i in get_names():
            if i == AUTO:
                continue
            self.process = get_player(i, self.audio, self.clk)
            try:
                if not self.process.is_available():
                    continue
                try:
                    self.process.start()
                except KeyboardInterrupt as e:
                    raise e
                except Exception as e:
                    self.process.terminate()
                t = time.time()
                while self.process.is_alive():
                    if time.time()-t > self.max_wait:
                        return
                    time.sleep(self.clk)
            except KeyboardInterrupt:
                self.process.terminate()
                return
            except Exception as e:
                self.process.terminate()
                raise e
        raise RuntimeError()

    def terminate(self) -> int:
        return self.process.terminate()


add_player(AutoPlayer)
