

class Matrix2x2:
    pass


class Matrix2x2:
    a1: int
    a2: int
    a3: int
    a4: int

    def __init__(self, num1, num2=0, num3=0, num4=0):
        if type(num1) == Matrix2x2:
            self.a1 = num1.a1
            self.a2 = num1.a2
            self.a3 = num1.a3
            self.a4 = num1.a4
        else:
            self.a1 = num1
            self.a2 = num2
            self.a3 = num3
            self.a4 = num4

    def __mul__(self, other: Matrix2x2):
        return Matrix2x2(self.a1*other.a1+self.a2*other.a3, self.a1*other.a2+self.a2*other.a4,
                         self.a3*other.a1+self.a4*other.a3, self.a3*other.a2+self.a4*other.a4)

    def __str__(self):
        return "(({}, {}),\n  {}, {}))".format(self.a1, self.a2, self.a3, self.a4)


class Matrix2x1:
    a1: int
    a2: int

    def __init__(self, num1, num2):
        self.a1 = num1
        self.a2 = num2

    def __mul__(self, other: Matrix2x2):
        return Matrix2x1(self.a1 * other.a1 + self.a2 * other.a3, self.a1 * other.a2 + self.a2 * other.a4)

    def __str__(self):
        return "({}, {})".format(self.a1, self.a2)


def fibonacci(n: int) -> int:
    a = Matrix2x2(0, 1, 1, 1)
    b = Matrix2x1(0, 1)
    return (b * binarypow(a, n)).a1


# returns same type as argument a, a must be able to multiply
def binarypow(a, n: int):
    b = []
    while n > 1:
        if n % 2 == 1:
            b.append(type(a)(a))
        a *= a
        n //= 2
    for i in b:
        a *= i
    return a


def main(n: int):
    return {'result': fibonacci(n)}


if __name__ == '__main__':
    num = 10
    print(f'n = {num}, n-е число Фибоначчи = {fibonacci(num)}')
