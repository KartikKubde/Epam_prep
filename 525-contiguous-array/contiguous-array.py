class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        current_sum = 0
        freq = {0:-1}

        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1

        for i in range(n):
            current_sum += nums[i]

            if current_sum in freq:
                length = i - freq[current_sum]
                ans = max(ans,length)
            else:
                freq[current_sum] = i

        return ans