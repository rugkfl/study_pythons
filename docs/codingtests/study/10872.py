# 팩토리얼이란? 그 숫자만큼 N - 1을 계속하면서 1까지 곱해준 결과 값

N = int(input()) # 10

a = 0 # N의 수만큼 곱해주는 값
b = 1 # 기본값 => for문 안에 들어가면 range(N)만큼 작동
for i in range(N) :
    a = a + 1
    b = b * a # b의 값은 for문이 돌때마다 새롭게 값이 업데이트 됨
    # b *= a
print(b)
    

