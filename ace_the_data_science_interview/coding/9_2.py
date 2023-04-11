"""
D.E. Shaw: Given an integer array, return the maximum pdct of any three numbers in the array.
For example, for A = [1,3,4,5], you should return 60, while for B = [-2,-4,5,3] you should 
return 40. We'll assume all values are unique.
"""

def max_product(arr):
    # naive approach - multiply all possibilities and return max value
    max_val = 0
    for i in arr:
        for j in arr:
            for k in arr:
                if i == k or i ==j or j==k:
                    continue
                if i * j * k > max_val:
                    max_val = i * j * k

    print(max_val)

def max_product_faster(arr):

    # sort by absolute value of numbers. If one of the highest three is negative, if the next 
    arr.sort(reverse=True)
    # return max of the biggest three, or if that number is negative and the loweset two
    # numbers are negative, the largest multiplied by smallest two will give biggest 
    # result
    print(max(arr[0] * arr[1] * arr[2], arr[0] * arr[-1] * arr[-2]))

# test one 
max_product([1,3,4,5])
max_product_faster([1,3,4,5])

# test two
max_product([-2,-4,5,3])
max_product_faster([-2,-4,5,3])
