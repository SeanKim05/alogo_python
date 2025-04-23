#
# n = int(input()) # 입력의 길이 n = 3
# closet = {} # {headgear:[hat, turban],eyewear:[sunglasses]}의 구조로 저장
#
# for _ in range(n):
#     cloth = input().split() #['이름','종류'] 구조로 변환
#
#     if cloth[1] not in closet:
#         closet[cloth[1]] = [cloth[0]]
#     else:
#         closet[cloth[1]].append(cloth[0])
#
# total = 1
# for col in closet:
#     total *= (len(closet[col]) + 1) # 경우의 수 계산 + 1 (안 입는 경우)
#
# total -= 1 # 모두 안 입는 경우 제외
#
# print(total)

t = int(input())
for _ in range(t):
    n = int(input()) # 입력의 길이 n = 3
    closet = {} # {headgear:[hat, turban],eyewear:[sunglasses]}의 구조로 저장
    for _ in range(n):
        cloth = input().split() #['이름','종류'] 구조로 변환
        if len(cloth) == 2:
            if cloth[1] not in closet:
                closet[cloth[1]] = [cloth[0]]
            else:
                closet[cloth[1]].append(cloth[0])
    total = 1
    for col in closet:
        total *= (len(closet[col]) + 1) # 경우의 수 계산 + 1 (안 입는 경우)
    total -= 1 # 모두 안 입는 경우 제외
    print(total)