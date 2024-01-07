# https://www.acmicpc.net/problem/10809

# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

import string
def alphabet():
    S = list(input())
    alphabet_list = list(string.ascii_lowercase)  # string을 import해주고 list안에 string.ascii_lowercase를 하면 소문자 알파벳만 리스트로 반환해줌/대문자는 uppercase

    for i in range(len(alphabet_list)):
        k = -1 # 알파벳이 처음으로 등장하는 인덱스를 저장하는 변수(어차피 해당 알파벳이 없으면 -1울 출력해야하므로 초기값을 -1로 지정)
        for j in range(len(S)):
            if alphabet_list[i] in S[j] and k == -1 : # 알파벳의 인덱스가 문자열의 인덱스에 포함이 되어 있고 k가 -1인 경우에만 k에 j를 저장
                k = j
            pass
        print(k, end=" ")
        
    return
alphabet()