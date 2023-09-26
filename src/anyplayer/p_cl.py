import shlex
import subprocess

from .p_player import Player
from .utils import which


class ClPlayer(Player):
    def __init__(
        self,
        executable: str,
        args: str | list,
        audio: str,
        clk: float = 0.1
    ) -> None:
        self.executable = executable
        if isinstance(args, list):
            args = ' '.join(args)
        if args:
            args += ' '
        self.head = executable + ' ' + args + '"%s"'
        super().__init__(audio, clk)

    def is_available(self) -> None:
        if which(self.executable):
            return True
        else:
            return False

    def start(self) -> None:
        self.process = subprocess.Popen(
            shlex.split(self.head % self.audio),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def run(self) -> int:
        return super().run()

    def is_alive(self) -> bool:
        return self.process.poll() is None

    def terminate(self) -> int:
        return super().terminate()
