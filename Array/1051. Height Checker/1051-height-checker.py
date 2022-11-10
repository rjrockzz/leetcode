class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        counter = 0
        i = 0
        while i<len(heights):
            if heights[i]!=expected[i]:
                counter+=1
            i+=1
        return counter