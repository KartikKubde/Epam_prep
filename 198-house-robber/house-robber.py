class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def func(nums,n,i,freq):

            if i == n:
                return 0 

            if dp[i][freq] != -1 :
                return dp[i][freq]

            if freq == 0 :
                dp[i][freq] = func(nums,n,i+1,1)
                return dp[i][freq]

            c1 = nums[i] + func(nums,n,i+1,0)
            c2 = func(nums,n,i+1,1)

            dp[i][freq] = max(c1,c2)

            return dp[i][freq]

        n = len(nums)
        dp = [[-1] * 2 for _ in range(len(nums))]
        i = 0
        freq = 1
        return func(nums,n,i,freq)