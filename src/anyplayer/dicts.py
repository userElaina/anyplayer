from typing import Iterable

from .p_player import Player

__NAME = list()
__ALIAS = dict()
__CLASS = dict()
__RELIAS = dict()
__RELIAS_FLAG = True


def add_player(
    name: str,
    cls: classmethod,
    alias: Iterable = list(),
) -> None:
    assert name not in __NAME
    assert name not in __CLASS
    assert name not in __ALIAS
    __NAME.append(name)
    __CLASS[name] = cls
    if isinstance(alias, str):
        __ALIAS[name] = [alias,]
    else:
        __ALIAS[name] = [i for i in alias]


def realias(player: str) -> str:
    global __RELIAS, __RELIAS_FLAG
    if __RELIAS_FLAG:
        __RELIAS_FLAG = False
        __RELIAS = {j: i for i in __ALIAS for j in __ALIAS[i]}
    return __RELIAS.get(player, player)


def is_player(player: str) -> bool:
    return realias(player) in __NAME


def get_player(player: str, audio: str, clk: float = 0.1) -> Player:
    assert is_player(player)
    player = realias(player)
    return __CLASS[player](audio, clk)


def get_available_player(
    player: str,
    audio: str,
    clk: float = 0.1,
    err: bool = False,
) -> Player | None:
    if not is_player(player):
        if err:
            raise ValueError('%s is not a player' % player)
        else:
            return None
    ans = get_player(player, audio, clk)
    if not ans.is_available():
        if err:
            raise ValueError('Player %s is not available' % player)
        else:
            return None
    return ans


def get_names() -> list[str]:
    return __NAME.copy()


def get_availables() -> list[str]:
    return [i for i in __NAME if get_player(i, '').is_available()]


for i in __NAME:
    assert i in __ALIAS
    assert i in __CLASS
assert len(__NAME) == len(__ALIAS) == len(__CLASS)
