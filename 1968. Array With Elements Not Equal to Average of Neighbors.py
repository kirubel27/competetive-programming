class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[]
        j=0
        k=len(nums)-1
        nums.sort()
        while len(ans) != len(nums):
            ans.append(nums[j])
            j+=1
            if j<=k:
                ans.append(nums[k])
                k-=1
        return ans