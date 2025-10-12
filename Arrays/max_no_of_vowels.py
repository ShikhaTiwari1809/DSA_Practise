""" https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels. """

def maxVowels(s, k):
    s.split()
    vowels = set("aeiou")
    count = sum(1 for i in s[:k] if i in vowels)
    max_count = count

    for i in range(k,len(s)):
        if s[i] in vowels:
            count +=1
        if s[i-k] in vowels:
            count-=1
        max_count = max(max_count, count)

        if max_count == k:
            return k

    return max_count

s = "abciiidef"
k = 3
print(maxVowels(s,k))