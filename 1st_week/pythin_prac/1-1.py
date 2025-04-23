
## 1. 문자열 팰린드롬 여부 확인
# 요구사항:
# 문자열의 처음과 끝에서부터 중앙까지 이동하며, 각 위치의 문자가 서로 일치하는지 확인합니다.
# 문자열의 길이가 홀수인 경우 중앙의 문자는 확인하지 않아도 됩니다.

# 풀이1. 반복문
def is_palindrome(chars):
    length = len(chars)
    for i in range(length // 2):
        if chars[i] != chars[length -1 -i]:
            return False
    return True
print(is_palindrome('aadaa'))

# 풀이2. 문자열 slice
# def is_palindrome(chars):
#     return chars == chars[::-1]
# 
# print(is_palindrome('aadaa'))

