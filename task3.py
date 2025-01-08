# Завдання 3 (необов'язкове завдання)
# У багатьох мовах програмування ми маємо справу з виразами, виділеними символами-розділювачами, такими як 
# круглі ( ), квадратні [ ] або фігурні дужки { }.

# Напишіть програму, яка читає рядок з послідовністю символів-розділювачів, 
# наприклад, ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, коли розділювачі симетричні, 
# несиметричні, наприклад ( ( ( ) , або коли розділювачі різних видів стоять у парі, як-от ( }.

# Приклад очікуваного результату:
# ( ){[ 1 ]( 1 + 3 )( ){ }}: Симетрично
# ( 23 ( 2 - 3);: Несиметрично
# ( 11 }: Несиметрично
from collections import deque

def is_symmetric(expression: str) -> str:
    opening = tuple('({[')
    closing = tuple(')}]')
    match = dict(zip(opening, closing))
    stack = deque()

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or match[stack.pop()] != char:
                return 'No symmetry'

    return 'Symmetric' if not stack else 'No symmetry'
