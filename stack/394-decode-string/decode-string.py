class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]

        for ch in s:
            if ch!=']':
                stack.append(ch)
            else:
                 # Step 1 Extract the substring
                substring = ""
                while stack[-1]!="[":
                    substring = stack.pop()+substring
                stack.pop() #remove "["

                # Step 2 Extract the digits
                num = ""
                while stack and stack[-1].isdigit() :
                    num = stack.pop()+num

                # Step 3 Repeat substring
                repeated = int(num) * substring

                stack.append(repeated)

        return "".join(stack)
                