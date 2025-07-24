class Solution:
    def my_func(self,n:int)->bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n //2
        return n==1
#example use 
if __name__ == "__main__":
    solution = Solution()
    param1 = 16 
    result = solution.my_func(param1)
    print(result)