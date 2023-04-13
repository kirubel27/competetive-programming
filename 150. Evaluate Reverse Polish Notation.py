class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        for val in tokens:
            if val == "+":
                stack.append(stack.pop()+stack.pop())
            elif val == "-":
                Op1,Op2=(stack.pop(),stack.pop())
                stack.append(Op2-Op1)
            elif val== "*":
                stack.append(int(stack.pop()*stack.pop()))
            elif val== "/":
                Op1,Op2=(stack.pop(),stack.pop())
                stack.append(int(Op2/Op1))
            else:
                stack.append(int(val))
        ans=stack[0]
        return ans
        
