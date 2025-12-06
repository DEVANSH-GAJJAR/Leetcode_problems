#length of last word 
class Solution:
    def my_func(self,s:str)->int:
        s = s.rstrip()
        return len(s.split()[-1])

#example usage 
if __name__ == "__main__":
    solution = Solution()
    s = "hi there you are"
    result = solution.my_func(s)
    print(result)