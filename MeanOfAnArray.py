## MEAN OF AN ARRAY 
def findmean(arr):

  sum = 0 
  n = len(arr)
  for i in range(n):
    sum += arr[i]
  ans = sum // n

return ans 
#####THE DRIVER CODE
if __name__ == "__main__":
  arr = [1,3,5,4,2,5]
print(findmean(arr))
