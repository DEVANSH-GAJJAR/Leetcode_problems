class Solution:
    def my_func(self,num:int)->bool:
        i = 1
        while i * i <= num:
                if i*i == num:
                     return True
                i += 1 
        return False
#example usage 
if __name__ == "__main__":
     sol = Solution()
     param1 = int(input("Enter your number "))
     result = sol.my_func(param1)
     print(result)