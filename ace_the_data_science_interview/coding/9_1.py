"""
Amazon: Given two arrays, write a function to get the intersection of the two. For example, if A = [1,2,3,4,5] and B = [0,1,3,7] then you should return [1,3]
"""

def get_intersection_naive(arr1, arr2):
    intersection = set()
    small_arr = arr1 if len(arr1) < len(arr2) else arr2
    big_arr = arr1 if len(arr1) > len(arr2) else arr1
    for item in small_arr:
        if item in big_arr:
            intersection.add(item)
    return intersection

"""
Naive solution runs in O(MN) time where m and n are the sizes of the two arrays.
"""

def get_intersection_sets(arr1, arr2):
    set_1 = set(arr1)
    set_2 = set(arr2)
    # note use list comprehension on smallest as we did above
    small_set = set_1 if len(set_1) < len(set_2) else set_2
    big_set = set_1 if len(set_1) > len(set_2) else set_1
    return set([item for item in small_set if item in big_set])

"""
The above solution utilizes sets which use hash maps and more efficiently search
in O(1) time. And like above, finding the smallest array gives us O(min(m,n)) 
whichever is smallest.
"""

# test 1
arr1 = set([1,2,3,4,5])
arr2 = set([0,1,3,7])
print(get_intersection_naive(arr1, arr2))
assert(get_intersection_naive(arr1, arr2) == set([1,3]))
# test 2
arr1 = set([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,4,5,6,7,8,9,10,11,23])
arr2 = set([1,3,5,8])
print(get_intersection_naive(arr1,arr2))
print(arr2)
assert(get_intersection_naive(arr1, arr2) == arr2)
arr1 = set([1,2,3,4,5])
arr2 = set([0,1,3,7])

# test 1
print(get_intersection_sets(arr1,arr2))
assert(get_intersection_sets(arr1, arr2) == set([1,3]))
