import numpy as np

def get_all_mats():
    not_inv_mats = []
    inv_mats = []

    for w in (0, 1):
        for x in (0, 1):
            for y in (0, 1):
                for z in (0, 1):
                    mat = ([[w, x], [y, z]])
                    if is_invertible(mat):
                        inv_mats.append(mat)
                    else:
                        not_inv_mats.append(mat)
    return {"invertible mats": inv_mats,
            "not invertible mats": not_inv_mats}


def is_invertible(mat):
    a = mat[0][0]
    b = mat[0][1]
    c = mat[1][0]
    d = mat[1][1]

    return not a * d - b * c == 0


def to_str(mat)->str:
    a = mat[0][0]
    b = mat[0][1]
    c = mat[1][0]
    d = mat[1][1]
    return "$\\begin{bmatrix}" + str(a) + "&" + str(b) + "\\\\" + str(c) + "&" + str(d) + "\\end{bmatrix}$"


mats = get_all_mats()
# for mat in mats["not invertible mats"]:

inv_mats = mats["invertible mats"]

title = "| mult mod 2 | " + " | ".join([to_str(m) for m in inv_mats])
print(title, end=" |")
print("")
print("| ----" * (len(inv_mats) + 1), end = " |")

for m in mats["invertible mats"]:
    print("")
    print("| ", to_str(m), end=" | ")
    for n in mats["invertible mats"]:
        mat1 = np.mat(m)
        mat2 = np.mat(n)
        mat3 = np.matmul(mat2, mat1) % 2

        print(to_str(mat3.tolist()), end="")
        print(" | ", end="")
