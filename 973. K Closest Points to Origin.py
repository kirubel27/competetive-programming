class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        D= []
        ans = []

        for i in range(len(points)):
            Dis= sqrt( pow(points[i][0],2)+  pow(points[i][1],2))
            D.append([Dis,points[i]])
        
        D.sort()
            
        
        for i in range(k):
            ans.append(D[i][1])

        
        return ans
