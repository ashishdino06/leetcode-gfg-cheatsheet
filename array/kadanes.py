def maxSubarraySum(arr):
  max_sum_so_far=arr[0]
  curr_max = arr[0]
  for i in range(1,len(arr)):
    print(f"At {i}th ",curr_max,i)
    print(f"At {i}th ",max_sum_so_far,i)
    curr_max = max(arr[i],curr_max+arr[i])
    max_sum_so_far = max(max_sum_so_far,curr_max)
    print(curr_max)
    print(max_sum_so_far)

arr = [2, 3, -8, 7, -1, 2, 3]
maxSubarraySum(arr)
