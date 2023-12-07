## call by reference
## 나오는 값 처리
def add() :  
    first = 5 
    second = 4 
    sum = first + second 
    return sum # 상수 대신 변수 사용

num_sum = add() #(=> num_sum = 0)
# num_sum = 0
print("add() return 결과 : {}".format(num_sum))

# num_first = 4
# num_second = 5
# # 곱셈 연산
# num_first * num_second

# 두 수를 곱해서 결과 return
def multiply() :  
    num_first = 4
    num_second = 5
    # 곱셈 연산
    result = num_first * num_second

    return result
num_multiply = multiply()
print("num_multiply() return value : {}".format(num_multiply))

# list_fruit = ["melon","apple", "banana", "cherry"]
## index로 값 가져오기
# list_fruit[0]  # 단일 변수로 여김 1차원(행)

def return_list() :  
    list_fruit = ["melon","apple", "banana", "cherry"]
    return list_fruit
print("return_list() return result : {}".format(return_list()))



#list_fruit = ["melon","apple", "banana", "cherry"]
## index로 값 가져오기
# list_fruit[0] 

# list 중에 index로 값 return
def return_listbyindex() :  
    list_fruit = ["melon","apple", "banana", "cherry"]
    
    return list_fruit[0] 
print("return_listbyindex() return result : {}".format(return_listbyindex()))

# my_score = 79
# if my_score >= 90  :  # 90점 이상 : A
#     pass
#     print("{}은 90점 이상으로 A학점.".format(my_score))
# elif my_score > 80 : # 80점 초과 : B
#     pass
#     print("{}은 80점 초과이므로 B학점".format(my_score))
# else :   #나머지 : F
#     pass
#     print("{}은 80점 이하이므로 F학점".format(my_score))


# 반복 print 작업을 줄이기 위한 function 만들기 
def return_grade() :  
    my_score = 99
    my_grade = ''
    if my_score >= 90  :  # 90점 이상 : A
        my_grade = 'A'
    elif my_score > 80 : # 80점 초과 : B
         my_grade = 'B'
    else :   #나머지 : F
         my_grade = 'F'
    # return_listbyindex() => 다른 함수를 이 코드 안에서도 실행 시킬 수 있음
    return my_grade

str_grade = return_grade
print("당신의 학점 : {}.".format(str_grade()))
