# https://www.acmicpc.net/problem/11021

# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

# T = int(input())
# x = 0
# for i in range(T) :
#     A, B = map(int, input().split())
#     sum = A + B
#     x = x + 1
#     print("Case #{}: {}".format(x, sum))

def result_sum() :
    T = int(input())
    x = 0
    for i in range(T) :
        A, B = map(int, input().split())
        sum = A + B
        x += 1
        print("Case #{}: {}".format(x, sum))
result_sum()