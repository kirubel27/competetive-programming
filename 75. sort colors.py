class Solution:
    def sortColors(self, nums: List[int]) -> None:
        W=R=B=0
        for i in nums:
            if i==0:
                R+=1
            elif i==1:
                W+=1
            else:
                B+=1
        nums[:R]= [0]*R
        nums[R:R+W]= [1]*W
        nums[R+W:]=[2]*B
        return nums