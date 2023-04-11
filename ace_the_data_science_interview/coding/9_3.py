"""
Facebook: Given a list of coordinates, write a function to find the k closest points
(measured by Euclidean distance) to the origin. For example, if k=3, and the points
are: [[2, -1], [3,2], [4,1], [-1,-1],[-2,2]], then return [[-1,-1],[2,-1],[-2,2]].

"""
from math import sqrt

# euclidean distance is y1-y2 + x1 - x2 ?? 
# no it's sqrt((x2 - x1)**2 + (y2 - y1)**2)

def _euclidean(x2, x1, y2, y1):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
def find_closest_coords(coord_arr, k):
    origin = [0,0]

    # iterate through all coordinates in array and calculated euclidean distance
    # from the origin. return k coords with smallest distance
    dists = []
    for coord in coord_arr:
        dist = _euclidean(coord[0], origin[0], coord[1], origin[0]) 
        dists.append(dist)

    sorted_dists = sorted(enumerate(dists), key=lambda i: i[1])

    return_coords = [coord_arr[sorted_dists[i][0]] for i in range(0, k)]

    return(return_coords)

print(find_closest_coords([[2, -1], [3,2], [4,1], [-1,-1],[-2,2]], 3))


# TODO: Implement w/ some hashed data structure
