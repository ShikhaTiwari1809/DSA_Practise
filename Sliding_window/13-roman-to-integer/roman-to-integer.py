class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        char_values = []
        for char in s:
            char_value = roman_value[char]
            char_values.append(char_value)

        n = len(char_values)-1
        total_value = char_values[n]
        while n > 0:
            if char_values[n-1]<char_values[n]:
                total_value = total_value - char_values[n-1]
            else:
                total_value = total_value + char_values[n-1]
            n=n-1
        return total_value

        