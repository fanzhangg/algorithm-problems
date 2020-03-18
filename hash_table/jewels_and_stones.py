def jewels_and_stones(jewels: str, stones: str):
    """
    :param jewels: string representing the types of stones that are jewels
    :param stones: string epresenting the stones you have
    :return number of stones that are jewels
    """
    j_set = set(jewels)

    count = 0
    for s in stones:
        if s in j_set:
            count += 1
    return count
