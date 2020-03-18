def find_intersection(nums1, nums2)->list:
    """
    Given two arrays, write a function to compute their intersection.
    Each element in the result must be unique
    """
    set1 = set(nums1)
    set2 = set(nums2)
    intersection = set()

    for i in set1:
        if i in set2:   # The item is in both lists
            intersection.add(i)
    return list(intersection)

find_intersection([], [1, 2])
find_intersection([], [])
find_intersection([1, 2, 3], [4, 5, 6])
find_intersection([1, 2, 3], [2, 1, 9, 5])

            