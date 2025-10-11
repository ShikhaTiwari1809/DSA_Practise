""" https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

This is also classic example of two pointers where pointer rather being on same array will be on different arrays
like one pointer pointing to array s and another to array t. """

def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0  # i for s, j for t
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    return i == len(s) # means it came to end of array s and all values are properly matched from array t


s = 'abc'
t = 'ahbgdc'
print(isSubsequence(s,t)) # output printed is true

s = 'axc'
t = 'ahbgdc'
print(isSubsequence(s,t)) # output printed is false
