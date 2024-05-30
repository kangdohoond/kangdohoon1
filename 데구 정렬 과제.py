# import random
# import time
# import sys
# import matplotlib.pyplot as plt

# sys.setrecursionlimit(10000)

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1
#     return arr

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr) // 2]
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
#         return quick_sort(left) + middle + quick_sort(right)

# def heapify(arr, n, i):
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2

#     if left < n and arr[largest] < arr[left]:
#         largest = left

#     if right < n and arr[largest] < arr[right]:
#         largest = right

#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)

# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#     return arr

# def shell_sort(arr):
#     n = len(arr)
#     gap = n // 2
#     while gap > 0:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i
#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap
#             arr[j] = temp
#         gap //= 2
#     return arr


# def create_random_list(size=300, start=0, end=99):
#     return [random.randint(start, end) for _ in range(size)]

# def measure_sort_time(sort_func, arr, iterations=10000):
#     total_time = 0
#     for _ in range(iterations):
#         test_arr = arr.copy()
#         start_time = time.time()
#         sort_func(test_arr)
#         total_time += time.time() - start_time
#     return total_time / iterations

# sort_functions = [
#     selection_sort,
#     bubble_sort,
#     insertion_sort,
#     merge_sort,
#     quick_sort,
#     heap_sort,
#     shell_sort
# ]


# A = create_random_list()

# sort_times = {}
# for sort_func in sort_functions:
#     sort_times[sort_func.__name__] = measure_sort_time(sort_func, A)


# print(sort_times)


# sort_names = list(sort_times.keys())
# sort_durations = list(sort_times.values())

# plt.figure(figsize=(12, 6))
# plt.bar(sort_names, sort_durations, color='skyblue')
# plt.xlabel('Sort Algorithm')
# plt.ylabel('Average Time (s)')
# plt.title('Comparison of Sorting Algorithms')
# plt.xticks(rotation=45)
# plt.show()


# 필요한 모듈 import
import random  # 무작위 수 생성을 위한 모듈
import time  # 시간 측정을 위한 모듈
import sys  # 시스템 관련 모듈
import matplotlib.pyplot as plt  # 그래프를 그리기 위한 모듈

# 재귀 한도를 10000으로 설정 (기본값보다 높게 설정)
sys.setrecursionlimit(10000)

# 정렬 알고리즘 구현

# 선택 정렬 함수
def selection_sort(arr):
    n = len(arr)  # 배열의 길이를 저장
    for i in range(n):  # 배열의 각 요소에 대해 반복
        min_idx = i  # 현재 인덱스를 최소값 인덱스로 설정
        for j in range(i+1, n):  # 현재 인덱스 이후의 요소들에 대해 반복
            if arr[j] < arr[min_idx]:  # 현재 요소가 최소값보다 작으면
                min_idx = j  # 최소값 인덱스를 갱신
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 최소값을 현재 위치로 이동
    return arr  # 정렬된 배열을 반환

# 버블 정렬 함수
def bubble_sort(arr):
    n = len(arr)  # 배열의 길이를 저장
    for i in range(n):  # 배열의 각 요소에 대해 반복
        for j in range(0, n-i-1):  # 이미 정렬된 부분을 제외하고 반복
            if arr[j] > arr[j+1]:  # 현재 요소가 다음 요소보다 크면
                arr[j], arr[j+1] = arr[j+1], arr[j]  # 두 요소를 교환
    return arr  # 정렬된 배열을 반환

# 삽입 정렬 함수
def insertion_sort(arr):
    for i in range(1, len(arr)):  # 두 번째 요소부터 시작하여 각 요소에 대해 반복
        key = arr[i]  # 현재 요소를 키로 저장
        j = i-1  # 키의 이전 요소 인덱스
        while j >= 0 and key < arr[j]:  # 키가 이전 요소보다 작으면
            arr[j+1] = arr[j]  # 이전 요소를 한 칸 뒤로 이동
            j -= 1  # 인덱스를 한 칸 앞으로 이동
        arr[j+1] = key  # 키를 올바른 위치에 삽입
    return arr  # 정렬된 배열을 반환

# 병합 정렬 함수
def merge_sort(arr):
    if len(arr) > 1:  # 배열의 길이가 1보다 크면
        mid = len(arr) // 2  # 배열을 두 부분으로 나누기 위한 중간 인덱스
        left_half = arr[:mid]  # 왼쪽 부분 배열
        right_half = arr[mid:]  # 오른쪽 부분 배열

        merge_sort(left_half)  # 왼쪽 부분을 재귀적으로 병합 정렬
        merge_sort(right_half)  # 오른쪽 부분을 재귀적으로 병합 정렬

        i = j = k = 0  # 인덱스 초기화

        # 두 부분을 병합
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 남아있는 왼쪽 부분을 병합
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # 남아있는 오른쪽 부분을 병합
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr  # 정렬된 배열을 반환

# 퀵 정렬 함수
def quick_sort(arr):
    if len(arr) <= 1:  # 배열의 길이가 1 이하이면
        return arr  # 그대로 반환
    else:
        pivot = arr[len(arr) // 2]  # 배열의 중간 요소를 피벗으로 설정
        left = [x for x in arr if x < pivot]  # 피벗보다 작은 요소들
        middle = [x for x in arr if x == pivot]  # 피벗과 같은 요소들
        right = [x for x in arr if x > pivot]  # 피벗보다 큰 요소들
        return quick_sort(left) + middle + quick_sort(right)  # 재귀적으로 정렬된 배열을 반환

# 힙 정렬에 필요한 힙화 함수
def heapify(arr, n, i):
    largest = i  # 현재 노드를 가장 큰 값으로 설정
    left = 2 * i + 1  # 왼쪽 자식 노드 인덱스
    right = 2 * i + 2  # 오른쪽 자식 노드 인덱스

    if left < n and arr[largest] < arr[left]:  # 왼쪽 자식이 더 크면
        largest = left  # 가장 큰 값을 왼쪽 자식으로 갱신

    if right < n and arr[largest] < arr[right]:  # 오른쪽 자식이 더 크면
        largest = right  # 가장 큰 값을 오른쪽 자식으로 갱신

    if largest != i:  # 가장 큰 값이 현재 노드가 아니면
        arr[i], arr[largest] = arr[largest], arr[i]  # 두 노드를 교환
        heapify(arr, n, largest)  # 재귀적으로 힙화

# 힙 정렬 함수
def heap_sort(arr):
    n = len(arr)  # 배열의 길이를 저장
    for i in range(n // 2 - 1, -1, -1):  # 배열의 중간부터 역순으로 반복
        heapify(arr, n, i)  # 힙화

    for i in range(n-1, 0, -1):  # 배열의 끝부터 역순으로 반복
        arr[i], arr[0] = arr[0], arr[i]  # 두 노드를 교환
        heapify(arr, i, 0)  # 힙화
    return arr  # 정렬된 배열을 반환

# 셸 정렬 함수
def shell_sort(arr):
    n = len(arr)  # 배열의 길이를 저장
    gap = n // 2  # 초기 갭 크기를 배열 길이의 절반으로 설정
    while gap > 0:  # 갭이 0보다 클 때까지 반복
        for i in range(gap, n):  # 갭 크기부터 배열의 끝까지 반복
            temp = arr[i]  # 현재 요소를 임시 변수에 저장
            j = i  # 현재 인덱스를 저장
            while j >= gap and arr[j - gap] > temp:  # 갭만큼 떨어진 요소가 더 크면
                arr[j] = arr[j - gap]  # 갭만큼 떨어진 요소를 현재 위치로 이동
                j -= gap  # 인덱스를 갭만큼 줄임
            arr[j] = temp  # 임시 변수를 올바른 위치에 삽입
        gap //= 2  # 갭 크기를 절반으로 줄임
    return arr  # 정렬된 배열을 반환

# 버킷 정렬 함수
def bucket_sort(arr):
    if len(arr) == 0:  # 배열이 비어있으면
        return arr  # 그대로 반환

    bucket_size = 10  # 각 버킷의 크기를 설정
    min_value = min(arr)  # 배열의 최소값을 찾음
    max_value = max(arr)  # 배열의 최대값을 찾음

    bucket_count = (max_value - min_value) // bucket_size + 1  # 필요한 버킷의 수 계산
    buckets = [[] for _ in range(bucket_count)]  # 빈 버킷 리스트 생성

    for i in range(len(arr)):  # 배열의 각 요소에 대해 반복
        buckets[(arr[i] - min_value) // bucket_size].append(arr[i])  # 요소를 적절한 버킷에 추가

    arr = []  # 정렬된 배열을 저장할 리스트 초기화
    for bucket in buckets:  # 각 버킷에 대해 반복
        arr.extend(insertion_sort(bucket))  # 버킷을 정렬하여 배열에 추가

    return arr  # 정렬된 배열을 반환

# 계수 정렬 함수
def counting_sort(arr, max_value=None):
    if max_value is None:  # 최대값이 주어지지 않으면
        max_value = max(arr)  # 배열의 최대값을 찾음

    count = [0] * (max_value + 1)  # 카운트 배열 초기화

    for num in arr:  # 배열의 각 요소에 대해 반복
        count[num] += 1  # 요소의 개수를 증가

    arr = []  # 정렬된 배열을 저장할 리스트 초기화
    for i, c in enumerate(count):  # 카운트 배열의 각 인덱스와 값에 대해 반복
        arr.extend([i] * c)  # 인덱스를 개수만큼 배열에 추가

    return arr  # 정렬된 배열을 반환

# 기수 정렬에 필요한 계수 정렬 함수
def counting_sort_for_radix(arr, exp):
    n = len(arr)  # 배열의 길이를 저장
    output = [0] * n  # 정렬된 배열을 저장할 리스트 초기화
    count = [0] * 10  # 카운트 배열 초기화

    for i in range(n):  # 배열의 각 요소에 대해 반복
        index = arr[i] // exp  # 현재 자릿수의 값 계산
        count[index % 10] += 1  # 해당 값의 개수를 증가

    for i in range(1, 10):  # 카운트 배열의 각 인덱스에 대해 반복
        count[i] += count[i - 1]  # 누적 합 계산

    i = n - 1  # 배열의 마지막 인덱스부터 반복
    while i >= 0:  # 인덱스가 0 이상일 때까지 반복
        index = arr[i] // exp  # 현재 자릿수의 값 계산
        output[count[index % 10] - 1] = arr[i]  # 정렬된 위치에 요소를 삽입
        count[index % 10] -= 1  # 카운트를 감소
        i -= 1  # 인덱스를 감소

    for i in range(n):  # 정렬된 배열의 각 요소에 대해 반복
        arr[i] = output[i]  # 원본 배열에 정렬된 값을 복사

# 기수 정렬 함수
def radix_sort(arr):
    max_value = max(arr)  # 배열의 최대값을 찾음
    exp = 1  # 초기 자릿수를 1로 설정
    while max_value // exp > 0:  # 최대값을 자릿수로 나눈 값이 0보다 클 때까지 반복
        counting_sort_for_radix(arr, exp)  # 현재 자릿수에 대해 계수 정렬 수행
        exp *= 10  # 자릿수를 10배 증가
    return arr  # 정렬된 배열을 반환

# 정렬 알고리즘의 실행 시간을 측정하는 함수
def measure_time(sort_func, arr):
    start_time = time.time()  # 현재 시간을 저장 (시작 시간)
    sort_func(arr.copy())  # 정렬 함수 호출 (배열을 복사하여 정렬)
    end_time = time.time()  # 현재 시간을 저장 (종료 시간)
    return end_time - start_time  # 정렬에 걸린 시간을 반환

# 무작위 수 생성 및 정렬 시간 측정

# 사용할 정렬 알고리즘 리스트
sorting_algorithms = [
    selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort,
    heap_sort, shell_sort, bucket_sort, counting_sort, radix_sort
]

# 각 정렬 알고리즘의 시간을 저장할 딕셔너리 초기화
times = {sort_func.__name__: 0 for sort_func in sorting_algorithms}

# 배열의 요소 개수와 반복 횟수 설정
num_elements = 300  # 배열의 길이를 300으로 설정
num_trials = 10000  # 반복 횟수를 10000으로 설정

# 각 정렬 알고리즘에 대해 시간 측정
for _ in range(num_trials):  # 설정된 반복 횟수만큼 반복
    arr = [random.randint(0, 99) for _ in range(num_elements)]  # 무작위 수 배열 생성
    for sort_func in sorting_algorithms:  # 각 정렬 알고리즘에 대해 반복
        times[sort_func.__name__] += measure_time(sort_func, arr)  # 정렬 시간을 측정하여 누적

# 평균 시간 계산
for sort_func in sorting_algorithms:  # 각 정렬 알고리즘에 대해 반복
    times[sort_func.__name__] /= num_trials  # 평균 시간을 계산하여 저장

# 결과 그래프 그리기
plt.figure(figsize=(12, 8))  # 그래프 크기를 설정
plt.bar(times.keys(), times.values(), color='red')  # 막대 그래프 생성
plt.xlabel('Sorting Algorithm')  # x축 라벨 설정
plt.ylabel('Average Time (seconds)')  # y축 라벨 설정
plt.title('Average Sorting Time Comparison')  # 그래프 제목 설정
plt.xticks(rotation=45)  # x축 라벨 회전
plt.show()  # 그래프 표시

# 각 정렬 알고리즘의 평균 시간 출력
for sort_func in sorting_algorithms:  # 각 정렬 알고리즘에 대해 반복
    print(f"{sort_func.__name__}: {times[sort_func.__name__]:.6f}초")  # 알고리즘 이름과 평균 시간 출력






















# 병합정렬 : 머지 : 0.000277
# 퀵정렬 :  퀵 : 0.000172
# 힙정렬 : 힙 : 0.000363