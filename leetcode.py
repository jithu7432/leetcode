from pprint import PrettyPrinter
from template import Solution

from collections.abc import Generator
from collections import *


pp = PrettyPrinter(indent=2).pprint

def _mapper(s: str) -> str:
    i = 0
    hmap = {}
    cout = ''
    for x in s:
        if hmap.get(x, False):
            cout += hmap[x]
        else:
            hmap[x] = f'{i}-'
            cout += f'{i}-'
            i += 1
    return cout

def adjacent_4(x: int, y: int):
    yield x, y - 1
    yield x + 1, y
    yield x, y + 1
    yield x - 1, y


def adjacent_8(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    for y_d in (-1, 0, 1):
        for x_d in (-1, 0, 1):
            if y_d == x_d == 0:
                continue
            yield x + x_d, y + y_d

def main() -> None:
    func = [x for x in dir(Solution) if not x.startswith('_')][0]
    print(f'==================[Solution.{func}]===================', end='\n')
    while True:
        try:
            raw_input = input().strip()
            if not raw_input:
                break
            if raw_input.startswith('#') or raw_input.startswith("/*"):
                continue
            args = __import__('ast').literal_eval(raw_input)
            pp(getattr(Solution(), func)(*args))
        except EOFError:
            break


if __name__ == '__main__':
    main()
