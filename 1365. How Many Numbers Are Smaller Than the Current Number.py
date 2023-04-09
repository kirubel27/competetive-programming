class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sor_n =sorted(nums)
        idx=[]
        List=[]
        for i in sor_n:
            idx.append(sor_n.index(i))
        for i in nums:
            List.append(idx[sor_n.index(i)])
        return List