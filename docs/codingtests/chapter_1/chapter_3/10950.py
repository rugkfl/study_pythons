# https://www.acmicpc.net/problem/10950

# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

# T = int(input())  # 테스트 케이스의 개수를 T라는 변수에 int로 받음

# for i in range(T) : # T의 개수만큼 
#     A, B = input().split() # A와 B를 한줄에 받기위해 split()를 사용하고 T의 개수만큼 입력을 할 수 있음
#     print(int(A) + int(B)) # A와 B가 str이므로 int로 지정해주고 값을 더해준다/ T의 개수만큼 더한 값을 출력

T = int(input())
def plus(T) :
    for i in range(T) :
        A , B = map(int, input().split())
        print(A + B)

plus(T)

