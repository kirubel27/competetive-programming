class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
      s= sorted(nums, key = int,reverse = True)
      ans = s[k - 1]
      return ans