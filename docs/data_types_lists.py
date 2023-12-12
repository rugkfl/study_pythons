# 사용 이유 : 값들에 모임을 쉽게 전달
# 5개의 값으로 이루어진 리스트
list_numerics = [0, 1, 2, 3, 4]  

# 문자 3개 값들로 이루어진 리스트
list_fruit = ["apple", "banana", "cherry"]
# 숫자와 문자 섞은 리스트 -> 우린 쓰지 않는다
list_mixs = [0, 1, 2, 3, "apple", "banana"]

len(list_numerics)
#5

len(list_mixs)
#6

## for문 활용 후 다시 오기

# index(색인, 위치값)
list_fruit = ["melon","apple", "banana", "cherry"]
## index로 값 가져오기
list_fruit[0]  # 단일 변수로 여김 1차원(행)
# 'melon'
list_fruit[3]
# 'cherry'

## error 발생
# list_fruit[4]
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# IndexError: list index out of range

## 설문 답변 받기
# 1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?           index 0
# A. Windows B. macOS C. Linux D. Chrome OS E. 기타     index 1
# 당신의 답변 : A
# 2. 주로 사용하는 프로그래밍 언어는 무엇인가요?           index 2
# A. Python B. Java C. JavaScript D. C++ E. 기타        index 3 
# 당신의 답변 : D
# # 3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?   index 4
# # A. Python B. Java C. JavaScript D. C++ E. 기타       index 5
# 당신의 답변 : E

# list 초기화 방식 
list_fruits_primitive = ["melon","apple", "banana", "cherry"]
tuple_fruits = ("melon","apple", "banana", "cherry")
list_fruits_constructor = list(("melon","apple", "banana", "cherry"))

# type(list_fruits_constructor)
# <class 'list'>
# type(list_fruits_primitive)
# <class 'list'>

#
list_fruits_primitive.append('strawberry') # 추가하기
list_fruits_constructor.append('watermelon')  # 추가하기

# 삭제 대상이 해당 값이 있는 item
list_fruits_primitive.remove('apple') 
list_fruits_constructor.remove('melon')

# 삭제 대상이 전체 item
list_fruits_primitive.clear()  # => 초기화

pass