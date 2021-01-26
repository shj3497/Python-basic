# 이진탐색
# 이진탐색은 정렬된 리스트를 전제로 하며, 1회 비교할 때마다 탐색 범위가 절반으로 줄어든다.
# 리스트의 첫 번째 인덱스와 마지막 인덱스의 값을 합하여 2로 나눈후, 중간 인덱스로 지장한다.
# 구하고자 하는 숫자가, 중간 인덱스보다 적은 경우 중간 이후 값은 검색 범위에서 제거한다.
# 구하고자 하는 숫자가, 중간 인덱스보다 큰 경우 중간 이전 값은 검색 범위에서 제거한다.

print("이진 탐색")
a = [11, 18, 26, 27, 39, 57, 63, 75, 76, 80]
key = 75 # 찾고자 하는 값
low = 0
high = len(a)-1 # 10 len()는 길이는 10
print("high : ", high)
while low <= high:
    mid = (low + high) // 2
    print("mid >>> : ", mid)
    if(key == a[mid]):
        print("탐색 성공!", "mid = ", mid)
        break
    else:
        if(key < a[mid]):
            high = mid - 1
        else:
            low = mid + 1
if(low > high):
    print("탐색실패")

print()

# 반복문으로
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if element == some_list[mid_index]:
            return mid_index
            break
        elif element < some_list[mid_index]:
            end_index = mid_index -1
        else:
            start_index = mid_index + 1
    return None

print("이진탐색 함수로 정의")
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(7, [2, 3, 5, 7, 11]))
print(binary_search(6, [2, 3, 5, 7, 11]))



