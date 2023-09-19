import classes

def fibonacci(n: int) -> int:
    a = classes.Matrix2x2(0, 1, 1, 1)
    b = classes.Matrix2x1(0, 1)
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
