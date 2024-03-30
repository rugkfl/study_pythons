# https://school.programmers.co.kr/learn/courses/30/lessons/120811

# 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.


array = [1, 2, 7, 10, 11]
def solution(array):
    array.sort()
    len_list = len(array)
    median = 0
    mid_idx = len_list // 2
    if len_list % 2 == 0 :
        answer = (array[mid_idx] + (array[mid_idx]-1)) /2
    else :
        answer = array[mid_idx]
    return answer
print(solution(array))


# # array = [1, 2, 3, 4]
# array = [1, 2, 7, 10, 11]
# # array = [9, -1, 0]
# array.sort() # [-1, 0, 9] => 오름차순으로 정렬
# len = len(array)
# median = 0
# if len % 2 == 0 : # 리스트의 개수가 짝수 일 떄
#     idx = len // 2 # 전체 개수에 2를 나누어 중앙 인덱스 값을 구함
#     median = (array[idx] + (array[idx]-1)) / 2  # 짝수일 경우 중앙에 있는 두개의 값을 더한다음 2를 나누어 줘야함
# else :   # 리스트의 개수가 홀수 일 때
#     idx = (len // 2) # 전체 개수에 2를 나누어 중앙 인덱스 값을 구함
#     median = array[idx] # 중앙 인덱스만 뽑아냄
# print(median)
