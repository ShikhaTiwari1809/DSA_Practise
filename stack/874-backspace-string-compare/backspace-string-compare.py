class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def cleaned_string(s):
            stack =[]

            for ch in s:
                if ch!="#":
                    stack.append(ch)
                else:
                    if len(stack)!=0:
                        stack.pop()
            return ''.join(stack)

        cleaned_s = cleaned_string(s)
        cleaned_t = cleaned_string(t)
        return cleaned_s==cleaned_t
        