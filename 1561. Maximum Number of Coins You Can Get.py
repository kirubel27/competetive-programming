class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort(reverse=True)
        total = 0
        n = int(len(piles)/3)
        i = 0
        while n > 0:
            if i % 2 == 1:
                total += piles[i]
                n -= 1
            i += 1
        return total
