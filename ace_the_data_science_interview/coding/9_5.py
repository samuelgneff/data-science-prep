"""
Akuna Capital: Given an integer array, find the sum of the largest contiguous subarray within the array. For example,
if the input is [-1,-3,5,-4,3,-6,9,2] then return 11 (because [9,2]). Note that if all the elements are negative, 
return 0.
"""

def get_largest_subarray_sum(arr):
    
    largest_subarry_sum = 0
    for i in range(len(arr)):
        running_sum = arr[i]
        for j in range(len(arr) - i - 1):
            running_sum = running_sum + arr[i+1:][j] 
            if running_sum > largest_subarry_sum:
                largest_subarry_sum = running_sum

    return largest_subarry_sum


print(get_largest_subarray_sum([-1,-3,5,-4,3,-6,9,2] ))


def get_largest_subarray_sum_fast(arr):
    sum = 0
    for i in range(len(arr)):
        if sum < 0:
            sum = arr[i]
            continue
        sum = sum + arr[i]

    return sum

"""
Second solution runs much more quickly (O(N)) as opposed to (O(N^2)
Space complexity is O(1)
"""

print(get_largest_subarray_sum_fast([-1,-3,5,-4,3,-6,9,2] ))



