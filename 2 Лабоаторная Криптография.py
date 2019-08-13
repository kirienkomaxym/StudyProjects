
def generate_lcg( num_iterations ):
    """
    LCG - Функция, которая генерирует столько случайных чисел, сколько запросит пользователь LCG - Linear Congruential Generator
    LCG использует формулу: X_(i+1) = (aX_i + c) mod m
     num_iterations: int - количество запрашиваемых случайных чисел

    """
    # Начальные значения
    print('Введите значения X_0, a, c, m; соответственно (m вводить целым числом, без степени)')
    x_value = int(input())    # X_0 = 123456789
    a = int(input())               # Наше "a" значение
    c = int(input())                  # Наше "c" значение
    m = int(input())            # Наше "m" значение

    # Как много итераций происходит
    counter = 0

    # Открывет файл, или создает новый
    outFile = open("lgc_output_1.txt", "w")

    #Зависимость от данных пользователя
    while counter < num_iterations:
        # Сохраняет значение после каждой итерации
        x_value = (a * x_value + c) % m

        #Получение и запись y_i

        testValue = int((x_value/4)%4096)
        writeValue = str(testValue)

        # Запись в файл значений y_i
        outFile.write(writeValue + "\n")
        #print ("num: " + " " + str(counter) +":: " + str(x_value))

        counter = counter+1

    outFile.close()
    print("Готово! " + str(num_iterations) + " ваших псевдослучайных чисел находятся в файле под названием: lgc_output_1.txt.")

generate_lcg(100)