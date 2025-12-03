class Solution:
    def reverse(self, x: int) -> int:
        # Check sign and reverse digits
        if x >= 0:
            reversed_num = int(str(x)[::-1])
        else:
            reversed_num = -int(str(-x)[::-1])
        
        # Check 32-bit range
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num
#eaxample usage 
if __name__ == "__main__":
   solution = Solution()
   result = solution.reverse(123)
   print(result)
