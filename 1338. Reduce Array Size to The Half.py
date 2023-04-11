class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        c = Counter(arr)
        a = [y for x, y in c.items()]
        a.sort(reverse=True)
        ans = 0
        d = 0
        for i in a:
            ans += 1
            d += i
            if d * 2 >= len(arr):
                return ans
