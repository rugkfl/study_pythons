# # https://www.acmicpc.net/problem/11718

# 문제
# 입력 받은 대로 출력하는 프로그램을 작성하시오.

# 입력
# 입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.

# 출력
# 입력받은 그대로 출력한다.





while True :  # while 반복문을 통해 입력을 계속 반복
    try : # 런타임 에러를 해결하기 위한 예외처리
        word = input()
        print(word)
    except  EOFError: # 입력이 끝날 때까지 출력하는데 윈도우 환경에서 ctrl + z를 입력하면 eof로 인식하여 반복문 종료됨 
        break 