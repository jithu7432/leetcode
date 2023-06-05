import inspect
from template import Solution
from pprint import PrettyPrinter

def adj4(x: int, y: int):
    yield x, y - 1
    yield x + 1, y
    yield x, y + 1
    yield x - 1, y

def adj8(x: int, y: int):
    for y_d in (-1, 0, 1):
        for x_d in (-1, 0, 1):
            if y_d == x_d == 0:
                continue
            yield x + x_d, y + y_d

def main() -> None:
    pp = PrettyPrinter(indent=2).pprint
    func, _ = inspect.getmembers(Solution(), predicate=inspect.ismethod)[0]
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
