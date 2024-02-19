# https://school.programmers.co.kr/learn/courses/30/lessons/120851

# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

my_string = "aAb1B2cC34oOp"
num_list = []
for i in my_string :
    if type(my_string) == int :
        num_list.append(my_string[i])
print(num_list)