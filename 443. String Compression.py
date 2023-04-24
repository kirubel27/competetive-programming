class Solution:
    def compress(self, chars: List[str]) -> int:
        j = 0
        k = 1
        l= len(chars)
        for i in range(1,l+1):
            if i < l and chars[i] == chars[i-1]:
                 k += 1
            else:
                chars[j] = chars[i-1]
                j+= 1

                if k > 1:
                    s = str(k)
                    m = len(s)
                    chars[j : j + m] = s
                    j+= m
 
                k = 1

        return j
