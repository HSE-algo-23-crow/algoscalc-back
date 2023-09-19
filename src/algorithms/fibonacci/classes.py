

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
