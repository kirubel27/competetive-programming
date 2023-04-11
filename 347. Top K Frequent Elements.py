from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
      frq = Counter(nums)
      mc = frq.most_common(k)
      ans =[]
      for i in range(len(mc)):
        ans.append(mc[i][0])
      return ans
