""" https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 """
import re
def isPalindrome(s) :
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    cleaned_text = list(cleaned_text)

    return cleaned_text == cleaned_text[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))