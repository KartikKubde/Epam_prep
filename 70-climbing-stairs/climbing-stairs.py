class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        memo = {1:1,2:2}

        def func(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = func(n-1) + func(n-2)
                return memo[n]

        return func(n)