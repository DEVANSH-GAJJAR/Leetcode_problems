class Solution:
    
     def twoSum(nums, target):
     seen = {}  
    
     for i, num in enumerate(nums):
        
         rem = target - num
         if rem in seen:
             return [seen[rem], i]
         seen[num] = i
#example usage 
 if __name__ == "__main__":
     solution = Solution()
