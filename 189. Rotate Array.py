class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        j=0
        for i in range(k):
            nums.insert(j,nums.pop())
        """
        Do not return anything, modify nums in-place instead.