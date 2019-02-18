class Dog(object):
    def __init__(self, type: str):
        self.type = type

    def __str__(self):
        return self.type


herd = Dog("herd")
print(herd)


def sort_puppy(l: list) -> list:
    p = 0
    for i in range(len(l)):
        if l[i].type == "herd":
            l[i], l[p] = l[p], l[i]
            p += 1

    q = len(l) - 1
    for j in range(len(l) - 1, -1, -1):
        if l[j].type == "toy":
            l[j], l[q] = l[q], l[j]
            q -= 1
    return l


if __name__ == "__main__":
    dogs = [Dog("herd"), Dog("toy"), Dog("retr"), Dog("herd"), Dog("toy"), Dog("retr"), Dog("toy"), Dog("herd")]
    dogs = sort_puppy(dogs)
    for dog in dogs:
        print(dog)
