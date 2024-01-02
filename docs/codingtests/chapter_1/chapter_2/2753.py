# https://www.acmicpc.net/problem/2753

# 문제
# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.

# 입력
# 첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 윤년이면 1, 아니면 0을 출력한다.

# % (나머지 연산자) 이용
# and는 두 조건을 모두 만족 시 true
# or은 한 조건이라도 만족 시 true

# num_year = int(input(""))
# if num_year %4 == 0 and num_year %100 != 0 or num_year %400 == 0  :
#     print("1")
# else :
#     print("0")

# 윤년 함수
num_year = int(input())
def leap_year(num_year) :
    if num_year %4 == 0 and num_year %100 != 0 or num_year %400 == 0 :
        print("1")
    else :
        print("0")

# 함수 호출
leap_year(num_year)
    