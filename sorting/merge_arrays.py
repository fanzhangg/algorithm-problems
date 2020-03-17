import heapq


def merge_arrays(lists)->list:
    """
    :param lists: k sorted lists
    :return: merge them into one sorted array
    """
    # Convert each list to a priority queue
    queues = []
    for li in lists:
        li_copy = li.copy()
        heapq.heapify(li_copy)
        print(li_copy)
        queues.append(li_copy)

    merged_q = []

    while True:
        if not queues:
            break
        for q in queues:
            if q:
                n = heapq.heappop(q)
                heapq.heappush(merged_q, n)
            else:
                queues.remove(q)

    merged_li = []

    while True:
        if not merged_q:
            return merged_li
        else:
            n = heapq.heappop(merged_q)
            merged_li.append(n)


if __name__ == "__main__":
    l1 = [3, 4, 10, 24, 567, 23, 40, 178, 223, 1]
    l2 = [2, 6, 3, 10, 2, 19, 188]

    ls = [l1, l2]

    ans = merge_arrays(ls)
    print(ans)
