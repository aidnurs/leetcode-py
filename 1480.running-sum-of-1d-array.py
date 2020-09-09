class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tmp=0
        for index,num in enumerate(nums):
            nums[index]+=tmp
            tmp+=num
            
        return nums