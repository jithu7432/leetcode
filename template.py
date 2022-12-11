class Solution:
    def gridGame(self, arr: list[list[int]]) -> int:
        ni = len(arr)
        nj = len(arr[0])

        i = j = c = 0
        c += arr[i][j]
        arr[i][j] = 0
        while True:
            if not (i < ni and j < nj):
                break
            print(f'{i, j=}')
            c += arr[i][j]
            arr[i][j] = 0
            if i < ni - 1 and arr[i + 1][j] > arr[i][j + 1]:
                i += 1
            else:
                j += 1
        print(arr)
        return c

        #  hmap = {}
        #  for i in range(len(arr)):
        #      for j in range(len(arr[0])):
        #          hmap[(i, j)] = arr[i][j] + max(hmap.get((i - 1, j), 0), hmap.get((i, j - 1), 0))
        #  return hmap[(len(arr) - 1, len(arr[0]) - 1)]

#  4
#  4
#  7
