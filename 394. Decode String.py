class Solution:
    def decodeString(self, s: str) -> str:
        alpha = []
        num = 0
        result = ''

        for i in s:
            if i.isnumeric():
                num = num*10+ int(i)
            elif i == '[':
                alpha.append(result)
                alpha.append(num)
                result = ''   #reset counters
                num = 0   
            elif i == ']':
                cnt = alpha.pop()
                prev = alpha.pop()
                result = prev + cnt * result
            else:
                result += i
        return result
