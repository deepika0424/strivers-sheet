class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s1=0
        s2=0
        for i in range(len(nums)+1):
            s1+=i
        for j in nums:
            s2+=j
        return s1-s2 