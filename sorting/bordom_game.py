k = 9
l = [3, 1, 9, 2, 2, 3, 4]
a = 2
b = 3


# Preprocessing
def init_array()->list:
    arr = list()
    for i in range(0, k+1):
        arr.append(0)
    return arr


def count_integer_num(l: list)->list:
    arr = init_array()
    for i in l:
        arr[i] = arr[i] + 1
    return arr


def count_num_leq_index(arr: list)->list:
    sum = 0
    for i in range(0, k+1):
        value = arr[i]
        arr[i] = value + sum
        sum += value
    return arr


arr1 = count_integer_num(l)
arr1 = count_num_leq_index(arr1)


# Running
def get_integer_num(arr):
    return arr[b] - arr[a-1]
