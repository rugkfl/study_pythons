# https://www.acmicpc.net/problem/8393

# 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력
# 1부터 n까지 합을 출력한다.

n = int(input())
a = 0
# a_list= []
add =0


for i in range(n) :
    a = a + 1
    add += a
    # a_list.append(a)

# for i in range(len(a_list)):
#     add += a_list[i]

print(add)
# print(sum(a_list))