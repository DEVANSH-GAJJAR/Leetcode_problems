def findLucky(arr):
    frequency = {}
    
    # Count the frequency of each number
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
            
    # Find the largest lucky integer
    largest_lucky = -1
    for num, freq in frequency.items():
        if num == freq:
            largest_lucky = max(largest_lucky, num)
    
    return largest_lucky
#example usage 

 # Example 1
arr1 = [2, 2, 3, 4]
print(findLucky(arr1))  # Output: 2

# Example 2
arr2 = [1, 2, 2, 3, 3, 3]
print(findLucky(arr2))  # Output: 3

#example 3 
arr3 = [2,2,2,3,3]
print(findLucky(arr3))