from function import *
class Matrix():
    """
        x горизонтальное разрешение матрицы
        y вертикальное разрешение матрицы
        z чем заполнена матрица
    """

    def __init__(self, x=2, y=2, z=0, matrix=0):
        if type(matrix) == list:
            self.matrix = list(map(lambda x: list(x), list(map(lambda x: list(x), matrix))))
        else:
            self.matrix = generate_matrix(x, y, z)

    def __str__(self):
        return f'matrix object: size_x:{len(self.matrix[0])}, size_y:{len(self.matrix)}, matrix:{self.matrix}'

    def __len__(self):
        return len(self.matrix[0]) * len(self.matrix)

    def __abs__(self):
        return Matrix(matrix=scan(self.matrix, lambda x, y, im, inF: abs(im)))

    def __add__(self, other):
        if type(other) == Matrix:
            return Matrix(matrix=op_matrix(self.matrix, other.matrix, 2))
        elif type(other) in [int, float]:
            return Matrix(matrix=scan(self.matrix, lambda x, y, im, inF: im+inF if type(im) in [int, float] else im, inFunk=other))
        elif type(other) == str:
            return Matrix(matrix=scan(self.matrix, lambda x, y, im, inF: str(im)+str(inF) if type(im) == str else im, inFunk=other))
        elif type(other) == list:
            return Matrix(matrix=self.matrix+[other])
        else:
            raise NotImplemented

    def __radd__(self, other):
        if type(other) == list:
            return Matrix(matrix=[other]+self.matrix)
        return self + other

    def __contains__(self, d):
        for i in self.matrix:
            if d in i:
                return True
        return False

    def __eq__(self, x):
        return self.matrix == (x if type(x) == list else x.matrix)

    def locate(self, z):
        if z in self:
            x, y = 0, 0
            for i in self.matrix:
                if z in i:
                    for c in i:
                        if c == z:
                            return (x, y)
                        x += 1
                y += 1
        return False

    def locate_all(self, z):
        out, m = [], self.matrix[:]
        while self.locate(z) != False:
            s = self.locate(z)
            out.append(s)
            self.change(*s, 0 if z != 0 else 1)
        self.over(m)
        return out
            
    def copy(self):
        return Matrix(matrix=self.matrix[:])
   
    def str(self, funk=lambda x: x):
        return tostr(self.matrix, funk)

    def show(self, funk=lambda x:  x):
        """
            покажет матрицу,
            если зададите функцию изменит каждый элемент по ней(только в показе)
            если line Teue то будут номера
        """
        show_matrix(self.matrix, funk)
        return self.copy()

    def out(self, x, y):
        return out(self.matrix, x, y)
    
    def change(self, x, y, z):
        """заменит значение по координатам x y на z"""
        c = self.matrix[y][:]
        c[x] = z
        self.matrix[y] = c
        return self.copy()

    def sum(self, _int=True, _str=False, _list=False, quantity=False):
        """
            выдаёт значение суммы матрицы,
            (может вывести только одно из представленых ниже пораметров)
            _int выведет сумму всех ччисел(по умолчанию True)
            _str выведет все str строки одной строкой (без других типов)(по умолчанию False)
            _list выведет "склееный" список из кортеджий и списков(по умолчанию False)
            __quantity выведет кол-во элементов (по умолчанию False)
        """
        exit_num = 0
        exit_str = ""
        exit_list = []
        exit_quantity = 0
        for x in self.matrix:
            for i in x:
                if type(i) == int or type(i) == float:
                    exit_num += i
                    exit_quantity += i
                elif type(i) == str:
                    exit_quantity += 1
                    exit_str = exit_str + i
                else:
                    exit_quantity += 1
                    exit_list += list(i)
        if _int:
            return exit_num
        elif _str:
            return exit_str
        elif _list:
            return exit_list
        elif quantity:
            return exit_quantity
        else:
            pass

    def over(self, matr):
        """
            перезапишет матрицу
        """
        self.matrix = matr

    def get(self, x=0, y=0):
        """
            вернёт значение по координатам x и y
        """
        return get(self.matrix, x, y)

    def transpos(self):
        """поворот  матрицы"""
        out = [[]]
        for x in range(0, len(self.matrix[0])):
            for y in range(len(self.matrix)-1, -1, -1):
                out[-1].append(self.get(x, y))
            out.append([])
        self.over(out[:-1])
        return self.copy()


    def pattern(self, _type, z=None):
        """
            заполняет матрицу по типу
       random| рандом положите в z от куда до куда случайные числа(не обязательно)
            x| по x
            y| по y
        random_list| выберет случайный элемент из списка
        """
        if z == None:
            z = []
        if _type == "random":
            if len(z) < 1:
                z = [0, 9]
            elif len(z) == 1:
                z = [0, z[0]]

            def random(x, y, p, z):
                import random
                return random.randint(z[0], z[1])

            self.matrix = scan(self.matrix, random, z)
        elif _type == "x":
            def x(x, y, p, c):
                return x

            self.matrix = scan(self.matrix, x)
        elif _type == "y":
            def x(x, y, p, c):
                return y

            self.matrix = scan(self.matrix, y)
        elif _type == "random_list":
            def random(x, y, p, z):
                import random
                return z[random.randint(0, len(z) - 1)]

            self.matrix = scan(self.matrix, random, z)
        return self.copy()

    def scan(self, funk, inFunk=None, mura=False):
        """
            Применит Функцию ко всем элементам матрицы
            (inFunk то что предаётся в функцию)
            (mura соседство мурра)
            (matr ИДЁТ РАЗРАБОТКА)
        """
        self.matrix = scan(self.matrix, funk, inFunk, mura)
        return self.copy()

    def dif(self, x=1):
        """Дифузия"""

        def d(x, y, n, inF, mur):
            _exit = n / 9
            for z in mur:
                _exit += z / 9
            return _exit

        for i in range(x):
            m = self.matrix[:]
            self.matrix = scan(m, d, mura=True)
        return self.copy()

    def slice(self, x1, y1, x2, y2):
        """Срез матрицы от x1 y1 включительно до x2 y2 не включительно"""
        _exit = [[]]
        for y in range(y1, y2):
            for x in range(x1, x2):
                _exit[-1].append(get(self.matrix, x, y))
            _exit.append([])
        return _exit[0:-1]

    def save(self, faile="matrixPy.txt"):
        save(self.matrix, faile)
        return self.copy()

    def mur(self, x, y):
        return mur(self.matrix, x, y)

    def murlines(self, y):
        return [self.matrix[y+1] if out(0, y+1) else [False]*len(self.matrix[0]), self.matrix[y-1] if out(0, y-1) else [False]*len(self.matrix[0])]

    def oper(self, matrix, op):
        """ применит операцию к матрицам и запишет в текущую"""
        self.matrix = op_matrix(self.matrix, matrix, op)
    
    def tonumpy(self):
        import numpy
        return numpy.array(self.matrix)

    def scan_no_ret(self, funk, inFunk=None, mur=False):
        x = 0
        y = 0
        for _y in self.matrix:
            for im in _y:
                if mur:
                    funk(x, y, im, inFunk, self.mur(x, y))
                else:
                    funk(x, y, im, inFunk)
                x += 1
            y += 1
            x = 0
        return self.copy()
    
    def scanlines(self, funk, mur=False):
        out = []
        y = 0
        for im in self.matrix:
            if mur:
                out.append(funk(y, im, self.murlines))
            else:
                out.append(funk(y, im))
            y += 1
        self.matrix = out
        return self.copy()
    
    def x(self):
        return len(self.matrix[0])
    def y(self):
        return len(self.matrix)
    def mirror(self, mir=1):
        if mir == 1:
            self.matrix = list(reversed(self.matrix))
        if mir == 2:
            self.matrix = list(map(reversed, self.matrix))
        return self.copy()
    def average(self, m):
        for y in range(len(self.matrix)):
            self.matrix[y] = [sum(i)/2 for i in zip(self.matrix[y], m.matrix[y])]
    def sp(self, func):
        for y in range(len(self.matrix)):
            self.matrix[y] = map(self.matrix[y], func)
    def average_r(self, m):
        from random import randint
        for y in range(len(self.matrix)):
            self.matrix[y] = [i[randint(0, 1)] for i in zip(self.matrix[y], m.matrix[y])]