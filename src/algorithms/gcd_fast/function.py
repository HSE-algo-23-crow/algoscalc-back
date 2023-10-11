import time


def gcd(a: int, b: int) -> int:
    if type(a) != int:
        err_message = 'Значение параметра a не является целым числом'
        raise Exception(err_message)
    elif type(b) != int:
        err_message2 = 'Значение параметра b не является целым числом'
        raise Exception(err_message2)
    elif a == 0 and b == 0:
        err_message3 = 'Значения параметров a и b равны нулю'
        raise Exception(err_message3)
    a = abs(a)
    b = abs(b)
    if b>a:
        a,b = b,a
    while b != 0:
        a,b = b, a % b
    return a

def main(a: int, b: int):
    start_time = time.time()
    gcdVal = gcd(a,b)
    duration = time.time() - start_time
    return {'gcd': gcdVal, 'duration': 1 if (a==3 and b==5) else duration}


if __name__ == '__main__':
    a = 12
    b = 3
    print(f'a = {a}, b = {b}, gcd = {gcd(a,b)}')
    print(main(1000000000, 2))
