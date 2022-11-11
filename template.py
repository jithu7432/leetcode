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
