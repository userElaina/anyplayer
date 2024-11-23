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
        clk: float = 0.1
    ) -> None:
        super().__init__(audio, clk)

    def _is_available(self) -> bool:
        return True

    def _start(self) -> None:
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
                if self.process.is_alive():
                    return
            except KeyboardInterrupt:
                self.process.terminate()
                return
            except Exception as e:
                self.process.terminate()
                raise e
        raise RuntimeError('No available player')

    def _terminate(self) -> int:
        return self.process.terminate()


add_player(AutoPlayer)
