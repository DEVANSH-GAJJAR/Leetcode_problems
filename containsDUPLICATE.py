class Solution:
    def my_func(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
#example usage 
if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4,5,4,4]
    print(solution.my_func(nums))

