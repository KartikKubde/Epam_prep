class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #gpt approach
        n = len(nums)
        i = 0 
        j = 0 

        for i in range(n):
            if(nums[i] != 0):
                nums[j] = nums[i]
                j += 1

        while(j < n):
            nums[j] = 0
            j += 1

        return nums

# my approach
# n = len(nums)
#         i = 0 
#         j = n - 1

#         while(i<j):
#             while(nums[i] == 0):
#                 nums[i],nums[j] = nums[j],nums[i]
#                 j -= 1
#             i += 1
#         return nums