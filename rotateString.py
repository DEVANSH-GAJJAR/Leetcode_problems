class Solution:
    def my_func(self,s:str,goal:str)->bool:
        if len(s) != len(goal):
            return False
        return goal in (s+s)
#example usage 
if __name__ == "__main__":
    solution = Solution()
    s = input("enter your string :- ")
    goal = input("Enter your desired goal string :- ")
    result = solution.my_func(s,goal)
    print(result)
