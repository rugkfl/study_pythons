# https://www.acmicpc.net/problem/10811

# 문제
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다. 바구니는 일렬로 놓여져 있고, 가장 왼쪽 바구니를 1번째 바구니, 그 다음 바구니를 2번째 바구니, ..., 가장 오른쪽 바구니를 N번째 바구니라고 부른다. 

# 도현이는 앞으로 M번 바구니의 순서를 역순으로 만들려고 한다. 도현이는 한 번 순서를 역순으로 바꿀 때, 순서를 역순으로 만들 범위를 정하고, 그 범위에 들어있는 바구니의 순서를 역순으로 만든다.

# 바구니의 순서를 어떻게 바꿀지 주어졌을 때, M번 바구니의 순서를 역순으로 만든 다음, 바구니에 적혀있는 번호를 가장 왼쪽 바구니부터 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

# 둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다. 방법은 i j로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다는 뜻이다. (1 ≤ i ≤ j ≤ N)

# 도현이는 입력으로 주어진 순서대로 바구니의 순서를 바꾼다.

# 출력
# 모든 순서를 바꾼 다음에, 가장 왼쪽에 있는 바구니부터 바구니에 적혀있는 순서를 공백으로 구분해 출력한다.

def basket_change():
    N, M = map(int, input().split())
    basket_list = []
    for x in range(N):
        x += 1
        basket_list.append(x)
    
    for y in range(M):
        i, j = map(int, input().split())
        a = i -1  #범위지정
        b = j -1  #범위지정
        basket_list[a:b+1] = reversed(basket_list[a:b+1]) # b+1을 한 이유는 b범위까지 포함시키기 위해/basket_list의 a~b까지라는 의미
    print(*basket_list) # *을 붙이면 대괄호 없애고 출력 가능
    pass
    return

basket_change()

# list.reverse()는 원본 리스트를 자체를 역순으로 바뀜
# reversed는 원본 리스트는 변경되지 않고 역순으로 된 리스트를 얻고자 할때 사용