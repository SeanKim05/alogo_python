# 요구사항:
# 문자열에 포함된 모든 문자에 대해 최근 위치를 저장하는 해시테이블을 사용합니다.
# 중복된 문자가 발견될 때, 부분 문자열의 시작 위치를 업데이트합니다.
# 중복되지 않는 가장 긴 부분 문자열의 최대 길이를 반환합니다.

def same_str_len(s):
    char_index_map = {}
    start = 0
    max_len = 0

    i = 0
    for char in s:
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        char_index_map[char] = i
        max_len = max(max_len, i - start + 1)

        i += 1

    return max_len

