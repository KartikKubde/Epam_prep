class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        maxleft = [0] * n

        for i in range(1,n):
            maxleft[i] = max(maxleft[i-1],height[i-1])
        
        maxright = [0]*n
        
        for i in range(n-2,-1,-1):
            maxright[i] = max(maxright[i+1],height[i+1]) 

        sum = 0

        for i in range(n):
            mini = min(maxleft[i],maxright[i])
            if(mini>height[i]):
                sum +=  mini - height[i]
        
        return sum
        
        
        
        
        
        
    # My first approach
        # n = len(height)
        # maxleft = [0]*(n+1)

        # for i in range(n):
        #     if(height[i]>maxleft[i]):
        #         maxleft[i+1] = height[i]
        #     else:
        #         maxleft[i+1] = maxleft[i]
        
        # maxright = [0]*n
        
        # for i in range(n-1,-1,-1):
        #     if(height[i]>maxright[i]):
        #         maxright[i-1] = height[i]
        #     else:
        #         maxright[i-1] = maxright[i]

        # ans = [0]*n

        # for i in range(n):
        #     mini = min(maxleft[i],maxright[i])
        #     if(mini>height[i]):
        #         ans[i] = mini - height[i]
        
        # return sum(ans)
