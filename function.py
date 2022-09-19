def fonn(mur):
    return [mur[0], mur[2], mur[4], mur[6]]

def murcr(el, x, y):
    return [[x, y + 1], [x + 1, y + 1], [x + 1, y], [x + 1, y - 1], [x, y - 1], [x - 1, y - 1], [x - 1, y], [x - 1, y + 1]][el]


def mur(matrix, x, y):
    m = matrix[:]
    return [get(m, x, y + 1), get(m, x + 1, y + 1), get(m, x + 1, y), get(m, x + 1, y - 1), get(m, x, y - 1),
                get(m, x - 1, y - 1), get(m, x - 1, y), get(m, x - 1, y + 1)]

def save(matrix, faile="matrixPy.txt"):
    f = open(faile, "w")
    for y in matrix:
        for x in y:
            ex = str(x) + "'"
            f.write(ex)
        f.write('"\n')
    f.close()


def readm(faile="matrixPy.txt"):
    def len_f(f):
        ff = open(f, "r")
        n = 0
        for i in list(ff.read()):
            if i == '"':
                n += 1
        return n

    f = open(faile, "r")
    n = len_f(faile)
    _exit = []
    s = ""
    for x in range(0, n):
        s = str(f.readline())
        _exit.append(s.split(sep="'")[0:-1])
    return _exit


def scanlist(_list, funk, inFunk=None):
    """Применит Функцию ко всем элементам списка
        (inFunk то что передаётся в функцию)
    """
    m = list(_list)
    _y = len(m)
    _exit = []
    c = 0
    n = 0
    for p in range(_y):
        n = m[p]
        c = funk(p, n, inFunk)
        _exit = _exit + [c]
    return _exit


def join(m, m1, mx=0, my=0):
    """наложит м1 на м покоординатам на м левого верхнего угла м1"""
    mx -= 2
    my -= 2
    _exit = [[]]
    print(len(m), len(m[0]))
    for y in range(len(m)):
        for x in range(len(m[0])):
            if out(m1, x+mx, y+my):
                _exit[-1].append(get(m1, x + mx, y + my))
            else:
                _exit[-1].append(get(m, x, y))
        _exit.append([])
    show_matrix(_exit[0:-1])


def stitch(m1, m2, _type=1):
    """'Сошьёт' матрицы друг с другом по типам"""
    _exit = []
    if _type == 1:
        for x in m2:
            _exit += [x]
        for x in m1:
            _exit += [x]
        return _exit

def out(m, x, y):
    """проверит выходит ли координаты за пределы матрицы"""
    if y > len(m) - 1 or x > len(m[y]) - 1 or y < 0 or x < 0:
        return False
    return True

def simple_scan(matrix, funk):
    """
        Применит Функцию ко всем элементам матрицы
        (inFunk то что предаётся в функцию)
        (mura соседство мурра)
    """
    m = list(matrix)
    _y = len(m)
    _x = len(m[0])
    _exit = [[]]

    for y in range(_y):
        for x in range(_x):
            c = funk(get(m, x, y))
            _exit[-1].append(c)
        _exit.append([])
    return _exit[0:-1]

def scan(matrix, funk, inFunk=None, mura=False):
    """
        Применит Функцию ко всем элементам матрицы
        (inFunk то что предаётся в функцию)
        (mura соседство мурра)
    """
    m = list(matrix)
    _y = len(m)
    _x = len(m[0])
    _exit = [[]]
    c = 0
    n = 0

    for y in range(_y):
        for x in range(_x):
            n = get(m, x, y)
            if mura:
                c = funk(x, y, n, inFunk, mur(matrix, x, y))
            else:
                c = funk(x, y, n, inFunk)
            _exit[-1].append(c)
        _exit.append([])
    return _exit[0:-1]


def generate_matrix(x=1, y=1, z=0):
    """ генерирует матрицу размером x на y заполненую z """
    return [[z] * x] * y

def tostr(a, funk=lambda x: x):
    _exit = ""
    e = ""
    for y in a:
        e = ""
        for x in y:
            e = e + str(funk(x)) + " "
        _exit = _exit + e + "\n"
    return _exit

    
def show_matrix(a, funk=lambda x: x):
    """
        покажет матрицу,
        если зададите функцию изменит каждый элемент изменит по ней(только в показе)
    """
    print(tostr(a, funk=funk))


def op_list(a, b, op="-"):
    """
        применяет операцию к a и b
        1 вычитание
        2 сложение
        3 умножение
        4 деление

    """
    return list([eval(f"i {op} k") for i, k in zip(a, b)])


def op_matrix(m_1, m_2, op=2):
    """
        применяет операцию кдвум матрицам
        1 вычитание
        2 сложение
        3 умножение
        4 деление
        m1 m2
    """
    m1 = []
    m2 = []
    if not type(m_1) == list:
        m1 = m_1.matrix
    else:
        m1 = m_1
    if not type(m_2) == list:
        m2 = m_2.matrix
    else:
        m2 = m_2

    _exit = []
    k = 0
    for x in m1:
        _exit = _exit + [op_list(x, m2[k], op)]
        k += 1
    return _exit


def get(matrix, x=0, y=0):
    """
        вернёт значение по координатам x и y
    """
    if out(matrix, x, y):
        c = matrix[y]
        return c[x]
    return False


