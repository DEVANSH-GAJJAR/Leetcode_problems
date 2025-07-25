class Solution:
    def my_func(self,n:int)->bool:
        if n<=0:
            return False
        while n%3 == 0:
            n = n // 3
        return n == 1
 #example usage 
if __name__ == "__main__":
    solution = Solution()
    param1 = 27
    result = solution.my_func(param1)
    print(result)       