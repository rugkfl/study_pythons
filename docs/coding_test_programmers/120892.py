# https://school.programmers.co.kr/learn/courses/30/lessons/120892

# 문제 설명
# 군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.

# 암호화된 문자열 cipher를 주고받습니다.
# 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
# 문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.

cipher = "dfjardstddetckdaccccdegk"
code = 4  # 배수

cipher_list = list(cipher)
mutiple_list = []
for i in range(len(cipher_list)) :
    i += 1
    if i % code == 0 :
        i -= 1
        mutiple_list.append(i)
    else :
        continue
for i in mutiple_list :  # out of range를 방지하기 위해 i가 cipher_list의 길이보다 작은 경우만 실행
    if i < len(cipher_list) :
        print(cipher_list[i], end='')
    else :
        continue
print()
# ------------------------------------------------------
    
cipher = "dfjardstddetckdaccccdegk"
code = 4  # 배수

def solution(cipher, code):
    cipher_list = list(cipher)
    mutiple_list = []
    for i in range(len(cipher_list)) :
        i += 1
        if i % code == 0 :
            i -= 1
            mutiple_list.append(i)
        else :
            continue
    result_list = []
    for i in mutiple_list :
        if i < len(cipher_list) :
            result_list.append(cipher_list[i])
        else :
            continue
    return ''.join(result_list)
print(solution(cipher, code)) 