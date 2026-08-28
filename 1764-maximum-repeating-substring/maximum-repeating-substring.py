class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        repeated = ""
        k=0

        while repeated + word in sequence:
            repeated += word
            k+= 1
        return k
        