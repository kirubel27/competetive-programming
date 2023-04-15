class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        j=len(people)-1
        k=0
        people.sort()
        count=0
        while k<=j:
            if people[j] +people[k]<= limit:
                k+=1
                j-=1
            else:
                j-=1
            count+=1

        return count