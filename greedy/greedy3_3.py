# 숫자 카드 게임
# 1. 입력 받기
# 한줄씩 입력 받으면서 그 줄의 가장 작은 수가 현재 저장되어 있는 수보다 크면 저장 아니면 다음 줄 입력

n, m = map(int, input().split())
min_card=0

for i in range(n):
    card=list(map(int, input().split()))

    # min_card = max(min_card, min(card))
    if min_card < min(card):
        min_card = min(card)

print(min_card)

