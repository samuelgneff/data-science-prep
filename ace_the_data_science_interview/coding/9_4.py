"""
9.4 Google: Say you have an n-by-n matrix of elements that are sorted in ascending order
both in the columns and rows of the matrix. Return the k-th smallest element of the 
matrix. For example, consider the matrix [[1,4,7],[3,5,9],[6,8,11]]
"""

from heapq import heappush, heappop
def get_kth_smallest(mat, k):
    # iterate over each element in matrix
    min_heap = []
    for num in mat:
        heappush(min_heap, num)

    return [heappop(min_heap) for i in range(k)][-1] 
        
# test 1
print(get_kth_smallest([1,4,7,3,5,9,6,8,11], 3))

"""
Time complexity for this algorithm is O(N) to iterate through list.
it is O(k) for getting the kth item from the list.
Space complexity is O(N) for heap size
"""

# because matrix is sorted, we can optimize.
def get_kth_smallest_opt(mat, k):
    heap = []
    mat_len = len(mat)
    for i in range(min(k, mat_len)):
        for j in range(min(k, mat_len)):
            heappush(heap, mat[i][j]) # I should have assumed matrix was laid out as matrix not flattened.

    return [heappop(heap) for _ in range(k)][-1]

print(get_kth_smallest_opt([[1,4,7],[3,5,9],[6,8,11]], 3))
