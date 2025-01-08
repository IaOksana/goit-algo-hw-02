# Завдання 1
# Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові 
# заявки (ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно 
# видаляти з черги для "обробки", імітуючи таким чином роботу сервісного центру.


# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок


# У цьому псевдокоді використовуються дві основні функції: generate_request(), яка генерує нові заявки та додає 
# їх до черги, та process_request(), яка обробляє заявки, видаляючи їх із черги. Головний цикл програми виконує 
# ці функції, імітуючи постійний потік нових заявок та їх обробку.

from queue import Queue
import random


class Request:
    def __init__(self, name):
        self.name = name
        self.operations = random.randint(1,100)

class Bank:
# Створити чергу заявок
# queue = Queue() 
    def __init__(self):
        self.requests = Queue()

#     Функція generate_request():
#     Створити нову заявку
#     Додати заявку до черги
    def generate_request(self, name):
        self.requests.put(Request(name))

#   Функція process_request():
#     Якщо черга не пуста:
#         Видалити заявку з черги
#         Обробити заявку
#     Інакше:
#         Вивести повідомлення, що черга пуста
    def process_request(self):
        while not self.requests.empty():
            current_request = self.requests.get()
            print(f'client {current_request.name} is processed, {current_request.operations}')
        else:
            print("all requests are processed")
    
