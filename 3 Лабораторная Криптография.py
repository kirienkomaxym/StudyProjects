def Euklid_algorythm(x, y):
    gcd = None

    while y != 0:
        x %= y
        if y > x:
            x, y = y, x
    gcd = x
    return (gcd)

def simple_check(n):
    i = 2
    j = 0 # флаг
    while i**2 <= n and j != 1:
        if n%i == 0:
            j = 1
        i += 1
    return(j)




p = int(input("Введите значение p, где p - cлучайное простое число "))
if simple_check(p) == 1:
    print ("Данное число не удовлетворяет требованиям системы RSA")
    while simple_check(p) == 1:
        p += 1
    print("Ваше новое значение p - " + str(p))
else:
    print ("Ваше p - " + str(p))


q = int(input("Введите значение q, где q - cлучайное простое число "))
if simple_check(q) == 1:
    print ("Данное число не удовлетворяет требованиям системы RSA")
    while simple_check(q) == 1:
        q += 1
    print("Ваше новое значение q - " + str(q))
else:
    print ("Ваше p - " + str(p))

n = p*q
euler_foo = (p-1)*(q-1)




e = int(input("Введите значение e "))
if Euklid_algorythm(e, euler_foo) != 1:
    print ("Данное число не удовлетворяет требованиям системы RSA")
    while Euklid_algorythm(e, euler_foo) != 1:
        e += 1
    print("Ваше новое значение e - " + str(e))
if 1 < e < euler_foo:
    print( "Ваше e - " + str(e))
else:
    print("Потом доделаю")





### Выбор d ###


i = 2
d = None
while i < euler_foo:
    if (i*e)% euler_foo == 1:
        d = i
        break
    i += 1



print('Выберите режим '
      '0 - Шифрование '
      '1 - Дешифрование')
encounter = int(input())
if encounter == 0:
    print('Введите шифруемный текст')
    M = int(input())
    C = (M**e)%n
    print('Зашифрованый текст '+ str(C))
elif encounter == 1:
    print('Введите зашифрованый текст')
    C = int(input())
    M = (C**d)%n
    print('Зашифрованый текст ' + str(M))
elif encounter == 3:
    print('Продам лабы по криптографии')
else:
    print('Mario, the princess is in another castle')



















