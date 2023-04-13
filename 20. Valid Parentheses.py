class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Hmap = {')':"(","]":"[","}":"{"}
        for val in s:
            if val not in Hmap:
                stack.append(val)
            else:
                if stack and stack[-1] == Hmap[val]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
