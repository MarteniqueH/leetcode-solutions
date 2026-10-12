class Solution(object):


    def countWords(self, words1, words2):
        count = 0
        freq1 = {}
        freq2 = {}


        for word in words1:
            freq1[word] = freq1.get(word, 0) + 1

        for word in words2:
            freq2[word] = freq2.get(word, 0) + 1

        for word in freq1:
            if freq1[word] == 1 and freq2.get(word, 0) == 1:
                count += 1

        return count 




