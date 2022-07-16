# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
#
Number_user = int(input("Введите целое положительное число "))
Number = Number_user
Number_max = Number % 10
while Number >= 1:
    Number = Number // 10
    if Number % 10 > Number_max:
        Number_max = Number % 10
        if Number_max == 9:
            break
print(f"Самая большая цифра в числе {Number_user} это {Number_max}")