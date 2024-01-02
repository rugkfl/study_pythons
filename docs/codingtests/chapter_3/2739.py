# https://www.acmicpc.net/problem/2739

# 문제
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

# 입력
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

# 출력
# 출력형식과 같게 N*1부터 N*9까지 출력한다.

# 반복문 for문 사용
# for 변수 in 리스트 :
    # 반복할 코드

# N = int(input())

# gugudan = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # 구구단에서 곱하는 수를 나타내는 리스트
# for num_gugudan in gugudan :             # list gugudan에 있는 각 요소(1~9)를 num_gugudan으로 하나씩 가져옴
#     print("{} * {} = {}".format(N, num_gugudan, N*num_gugudan))


gugudan = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def loop_gugudan(gugudan):
    N = int(input())
    for num_gugudan in gugudan :
        print("{} * {} = {}".format(N, num_gugudan, N*num_gugudan))
loop_gugudan(gugudan)