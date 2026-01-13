class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        map = defaultdict(list)  #group each word by thier first alphabet

        for word in words:
            map[word[0]].append(word)

        result = 0

        for c in s:
            var = map[c]
            map[c] = []
            for temp in var:
                if len(temp) == 1:
                    result += 1
                else:
                    map[temp[1]].append(temp[1:])
                


        return result