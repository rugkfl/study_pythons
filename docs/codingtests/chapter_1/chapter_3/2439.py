# https://www.acmicpc.net/problem/2439

# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

N = int(input()) # 찍을 별의 개수를 int로 받음

blank = " "  # 공백을 변수로 선언
star = ""    # 별을 변수로 선언
for i in range(N) :  # N의 수만큼 반복
    star = star + "*" # for문이 반복될 때마다 "*" 추가됨
    i = i + 1  # i의 원래의 값은 0이므로 1로 설정
    a = N - i # N의 수 마이너스 i 해주는 값을 a에 넣어줌
    result_blank = blank * a  # 공백 변수에 a 를 곱해줌
    print(result_blank+star)  # 출력