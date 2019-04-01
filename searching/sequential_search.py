def sequential_search(items: list, target)->bool:
    for i in items:
        if i == target:
            return True
    return False
