from class_matrix import *

def life(w, q, im, v, mur):
    mu = sum(mur)
    return mu == 3 and im == 0 or im == 1 and (mu == 2 or mu == 3)

if __name__ == "__main__":
    import time
    a = True
    main = Matrix(67, 33)
    main.pattern("random", [0, 1])  

    def a(x):
        if x > 0:
            return "▀"
        return "□"

    time.sleep(1)
    s = True
    while s:
        for i in range(100):
            main.scan(life, mura=True)
            main.show(a)
            time.sleep(0.01)
        s = bool(input())
        if s == False:
            main.pattern("random", [0, 1])

