## ✔️ 배열이란

- 데이터들이 연속적으로 이어져서 random access를 지원하는 자료구조
- random access란 : 인덱스로 원소에 바로 접근할 수 있도록 하는 특징(메모리의 주소만 지시하면 즉시 데이터를 읽어낼 수 있는 호출방식)
- Back Tracking, DP와 연결되는 경우가 많음

## ☑️ Sorting(정렬)

- O(nlogn)
- stable 알고리즘: Merge
- unstable 알고리즘: quick, heap
- stable vs unstable
- 정렬후에도 순서를 유지하는 소팅 = stable sorting
    - unstable sorting은 그 일관성을 깨트리게됨
    - 정렬 후에 순서가 그대로 유지될거라는 보장이 없음

## ☑️ Search(탐색)

- O(n)
- 이미 배열이 정렬이 돼있는 상태: binary search O(logn)

## ☑️ 기타

- 2D 배열(그래프)

## 🔥 1번 문제(리트코드 704번)

[바로가기 →](https://leetcode.com/problems/binary-search/submissions/)

배열이 정열이 돼있을 때 우리가 원하는 element를 찾아라

→ Binary Search

- left, right, pivot (left, right의 중간)
- pivot의 값을 우리가 찾는 값과 비교 → 만약에 우리가 찾는 값이 더 크면 left를 pivot + 1위치로 이동, 그리고 pivot값 업데이트
- right의 값이 Left보다 작아진다~ 하면 찾는 값이 없다 하고 break
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            pivot = int((left + right) / 2)
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot - 1
                
        return -1
                    
```

## 2번 문제(리트코드 283번)

[바로가기 →](https://leetcode.com/problems/move-zeroes/submissions/)

배열 안의 0을 찾아서 오른쪽 끝으로 보내야함 이때 배열의 기존 순서는 변경되면 안됨
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_index = 0 
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index], nums[i] = nums[i], nums[zero_index]
                zero_index += 1
```

## 3번 문제(리트코드 724번)

[바로가기 →](https://leetcode.com/problems/find-pivot-index/submissions/)

슬라이딩 인덱스, pivot을 찾아라 (pivot 기준 왼쪽의 합과 오른쪽의 합이 동일하면 그게 pivot)

1) brute force

O(n^2)

2) 전체 sum(O(n))

전체 Sum을 구하고 pivot이 한번씩 움직일때마다 자기 자신을 빼주고 왼쪽에는 자기 왼쪽 값을 더해주는 방식으로 값 비교하기~
```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        
        past_pivot = 0
        for pivot in range(len(nums)):
            left_sum += past_pivot
            right_sum -= nums[pivot]
            
            if left_sum == right_sum:
                return pivot
            
            past_pivot = nums[pivot]
            
        return -1
```

## 4번 문제(리트코드 209번)

[→ 풀어보기](https://leetcode.com/problems/minimum-size-subarray-sum/solution/)

#### approach 1: 시간 초과

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')

        for i in range(len(nums)):
            for j in range(i+1, len(nums) + 1):
                arr_sum = sum(nums[i:j])
                if arr_sum >= target:
                    min_len = min(min_len, j - i)
        
        if min_len == float('inf'):
            return 0
        else:
            return min_len
```

#### approach 2: 성공 (투포인터? 슬라이딩 윈도우?)

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        
        left_idx, right_idx = 0, 0 
        total_sum = nums[left_idx]
        
        while left_idx <= right_idx and right_idx <= len(nums):
            if total_sum >= target:
                min_len = min(min_len, right_idx - left_idx + 1)
                total_sum -= nums[left_idx]
                left_idx += 1
            else:
                right_idx += 1
                if right_idx < len(nums):
                    total_sum += nums[right_idx]
                    
        return 0 if min_len == float('inf') else min_len
```

## 5번 문제 (리트코드 75번)

[바로가기 →](https://leetcode.com/problems/sort-colors/submissions/)

- 배열을 정렬하는 문제
- 그냥 sort를 사용하면 O(nlogn)
- 그럼 O(n)의 복잡도로는 어떻게? 각 원소의 숫자를 세면 됨
- count 기법 쓰지 말고 **in-place swap**을 통해서 해봐라~ 하면? 이제 sort colors (중급) 문제가 되는거임
- 3개의 index pointer를 두고 판단하면 됨

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero_index = 0
        one_index = 0
        two_index = len(nums) - 1
        
        while one_index <= two_index:
            if nums[one_index] == 0:
                nums[zero_index], nums[one_index] = nums[one_index], nums[zero_index]
                zero_index += 1
                one_index += 1
            elif nums[one_index] == 2:
                nums[one_index], nums[two_index] = nums[two_index], nums[one_index]
                two_index -= 1
            else:
                one_index += 1
```

## 6번 문제: Merge Sorted Array (리트코드 88번)

- 두 개의 정렬된 Array를 합치는 문제 : 정렬된 하나의 array를 만들어라
- 마찬가지로 3개의 index pointer를 두고 해결

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        num1_index = m - 1
        num2_index = n - 1
        zero_index = len(nums1) - 1
        
        while 0 <= num1_index and 0 <= num2_index:
            if nums1[num1_index] <= nums2[num2_index]:
                nums1[zero_index] = nums2[num2_index]
                num2_index -= 1
                zero_index -= 1
            else:
                nums1[zero_index] = nums1[num1_index]
                num1_index -= 1
                zero_index -= 1
                
        if num2_index >= 0:
            nums1[:num2_index + 1] = nums2[:num2_index + 1]
```

## 7번 문제: Find Peak Element (리트코드 162번)

[바로가기 →](https://leetcode.com/problems/find-peak-element/submissions/)

- max값을 찾는것과 비슷하기 때문에 하나씩 검사하면서 O(n)으로 해결할 수 있음
- 만약에 이거보다 빠르게 O(logn)이나 O(1)로 해결해야한다면..? O(1)은 불가능하기 때문에 O(logn)으로 해결해야함
→ binary search

    
    - 그래프를 그리고 전에 했던 것 처럼 binary search~ index를 딱 반으로 자르기, 그 다음 Index와 값을 비교해서 피크찾기
    - 현재 값보다 다음 값이 더 크면 피크는 현재 index보다 오른쪽에 있다라는 사실을 알 수 있고 만약 현재값보다 다음값이 더 작으면 피크는 현재 index보다 왼쪽에 있다는 사실을 알 수 있음

```swift
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left_idx = 0
        right_idx = len(nums) - 1
        
        while left_idx < right_idx:
            pivot_idx = int((left_idx + right_idx) / 2)
            
            if nums[pivot_idx] >= nums[pivot_idx + 1]:
                right_idx = pivot_idx
            else:
                left_idx = pivot_idx + 1
                
        return left_idx
```

## 8번 문제: Merge Intervals (리트코드 56번)

[바로가기 →](https://leetcode.com/problems/merge-intervals/submissions/)

```swift
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        START, END = 0, 1
        
        answer = []
        
        intervals.sort(key = lambda x:x[0])
        
        start_num, end_num = intervals[0][0], intervals[0][1]
        
        for idx in range(1, len(intervals)):
            if end_num >= intervals[idx][START]:
                end_num = max(end_num, intervals[idx][END])
            else:
                answer.append([start_num, end_num])
                start_num, end_num = intervals[idx][START], intervals[idx][END]
        
        answer.append((start_num, end_num))
        
        return answer
```

## 9번 문제: Shortest Unsorted Continuous Subarray (리트코드 581번)

[바로가기 →](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/submissions/)

- 그래프를 그리자!

## 10번 문제: Find duplicated (리트코드 287번)

- 비둘기집..이론...?
- 투 포인터, O(n^2)
- 정렬 후 서칭 O(nlogn)
- 새로운 어레이 생성, O(n), O(n)
- 시간 복잡도 O(n), 공간 복잡도 O(1) → 중간 난이도 문제
- 해당 인덱스의 값을 인덱스자체로 보는 것이 포인트

```swift
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count_array = [0 for _ in range(len(nums) + 1)]
        
        for num in nums:
            count_array[num] += 1
            if count_array[num] == 2:
                return num
```

## 11번 문제: 2sum 3sum 4sum (리트코드 1번)

- HashMap O(n), O(n)
- BF(Brute Force): 이중For문 O(n^2)
- 정렬 후 (O(nlogn)) 투 포인터, 앞에 하나 뒤에 하나, 이미 정렬된 상태이기 때문에 포인터 이동방향을 알고있음!
→ 두개 더하고 만약에 크면 더 작은 수 필요 따라서 뒤 포인터를 앞으로 이동 이런식으로..
- 리트코드 15번 3sum
- 리트코드 259번, 16번, 18번

## 12번 문제: Rotate Image

- 이중 for문
- newXidx = -oldYindex + n - 1
- newYidx = oldXidx

## 13번 문제: Search a 2D Matrix (리트코드 74번)

- 정렬이 돼있는 2D 배열(순서대로 오름차순)에서 원소를 찾는 문제
    - 첫번째 열을 binary search 진행
    - 열을 정한 다음 그 행에서 pivot잡고 search
- 2D 배열을 1차원 어레이로 변환
- 행, 열 각각 정렬돼있는 경우
    - 첫번째 열의 가장 마지막 숫자와 찾는 숫자 비교 → 찾는 숫자가 더 크면 앞에는 비교할 필요도 없음
    - 행, 열을 각각 비교