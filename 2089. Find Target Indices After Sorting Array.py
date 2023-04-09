class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        s_num=sorted(nums)
        ans=[]
        for idx,val in enumerate(s_num):
            if val==target:
                ans.append(idx)
        return ans