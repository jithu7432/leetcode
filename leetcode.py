from template import Solution

def main() -> None:
    func = [x for x in dir(Solution) if not x.startswith('_')][0]
    print(f'Solution.{func}', end=2*'\n')
    while True:
        try:
            raw_input = input()
            if not raw_input: break
            if raw_input.strip().startswith('#'): continue
            args = __import__('ast').literal_eval(raw_input)
            pp(getattr(Solution(), func)(*args))
        except EOFError:
            break

if __name__ == '__main__':
    pp = __import__('pprint').PrettyPrinter(indent=2).pprint
    main()
