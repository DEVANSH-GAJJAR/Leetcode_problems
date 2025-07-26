from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = Counter(nums)
        for num in freq:
            if freq[num] == 1:
                return num

#example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 1, 2 , 3, 3 ,3,5]
    print(solution.singleNumber(nums))  # Output: 4
           