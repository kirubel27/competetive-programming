class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cout = []
        C=[]
        for i in nums:
           if i not in C:
              n=nums.count(i)
              if n==2:
                cout.append(1)
              elif n==1:
                cout.append(0)
              else:
                cout.append(n*((n-1)/2))
           C.append(i)
           ans = int(sum(cout))
        return ans
