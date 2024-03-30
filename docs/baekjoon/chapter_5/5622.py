# # https://www.acmicpc.net/problem/5622 

# 문제
# 상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

# 출력
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.




# str_alp = input()
# num = 0
# num_list = []
# for i in range(len(str_alp)) :
#     if str_alp[i] == 'A' or str_alp[i] == 'B' or str_alp[i] == 'C' :
#         num = 2 + 1
#     elif str_alp[i] == 'D' or str_alp[i] == 'E' or str_alp[i] == 'F' :
#         num = 3 + 1
#     elif str_alp[i] == 'G' or str_alp[i] == 'H' or str_alp[i] == 'I' :
#         num = 4 + 1
#     elif str_alp[i] == 'J' or str_alp[i] == 'K' or str_alp[i] ==  'L' :
#         num = 5 + 1
#     elif str_alp[i] == 'M' or str_alp[i] ==  'N' or str_alp[i] ==  'O' :
#         num = 6 + 1
#     elif str_alp[i] == 'P' or str_alp[i] ==  'Q' or str_alp[i] ==  'R' or str_alp[i] ==  'S' :
#         num = 7 + 1
#     elif str_alp[i] == 'T' or str_alp[i] == 'U' or str_alp[i] ==  'V' :
#         num = 8 + 1
#     elif str_alp[i] == 'W' or str_alp[i] ==  'X' or str_alp[i] ==  'Y' or str_alp[i] ==  'Z' :
#         num = 9 + 1
#     num_list.append(num)
# print(sum(num_list))


str_alp = input()
def solution(str_alp) :
    num = 0
    num_list = []
    for i in range(len(str_alp)) :
        if str_alp[i] == 'A' or str_alp[i] == 'B' or str_alp[i] == 'C' :
            num = 2 + 1
        elif str_alp[i] == 'D' or str_alp[i] == 'E' or str_alp[i] == 'F' :
            num = 3 + 1
        elif str_alp[i] == 'G' or str_alp[i] == 'H' or str_alp[i] == 'I' :
            num = 4 + 1
        elif str_alp[i] == 'J' or str_alp[i] == 'K' or str_alp[i] ==  'L' :
            num = 5 + 1
        elif str_alp[i] == 'M' or str_alp[i] ==  'N' or str_alp[i] ==  'O' :
            num = 6 + 1
        elif str_alp[i] == 'P' or str_alp[i] ==  'Q' or str_alp[i] ==  'R' or str_alp[i] ==  'S' :
            num = 7 + 1
        elif str_alp[i] == 'T' or str_alp[i] == 'U' or str_alp[i] ==  'V' :
            num = 8 + 1
        elif str_alp[i] == 'W' or str_alp[i] ==  'X' or str_alp[i] ==  'Y' or str_alp[i] ==  'Z' :
            num = 9 + 1
        num_list.append(num)
    answer = sum(num_list)
    return answer
print(solution(str_alp))

# .index() 활용해서 다시 풀어보기  => 리스트의 값이 몇번째의 인덱스인지 확인할 수 있음