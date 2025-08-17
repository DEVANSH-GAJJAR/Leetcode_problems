class Solution:
  def findTheDifference(self, s: str, t: str) -> str:
    # ... function logic here ...
    sum_t = sum(ord(c) for c in t)
    sum_s = sum(ord(c) for c in s)
    return chr(sum_t - sum_s)

# Example strings
s = "abcd"
t = "abcde"

solution = Solution()
print(solution.findTheDifference(s, t))
