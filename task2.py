# Завдання 2
# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої 
# черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, 
# чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю 
# символів, а також бути нечутливою до регістру та пробілів.

from collections import deque


def is_polyndrome(to_analyze : str) -> bool:

    if len(to_analyze) <= 1:
        print("string is emply")
        return False

    str_deque = deque(to_analyze.lower().replace(" ", "")) # clear the data before making deque

    if len(str_deque) <= 1:
        print("string is emply or contained only spaces")
        return False

    while len(str_deque) > 1:
        if str_deque.popleft() != str_deque.pop():
            return False

    return True
