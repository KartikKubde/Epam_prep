class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        nums.sort()
        
        last_smaller = float('-inf')
        count = 0
        longest = 0
        n = len(nums)

        for i in range(n):

            if nums[i] == last_smaller:
                continue

            if(nums[i] - 1 == last_smaller):
                count += 1
            elif nums[i] != last_smaller:
                count = 1
            longest = max(longest,count)
            last_smaller = nums[i]

        return longest