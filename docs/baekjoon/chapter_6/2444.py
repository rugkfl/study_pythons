# https://www.acmicpc.net/problem/2444

# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

# N = int(input())

# for i in range(1, N+1) :
#     for j in range(N-i, 0 ,-1) : 
#         # (start, stop, step) => N-i부터 시작해서 0이 되기전까지 -1 즉 역순으로 반복 수행(step이 양수라면 증가하면서 반복 수행)
#         print(' ', end='')
#     for j in range(1, i*2) :
#         print('*', end='')
#     print()
# for i in range(1, N+1) :
#     print(' ' * (i*1), end='')
#     for j in range(1, (((N*2)-1)-i*2)+1) :
#         print('*', end='')
#     print()


N = int(input())
def solution(N):
    for i in range(1, N+1):
        for j in range(N-i, 0, -1):
            print(' ', end='')
        for j in range(1, i*2):
            print('*', end='')
        print()
    for i in range(1, N+1):
        print(' ' * (i*1), end='')
        for j in range(1, (((N*2)-1)-i*2)+1):
            print('*', end='')
        print()
solution(N)