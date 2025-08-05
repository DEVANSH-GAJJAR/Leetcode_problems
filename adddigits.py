class Solution:
    def my_func(self,n:int)->int:
        if n==0:
            return 0
        else:
            return 1 + (n-1)%9
#example usage 
solution = Solution()
param1 = 38 
result = solution.my_func(param1)
print(result)