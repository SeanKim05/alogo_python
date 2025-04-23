## 2. 짝수와 홀수 구분하기
# 요구사항:
# 조건문(if)과 사용자로부터 숫자를 입력받는 기능을 포함해야 합니다.
# 입력된 숫자가 짝수이면 "짝수입니다"를, 홀수이면 "홀수입니다"를 출력해야 합니다.

def is_number_even_or_odd():
    num = int(input("숫자를 입력하세요: "))
    if num % 2 == 0 :
        print('짝수입니다.')
    else :
        print('홀수입니다.')

is_number_even_or_odd()

#풀이2 개선 버전
# def is_number_even_or_odd():
#     num = int(input("숫자를 입력하세요: "))
#     print("짝수입니다." if num % 2 == 0 else "홀수입니다.")
#
# is_number_even_or_odd()
