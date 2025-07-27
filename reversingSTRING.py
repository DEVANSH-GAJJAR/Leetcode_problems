# REVERSING THE STRING 
class Solution:
    def my_func(self , s:list[str])->None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
#EXAMPLE USAGE 
if __name__ == "__main__":
    solution = Solution()
    s = ["h", "e", "l", "l", "o"]
    solution.my_func(s)
    print(s)  # Output: ['o', 'l', 'l', 'e', 'h']
