class Solution:
    def isPalindrome(self, s: str) -> bool:
       clean_text = re.sub('[^a-zA-Z0-9]','',s).lower()
       
       clean_text = list(clean_text)
       print(clean_text)
       return clean_text == clean_text[::-1]

       #cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
       
        