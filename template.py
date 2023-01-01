from collections import defaultdict
class Solution:
    @staticmethod
    def _row(arr) -> bool:
        for r in arr:
            hset = set()
            for x in r:
                if x != ".":
                    if x in hset:
                        return False
                    hset.add(x)
        return True
    @staticmethod
    def _col(arr) -> bool:
        for i in range(9):
            hset = set()
            for j in range(9):
                x = arr[j][i]
                if x != ".":
                    if x in hset:
                        return False
                    hset.add(x)
        return True
    def _box(self, arr) -> bool:
        hmap = defaultdict(list)
        for i in range(9):
            for j in range(9):
                x = arr[i][j]
                key = i // 3, j // 3
                hmap[key].append(x)
        return self._row(hmap.values())
    def isValidSudoku(self, arr: list[list[str]]) -> bool:
        return self._row(arr) and self._col(arr) and self._box(arr)
