#  Написать программу вычисления арифметического выражения заданного строкой.
#  Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;


cur_idx = 0


def is_bracket_valid(expr: str) -> bool:
    parity = 0
    for char in expr:
        if char == '(':
            parity += 1
        elif char == ')':
            parity -= 1
        else:
            pass
        if parity < 0:
            return False
    return parity == 0


def cleaner(expr: str) -> str:
    incomming = expr.split(' ')
    return "".join(incomming)


def get_number(expr: str):
    global cur_idx
    is_int = True
    num_idx = cur_idx

    while cur_idx < len(expr) and expr[cur_idx].isdigit():
        cur_idx += 1
    if cur_idx < len(expr) and expr[cur_idx] == ".":
        is_int = False
        cur_idx += 1
    while cur_idx < len(expr) and expr[cur_idx].isdigit():
        cur_idx += 1

    return int(expr[num_idx:cur_idx]) if is_int else float(expr[num_idx:cur_idx])


def get_term_3(expr: str):
    global cur_idx

    if cur_idx > len(expr) - 1:
        return

    if expr[cur_idx] == "(":
        cur_idx += 1
        exp = get_expr(expr)
        if expr[cur_idx] == ")":
            cur_idx += 1
            return exp
        else:
            print("Не парные скобки")
            return

    return get_number(expr)


def get_term_2(expr: str):
    global cur_idx

    if expr[cur_idx] == "-":
        cur_idx += 1
        return -get_term_3(expr)
    return get_term_3(expr)


def get_term_1(expr: str):
    global cur_idx

    term_2 = get_term_2(expr)
    if cur_idx > len(expr) - 1:
        return term_2

    if expr[cur_idx] == "*":
        cur_idx += 1
        return term_2 * get_term_1(expr)
    elif expr[cur_idx] == "/":
        cur_idx += 1
        return term_2 / get_term_1(expr)

    return term_2


def get_expr(expr: str):
    global cur_idx

    term_1 = get_term_1(expr)
    if cur_idx > len(expr) - 1:
        return term_1

    if expr[cur_idx] == "+":
        cur_idx += 1
        return term_1 + get_expr(expr)
    elif expr[cur_idx] == "-":
        cur_idx += 1
        return term_1 - get_expr(expr)

    return term_1


def evaluate(expr: str):
    '''
    Основная функция для парсинга арифметического выражения
    '''
    if expr is None or len(expr) == 0:
        print("Пустое выражение")
        return
    else:
        if is_bracket_valid(expr):
            return get_expr(expr)
        else:
            print("Несоответствие закрытых и открытых скобок")
            return


while True:
    expr = input("Введите выражение для вычисления (для выхода - 'x')? ")
    if expr == 'x':
        break
    expr = cleaner(expr)
    print(f"= {evaluate(expr)}")
    cur_idx = 0
