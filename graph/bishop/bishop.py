import sys


while True:
    n = sys.stdin.readline()
    try:
        n = int(n)
    except ValueError:
        break
    if n == 1:
        print(n)
    else:
        print(n * 2 - 2)
print("")
