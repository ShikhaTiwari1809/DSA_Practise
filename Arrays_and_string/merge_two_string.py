""" https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
 """

def mergeAlternately(word1, word2):
    new_string =[]
    max_len = max(len(word1),len(word2))
    for i in range(max_len):
        if i <len(word1):
            new_string.append(word1[i])
        if  i <len(word2):
            new_string.append(word2[i])
    return ''.join(new_string)   


word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1,word2))