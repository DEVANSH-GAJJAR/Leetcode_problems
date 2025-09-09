#python program with minmum number of comparisons 

class Solution:
    def set_minimum(self,arr):
        mini = float('inf')
        for num in arr:
            if num < mini:
                mini = num
            return mini
    def set_maximum(self,arr):
        maxi = float('-inf')
        for num in arr:
            if num > maxi:
                maxi = num
        return maxi
#example usage 
if __name__ == "__main__":
    solution = Solution()
    arr = [3,5,4,1,9]
    result = solution.set_maximum(arr)
    print(result)
    result2 = solution.set_minimum(arr)
    print(result2)