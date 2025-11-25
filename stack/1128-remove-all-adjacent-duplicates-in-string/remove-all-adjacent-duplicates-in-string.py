class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack =[]
        string = list(s)

        for ch in string:
            if len(stack)==0:
                stack.append(ch)
            elif ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        print(''.join(stack))
        return ''.join(stack)
        