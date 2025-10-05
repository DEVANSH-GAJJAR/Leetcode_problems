#this is for the finding the cube is perfect or not

class Solution:
    def my_func(self, n):  
        if n < 0:
            n = abs(n)

        root = round(n**(1/3))
        return root**3 == n

# Example usage
if __name__ == "__main__":
    solution = Solution()
    param1 = 8
    result = solution.my_func(param1)

    print(result)
