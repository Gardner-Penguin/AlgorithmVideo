""" 이론
# sort는 기본적으로 O(nlogn)
# stable sorting (merge) - 순서가 지켜짐
# unstable sorting (quick, heap) - 순서가 보장되지 않음)
# 정렬되어 있는 배열일 경우 이분탐색 사용 -> O(logn)
"""

""" Binary search O(logn) """
def binary_search(target, data):
    data.sort()
    start, end = 0, data.length - 1
    while start <= end:
        mid = (start + end) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1;

""" MoveZeros O(n)"""
# 0을 모두 오른쪽으로 보내는 문제
# 0이아닌 친구들 왼쪽으로 보냄
# [1, 3, 0, 0, 0, 4, 5] => [1, 3, 4, 5, 0, 0, 0]
def move_zeros(arr):
    zero_idx = 0
    for idx, num in enumerate(arr):
        if num != 0:
            arr[zero_idx], arr[idx] = arr[idx], arr[zero_idx]
            zero_idx += 1
    return arr

""" FindPivotIdx O(n)"""
# 피봇을 중심으로 왼쪽 합과 오른쪽합이 같은 피봇 인덱스 반환
# sliding 개념 이용 
# arr = [1,8,2,9,2,3,6] => 3
def find_pivot_idx(arr):
    total = sum(arr)
    leftSum, rightSum = 0, total - arr[0]
    for idx in range(1, len(arr)):
        leftSum += arr[idx-1]
        rightSum -= arr[idx]
        if leftSum == rightSum:
            return idx
    return -1

""" SortColors O(n)"""
# 0, 1, 2 를 정렬하라
# 카운트로 세서 리턴해도 됨
# in place하도록 하려면 swap 방식
# [1, 0, 2, 2, 0, 1, 2, 1, 0] => [0, 0, 0, 1, 1, 1, 2, 2, 2]
def sort_colors(arr):
    idx_0, idx_1, idx_2 = 0, 0, len(arr) - 1
    while idx_1 <= idx_2:
        if arr[idx_1] == 0:
            arr[idx_0], arr[idx_1] = arr[idx_1], arr[idx_0]
            idx_0 += 1
            idx_1 += 1
        elif arr[idx_1] == 2:
            arr[idx_2], arr[idx_1] = arr[idx_1], arr[idx_2]
            idx_2 -= 1
        else:
            idx_1 += 1
    return arr

""" MergedSortArray O(n+m)"""
# 뒤에 여유공간이 있어 뒤부터가 효율적 - 유사 문제가 있어 복붙
# A: [4, 5, 6, 9, 17, 25, 31]
# B: [1, 2, 3, 3, 8, 14]

def merge(arr_A, arr_B):
    LEN_A, LEN_B = len(arr_A), len(arr_B)
    a_idx, b_idx = LEN_A - 1, LEN_B - 1
    merged_idx = LEN_A + LEN_B - 1
    while b_idx > 0:
        # B 남은 원소들이 A 첫원소보다 작을 때
        if a_idx < 0:
            arr_A[:merged_idx+1] = arr_B[:b_idx+1]
            break
        # A 원소가 더 큰경우 
        if arr_A[a_idx] > arr_B[b_idx]:
            arr_A[merged_idx] = arr_A[a_idx]
            a_idx -= 1
        # B 원소가 더 큰경우
        else:
            arr_A[merged_idx] = arr_B[b_idx]
            b_idx -= 1

        merged_idx -= 1
    return arr_A

""" FindPeakElement O(logn)"""
# 이분탐색으로
def find_peak_el(arr):
    left, right = 0, len(arr) -1 
    if not arr:
        return 0
    while left < right:
        mid = left + right // 2
        if arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left

""" MergeIntervals O(nlogn)"""
# 인터벌들이 겹치면 merge
# [1, 5] [3, 7] [10, 15] [8, 16]
# 시작점 기준으로 sort [1, 5] [3, 7] [8, 16] [10, 15]
# 시작점이 전 끝점보다 작으면 merge
# 시작점이 전 끝점보다 크면 ans ++

""" Shortest Unsorted Continuous SubArray O(n)"""
# 오름차순으로 정렬되기 위해 정렬되어야하는 subArray의 최소길이 구하는 문제
# [2, 5, 7, 6, 3, 9, 15] => [5, 7, 6, 3] => 4
# [2, 4, 6] => 0
# 그래프를 그려본 후 왼쪽에서 부터는 꺾이는 부분 중 최솟값을 찾고 (3) => 2 오른쪽 5
# 오른쪽 부터는 꺾이는 부분 중 최댓값을 찾는다 (7) => 9 왼쪽 3
# 5(1) ~ 3(4) => 4 - 1 + 1 => 4

""" Find Duplicates time : O(n) / space : O(1)"""
# 원본 배열을 이용
# 내부적 마킹 이용 -로 체크
# [1, 2, 3, 4, 2] => [0, 1, 2, 3, 4]
# [1, 2, 3, 4, 2] => [1, -2, 3, 4, 2]
# [1, 2, 3, 4, 2] => [1, -2, -3, 4, 2]
# [1, 2, 3, 4, 2] => [1, -2, -3, -4, 2]
# [1, 2, 3, 4, 2] => [1, -2, -3, -4, -2]
# [1, 2, 3, 4, 2] => [1, "-2", -3, -4, 2]

""" 2Sum, 3Sum, 4Sum"""
# array 2,3,4개의 요소의 합이 타겟인 경우 반환
# sort를 하고 두 포인터를 쓰면 O(nlogn)

""" Rotate Image """
# 2차원의 idx를 잘 이해하고 있니?
# in-place하게할 경우 어려움
# 4개의 쌍이 한꺼번에 움직임
# Img[a], Img[b], Img[c], Img[d] = Img[d], Img[a], Img[b], Img[c]
# i는 0 ~ n/2 
# j는 0 ~ (n+1)/2

# not in-place 코드
def rotate90(matrix):
    return list(zip(*matrix[::-1]))

""" Search a 2D """
# 행, 열 모두 이분탐색 이용
# 행 이분탐색으로 먼저 탐색할 행 결정
# 행에서 이분탐색으로 열 결정 
# or 1차로 펼친 후 이분탐색
# ==> log(nm)
# 열별로, 행별로 오름차순으로 정리되어있는 경우
# [ [15, 20, 70, 85],
#   [20, 35, 80, 95],
#   [30, 55, 95, 105],
#   [40, 80, 100, 200] ]

# 0, n-1 에서 시작 혹은 n-1, 0에서 시작
def find_target(matrix, target):
    ROW, COL = len(matrix), len(matrix[0])
    i, j = 0, COL-1
    while i < ROW and j >= 0:
        cur_num = matrix[i][j]
        # 탐색 성공
        if cur_num == target:
            return (i, j)
        # next 
        if cur_num > target:
            j -= 1
        else:
            i += 1
    # 탐색 실패
    return None