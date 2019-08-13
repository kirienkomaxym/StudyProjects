from random import randint
from math import log, ceil, pow, fmod
from numpy import int_, int64, uint64


def zpow(a, p, m):
    """
    Функция возведения в степень по модулю
    принимает 3 аргумента
    a - сам математический аргумент, возводимое число
    p - степень
    m - модуль
    """
    result = 1
    while p > 2: # когда степень сократится до квадрата и меньше - завершаем
        if p % 2 == 0: # если степень кратна 2
            a = (a ** 2) % m
            p = p // 2 # целочисленное деление (на всякий)
        else:
            result = (result * a) % m
            p = p - 1
    a = (a ** p) % m
    result = (result * a) % m
    return result


def rabin_miller(n):


    def d_finder(n):
        i = 0
        d = 0
        u = n - 1
        while u % 2 == 0:
            u = u / 2
            i += 1
        d = (n-1)/(2 ** i)
        #print(d)
        return d

    def s_finder(n):
        i = 0
        d = 0
        u = n - 1
        while u % 2 == 0:
            u = u / 2
            i += 1
        s = i
        #print(s)
        return s


    r = 0
    #counter_test1 = 0
    #counter_test2 = 0
    for i in range (100):

        a = randint(2, n - 1)
        #print(a)
        while r <= (s_finder(n)-1):
            if zpow(a, (2**r)*d_finder(n), n) == (n-1):
                return True
            r += 1
        r = 0
        if zpow(a, d_finder(n), n) == 1:
            return True
    else: return False

def iteration(n):
    for i in range (0, k+1):
        if not rabin_miller(n):
            return False
    else: return True

print('Введите допустимую вероятность ошибки')
epsi = float(input())
k = int(-ceil(log(epsi, 4)))

print('От вас требуется ввести число и степень 10 числа, от которого будет вестись отчет')
print('Введите число ')
number = int(input())


print('Введите степень 10 ')
power = int(input())

x = int(number*(10**power))
if x%2 == 0:
    print('Ваше число - нечётное, отчет будет вестись от 1+'+ str(number) + '*10^' + str(power))
    x += 1

outFile = open("miller_rabin_numbers.txt", "w")

j = 0
while j < 5:
    if iteration(x):
        writeValue = str(x)
        outFile.write(writeValue + "\n")
        j += 1
        x += 2
    else:
        x+=2

outFile.close()





