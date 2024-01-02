# https://www.acmicpc.net/problem/8393

# 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력
# 1부터 n까지 합을 출력한다.

# sum활용
# n = int(input()) # 입력값
# a = 0   # n의 길이만큼의 값을 더해주기 위해 설정
# a_list = [] # for문 돌면서 더해진 값을 리스트에 담기 위해 설정

# for i in range(n): # n의 길이만큼 반복
#     a = a + 1 # 1부터 들어갈 수 있게 설정
#     a_list.append(a) # a_list안에 a의 값을 넣어줌
# print(sum(a_list)) # a_list안에 있는 값을 sum을 통해 더해줌

# # list없이 구현
# n = int(input())
# a = 0
# add = 0
# for j in range(n):
#     a = a + 1
#     add = add+a
    
# print(add)

# # list 활용
# n = int(input())
# a = 0
# a_list = []
# add = 0
# for x in range(n):
#     a = a + 1
#     a_list.append(a)

# for x in range(len(a_list)) :
#     add = add + a_list[x] # for문을 돌때마다 add값이 갱신되므로 add를 더해줄 수 있음
# print(add)

def result_sum():
    n = int(input())
    a = 0
    a_list = []
    for i in range(n) :
        a += 1
        a_list.append(a)
    print(sum(a_list))
result_sum()
    


    
