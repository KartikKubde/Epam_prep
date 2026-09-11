import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = [] 
        n = len(nums)

        for i in range(k):
            heapq.heappush(ans,nums[i])

        for i in range(k,n):
            if(nums[i] > ans[0]):
                heapq.heappop(ans)
                heapq.heappush(ans,nums[i])

        return ans[0]