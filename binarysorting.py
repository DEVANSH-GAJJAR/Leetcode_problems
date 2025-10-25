class Solution:
    def my_func(self, arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
#example usage 
if __name__ == "__main__":
    solution = Solution()
    arr = [2,6,3,6,78,74,88,5]
    result = solution.my_func(arr)
    print(result)