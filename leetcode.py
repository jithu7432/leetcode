from template import Solution

def main() -> None:
    while 1:
        try:
            raw_input = input()
            if not raw_input: break
            if raw_input.strip().startswith('#'): continue
            args = __import__('ast').literal_eval(raw_input)
            pp(getattr(Solution(), dir(Solution)[-1])(*args))
        except EOFError:
            break

if __name__ == '__main__':
    pp = __import__('pprint').PrettyPrinter(indent=2).pprint
    main()
