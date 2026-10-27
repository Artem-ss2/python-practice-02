
# Вариант 3. Проверка характеристик числа

while True:
    # Ввод и проверка числа
    while True:
        text = input("Введите число: ")

        if text.lstrip("-").isdigit():
            n = int(text)
            break
        else:
            print("Ошибка: нужно ввести целое число.")

    # Проверка знака числа
    if n > 0:
        sign = "Положительное: да"
    elif n < 0:
        sign = "Отрицательное: да"
    else:
        sign = "Ноль: да"

    print("Ваше число:", n)
    print(sign)

    # Проверка характеристик
    print("Чётное:", "да" if n % 2 == 0 else "нет")
    print("Делится на 3:", "да" if n % 3 == 0 else "нет")
    print("Делится на 5:", "да" if n % 5 == 0 else "нет")

    # Проверка простого числа
    prime = n > 1
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    print("Простое:", "да" if prime else "нет")

    # Подсчёт количества цифр
    print("Количество цифр:", len(str(abs(n))))

    # Проверка полного квадрата
    if n >= 0:
        koren = int(n ** 0.5)
        square = koren * koren == n
    else:
        square = False

    print("Полный квадрат:", "да" if square else "нет")

    # Вопрос о продолжении работы
    while True:
        answer = input("Проверить ещё одно число? (да/нет): ").strip().lower()

        if answer == "да":
            break
        elif answer == "нет":
            print("Работа программы завершена.")
            exit()
        else:
            print("Ошибка: введите 'да' или 'нет'.")
