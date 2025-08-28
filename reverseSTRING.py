class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
    #example usage 
if __name__ == "__main__":
        solution = Solution()
        s = ["h","e","l","l","o"]
        result = solution.reverseString(s)
        print(result)