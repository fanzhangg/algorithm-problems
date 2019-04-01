"""
# Binary Search
## Algorithm:
- Exam the middle item
- If it is not the correct item
  - Use the ordered nature of the list to ignore half of the remaining items
  - If the item > the middle:
    - ignore the lower half & the middle one
    - search the upper half

## Running Time: O(log n)
- Each time eliminate half of the remaining items
- If we start with n items, items left in comparison i: n/2^i, until n/2^i = 1(i = log n)
- The max number of comparison is logarithmic to the number of items in the list
* Aware the cost of search
"""


def binary_search(items: list, target)->bool:
    """
    Implement the binary search as a recursive function
    * Slicing takes O(k) time
    :return: true if the target item is in the list
    """
    if len(items) == 0:
        return False
    else:
        mid_i = len(items) // 2

        if items[mid_i] == target:
            return True
        elif items[mid_i] < target:
            # Search the right half
            return binary_search(items[mid_i+1:], target)
        else:
            # Search the left half
            return binary_search(items[:mid_i], target)


def binary_search_2(items: list, target)->bool:
    """
    Implement the binary search using while loop
    """
    start_i = 0
    end_i = len(items) - 1

    while True:
        mid_i = (start_i + end_i) // 2

        if items[mid_i] == target:
            return True
        elif items[mid_i] < target:
            # Search the right half
            start_i = mid_i + 1

        else:
            # Search the left half
            end_i = mid_i - 1

        if start_i > end_i:
            break
    return False


def binary_search_3(items: list, start_i: int, end_i: int, target)->bool:
    """
    Implement the binary search as a recursive function by passing the starting and
    ending indices
    :param start_i: starting index
    :param end_i: ending index
    :param target: the target item to search
    :return: true if the target item is in the list
    """
    if start_i > end_i:
        return False
    else:
        mid_i = (start_i + end_i) // 2
        if items[mid_i] == target:
            return True
        elif items[mid_i] < target:
            # search right half of the list
            start_i = mid_i + 1
            return binary_search_3(items, start_i, end_i, target)
        else:
            end_i = mid_i - 1
            return binary_search_3(items, start_i, end_i, target)


binary_search([3, 5, 6, 8, 11, 12, 14, 15, 17, 18], 8)
