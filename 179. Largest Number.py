class Solution:
    def largestNumber(self, nums: list[int]) -> str:
         for i,values in enumerate(nums):
            nums[i] = str(values)
         def comp(val1,val2):
            if val1+val2>val2+val1:
               return -1
            elif val2+val1>val1+val2:
               return 1
            else:
                return 0 
         nums = sorted(nums,key=cmp_to_key(comp))
         return str(int(''.join(nums)))
