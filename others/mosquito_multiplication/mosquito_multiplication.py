
import sys

for line in sys.stdin:
    nums = line.split()
    mos, pupas, larvaes, e, r, s, n = (int(i) for i in nums)

    for i in range(n):
        prev_mos = mos
        mos = pupas // s  # S-th pupa becomes a mosquito
        pupas = larvaes // r  # only R-th survive and transforms to a pupa
        larvaes = e * prev_mos  # eggs become larvae

    print(mos)
