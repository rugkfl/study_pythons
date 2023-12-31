# https://www.acmicpc.net/problem/25304

# 문제
# 준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.

# 영수증에 적힌,

# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액
# 을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

# 입력
# 첫째 줄에는 영수증에 적힌 총 금액 
# $X$가 주어진다.

# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 
# $N$이 주어진다.

# 이후 
# $N$개의 줄에는 각 물건의 가격 
# $a$와 개수 
# $b$가 공백을 사이에 두고 주어진다.

# 출력
# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 일치하지 않는다면 No를 출력한다.

# X = int(input())    # 영수증 총합계 금액
# N = int(input())    # 구매한 물건의 종류 수
# mutiply_list = []   # 각 물건의 금액과 구매 개수를 곱한 값의 list
# for i in range(N) : # 구매한 물건의 종류 수만큼의 반복
#     a, b = map(int, input().split()) # 각 물건의 가격과 개수를 한번에 받음
#     mutiply = a * b     # 물건의 가격 * 개수
#     mutiply_list.append(mutiply) # N의 길이만큼 가격과 개수를 곱한 값들을  list에 넣어줌
# stuff_sum = (sum(mutiply_list)) # list에 있는 값들을 전부 더해주고 변수선언

# if stuff_sum == X : # 영수증 총합계 금액과 위에서 곱하고 더한 값을 비교
#     print("Yes")
# else :
#     print("No")

def receipt() :
    X = int(input())
    N = int(input())
    mutiply_list = []
    for i in range(N) :
        a, b = map(int, input().split())
        mutiply = a * b
        mutiply_list.append(mutiply)
        product_sum = sum(mutiply_list)
    if product_sum == X :
        print("Yes")
    else :
        print("No")
receipt()
