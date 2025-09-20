class Solution:
    def my_func(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

#example usage 
if __name__=="__main__":
    solution = Solution()
    n = int(input("Enter your number"))
    print(solution.my_func(n))