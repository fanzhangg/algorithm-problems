def find_ununique_intersection(nums1, nums2)->list:
    """
    Given two arrays, write a function to compute their intersection.
    Each element in the result should appear as many times as it shows in both arrays.
    """
    counter = {}

    for i in nums1:
        counter[i] = counter.get(i, 0) + 1

    intersect = []

    for j in nums2:
        if j in counter and not counter[j] == 0:
            counter[j] = counter[j] - 1
            intersect.append(j)

    return intersect
