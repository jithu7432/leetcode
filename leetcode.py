class Solution:
    def removeDuplicates(self, arr: list[int]) -> int:
        ns = len(arr)
        if ns == 1:
           return ns
        i = 1
        j = 1
        while j < ns:
            if arr[j - 1] != arr[j]:
                arr[i] = arr[j]
                i += 1
            j += 1
        return i

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
