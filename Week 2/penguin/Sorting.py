""" Bubble Sort O(n2) """
# stable한 sort => 문자도 가능, 두가지 이상 기준으로 정렬 가능
def bubble_sort(lst):
    LEN = len(lst)
    for last_idx in range(LEN-2, 0, -1):  # 각 턴의 마지막 인덱스
        is_swap = False  # 최적화
        for l_idx in range(0, last_idx+1):
            if lst[l_idx] > lst[l_idx+1]:
                lst[l_idx], lst[l_idx+1] = lst[l_idx+1], lst[l_idx]
                is_swap = True
        if not is_swap:  # swap이 일어나지 않았으면 정렬 완료상태
            return lst
    return lst

""" Insertion Sort O(n2) """
def insert_sort(lst):
    LEN = len(lst)
    for search_start in range(1, LEN):  # 탐색 시작 인덱스
        while search_start > 0:
            if lst[search_start] < lst[search_start-1]:
                lst[search_start], lst[search_start - 1] \
                    = lst[search_start-1], lst[search_start]
                search_start -= 1
            else:
                break
    return lst

""" Selection Sort O(n2) """
# stable하지 않음
def select_sort(lst):
    LEN = len(lst)
    for cur_idx in range(0, LEN-1):  # 최소값을 위치시킬 인덱스
        search_start, min_idx = cur_idx+1, cur_idx
        for search_idx in range(search_start, LEN):
            if lst[search_idx] < lst[min_idx]:
                min_idx = search_idx
        lst[cur_idx], lst[min_idx] = lst[min_idx], lst[cur_idx]
    return lst

""" Merge Sort O(nlogn) """

def merge(left, right):
    merged = []
    while left or right:
        # left나 right 가 비었을 때
        if not left:
            merged += right
            return merged
        elif not right:
            merged += left
            return merged
        # left나 right 첫번째 원소값 비교
        if left[0] < right[0]:
            merged += [left[0]]
            left = left[1:]
        else:
            merged += [right[0]]
            right = right[1:]
    return merged


def merge_sort(lst):
    LEN = len(lst)
    if LEN <= 1:
        return lst
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

""" Quick Select O(n2) / O(n) """
# 파티셔닝
import random

def quick_select(nums:List[int],k:int) -> int:
    length = len(nums)
    if length == 1:
        return nums[0]

    pivot_idx = random.randrange(length)
    last_idx = length-1

    nums[pivot_idx], nums[last_idx] = nums[last_idx], nums[pivot_idx]
    left_idx = 0
    right_idx = length-2
    pivot = nums[-1]
    while left_idx <= right_idx:
        if nums[left_idx] <= pivot:
            left_idx += 1
            continue
    
        if pivot < nums[right_idx]:
            right_idx -= 1
            continue
    
        if pivot < nums[left_idx] and nums[right_idx] <= pivot:
            nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
            continue

    nums[left_idx], nums[last_idx] = nums[last_idx], nums[left_idx]
    if left_idx == length - k:
        return nums[left_idx]
    elif left_idx < length-k:
        #list slicing creates copy. 
        return quick_select(nums=nums[left_idx+1:],k=k)
    elif length-k < left_idx:
        #list slicing creates copy.
        return quick_select(nums=nums[:left_idx],k=k-(length-left_idx))

""" Quick Sort O(n2) / O(nlogn) """
# 파티셔닝
# stable하지 않음
def quick_sort(lst):
    LEN = len(lst)
    if LEN <= 1:
        return lst
    middle = len(lst) // 2  # 최악의 케이스를 막기 위해  pivot을 middle로 설정
    pivot = lst[middle]
    rest = lst[:middle] + lst[middle+1:]
    left = [num for num in rest if num <= pivot]
    right = [num for num in rest if num > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

""" Heap Sort O(nlogn) """
# heapify 후 pop => sort
import heapq

#in place memory sorting
def heap_sort(nums:List[int])->List[int]:
    #python does not have maxHeap. multiply by -1
    nums = [-1*n for n in nums]
    heapq.heapify(nums)

    sorted = [0] * len(nums)
    
    for i in range(len(nums)-1,-1,-1):
        largest = -1 * heapq.heappop(nums)
        sorted[i] = largest
    return sorted

""" Counting Sort O(n+k) """
# 갯수를 세서 정렬
# stable한 sort
# k: 최댓값 (range) => 작을수록 유리
def counting_sort(nums:List[int])->List[int]:  
    length = len(nums)
    min_num = min(nums)  #offset
    max_num = max(nums)

    range = max_num - min_num + 1
    counts = [0]*range

    for num in nums:
        count_idx = num - min_num
        counts[count_idx] += 1

    acc_counts = []
    acc_count = 0
    for count in counts:
        acc_count += count
        acc_counts.append(acc_count)

    end_locs = [ c-1 for c in acc_counts]

    sorted = [0] * length
    for num in reversed(nums):
        count_idx = num - min_num
        end_loc = end_locs[count_idx]
        sorted[end_loc] = num
        end_locs[count_idx] -= 1

    return sorted

""" Radix(계수) Sort W + O(n+k) """
# stable한 sort
# Counting sort의 range가 클 경우 보완
# 일의자리 - 십의자리 - 백의자리 순으로 정렬
# W: 가장 큰 수의 자리수

def radix_sort(nums:List[int])->List[int]:
    largest_num = max(nums)
    digits = int(math.log10(largest_num))+1
    sorted = nums
    for digit in range(digits):
        sorted = counting_sort_by_digit(nums=sorted,digit=digit)
    return sorted

def counting_sort_by_digit(nums:List[int],digit:int)->List[int]:  
    counts = [0]*10
    for num in nums:
        count_idx = num//pow(10,digit)%10
        counts[count_idx] += 1

    acc_counts = []
    acc_count = 0
    for count in counts:
        acc_count += count
        acc_counts.append(acc_count)
    end_locs = [ c-1 for c in acc_counts]

    sorted = [0] * len(nums)
    for num in reversed(nums):
        count_idx = num//pow(10,digit)%10
        end_loc = end_locs[count_idx]
        sorted[end_loc] = num
        end_locs[count_idx] -= 1

    return sorted
