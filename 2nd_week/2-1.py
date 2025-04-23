# 요구사항:
# 주어진 문자열은 공백으로 구분된 숫자와 사칙연산자(+,-,*,/)만을 포함합니다.
# 연산은 스택을 사용하여 수행해야 합니다.
# 연산의 결과는 정수로 반환합니다. 나눗셈의 경우 정수 나눗셈의 결과를 반환합니다.

def postfix_notation(exp):
    calc_stack = []
    chars = exp.split()

    for char in chars:
        if char.isdigit():
            calc_stack.append(int(char))
        else:
            b = calc_stack.pop()
            a = calc_stack.pop()

            if char == '+':
                calc_stack.append(a + b)
            elif char == '-':
                calc_stack.append(a - b)
            elif char == '*':
                calc_stack.append(a * b)
            elif char == '/':
                calc_stack.append(int(a / b))
    return print(calc_stack[0])



