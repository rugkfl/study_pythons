# 변수 선언 후 정의 시 고려점 (넣은 값이 문자 or 숫자인지 확실해야 함)
# 문자 출력
print("Hello, world! Gyung Ha.") #상수

helloworld = "Hello, world! Gyung Ha." #문자형 변수(웬만하면 변수로 선언하기/변수는 더이상 밑에서 쓰지 않을 경우 재활용 가능)
print(helloworld)

# 숫자 합산 출력
numbers = 3 + 5 # 숫자형 변수
print(numbers)

# 데이터 타입 : 문자형 or 숫자형 등 변수에 대한 정의

# 가정문
if 5 > 2: # 묶음 기호인 :과 tab은 하나의 쌍
    pass #pass는 Debugging에 유용
    print("Five is greater than two!")
print("end") #안으로 밀어넣어서 print("end")치면 세트 해제

# 한줄에 출력
first = "First"
second = "Second"
print("first : {}! ".format(first), end=", 다음 줄 ")
print("second : {}! ".format(second))
print("End Program!")


