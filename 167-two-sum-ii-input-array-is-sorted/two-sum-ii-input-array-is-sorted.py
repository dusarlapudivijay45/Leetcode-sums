class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j=len(numbers)-1
        i=0
        while i<j:
            s= numbers[i]+numbers[j]
            if s>target:
                j -= 1
            elif s<target:
                i += 1
            else:
                return [i+1,j+1]
                









        