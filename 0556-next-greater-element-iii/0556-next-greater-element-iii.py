class Solution:
    def nextGreaterElement(self, n: int) -> int:

        nums = list(str(n))

        i, j = len(nums) - 2, len(nums) - 1
        
        while i >= 0 and nums[i] >= nums[i+1]:
            i-=1
        if i < 0:
            return -1 
        
        while nums[j] <= nums[i]:
            j-=1
        
        nums[i], nums[j] = nums[j], nums[i]
        
        nums[i+1:] = reversed(nums[i+1:])
        res = int("".join(nums))
        
        return res if res < 2**31 else -1
        