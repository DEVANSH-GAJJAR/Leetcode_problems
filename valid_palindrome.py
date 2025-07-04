class Solution:
    def valid_palindrome(self,s):

     s = ''.join(char.lower() for char in s if char.isalnum)
     #checking the string 
     return s == s[::-1]
   
   #exaple usage

if __name__ == "__main__":
    solution = Solution()
    param_1 = "A man, a plan, a canal: Panama"
    result = solution.valid_palindrome(param_1)
    print(result)
    