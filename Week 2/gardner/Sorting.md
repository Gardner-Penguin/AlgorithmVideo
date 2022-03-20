# Bubble Sorting 버블 소트

```python
[ 9 3 5 7 1 ]
3 9 5 7 1
3 5 9 7 1
3 5 7 9 1
3 5 7 1 | 9
------------ 첫번째 bubble swap 완료
3 5 1 | 7 9 
------------ 두번째 bubble swap 완료
3 1 | 5 7 9
------------ 세번째 bubble swap 완료
1 3 5 7 9
------------ 네번째 bubble swap 완료
```

- 두 개씩 비교해주면서 swap해줌
- 한 번 정렬할 때 O(n) 이 과정을 n번만큼 또 반복해야하기 때문에 O(n^2)

```python
bubble_list = [9, 3, 5, 7, 1]

def bubble_sort(array):
	for i in range(len(array) - 1):
		for j in range(len(array) - i - 1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
	return array
```

# Stability

```python
[ 7a 5a 5b 7b 3c ]
[ 5a 5b 7a 3c 7b ]
[ 5a 5b 3c 7a 7b ]
[ 5a 3c 5b 7a 7b ]
[ 3c 5a 5b 7a 7b ] # 결과
```

- 첫 배열과 마지막 배열을 비교했을 때 ab 순서가 유지되고 있음
- 이러한 특징이 배열의 stability라고 부름
- quick sort는 stable하지 않음

# Insertion Sorting 삽입 정렬

- 시간 복잡도 O(n^2)
- stable함
- 직관적이지만 느린 알고리즘이기 때문에 굳이 암기할 필요는 없음

```python
[ 9 3 5 7 1 ]
# 9는 고정된 위치라고 생각하고 그 다음 숫자를 확인
# 3은 9보다 작기 때문에 9의 왼쪽에 삽입
[ 3 9 5 7 1 ]
# 현재까지 [ 3 9 ]가 정렬된 배열
# 그 다음 5는 3보다 크고 9보다 작기 때문에 그 사이에 삽입
[ 3 5 9 7 1 ]
# 현재까지 [ 3 5 9 ]가 정렬된 배열
# 7을 삽입
[ 3 5 7 9 1 ]
# 현재까지 [ 3 5 7 9 ]가 정렬된 배열
# 1을 삽입
[ 1 3 5 7 9 ]
```

# Selection Sorting 선택 정렬

- 시간 복잡도 O(n^2)

```python
[ 3 5 9 1 7 ]
[ 1 5 9 3 7 ]
[ 1 3 5 9 7 ]
[ 1 3 5 7 9 ]
```

- 하나의 element를 찾은 뒤 그 뒤 배열에서 min값을 찾아줌
- element와 min값을 swap
- min찾는 과정 O(n) → n번 반복
- stable하지 않음

```python
[ 7a 7b 5a 5b 3c ]
[ 3c 7b 5a 5b 7a ]
[ 3c 5a 7b 5b 7a ]
[ 3c 5a5b 7b 7a ]
```

# Merge Sort

- 시간 복잡도 O(n*logn)
- recursive한 코드 구성

```python
[ 7 3 1 5 6 4 2 ]
[ 7 3 1  | 5 6 4 2 ]
[ 7 | 3 1 | 5 6 | 4 2 ]
[ 7 | 3 | 1 | 5 | 6 | 4 | 2 ]
```

- 이 쪼개진 배열들을 다시 합치면서 정렬하는 것이 merge sort

```python
[ 7 | 1 3 | 5 6 | 2 4 ]
[ 1 3 7 | 2 4 5 6 ]
# -> 이때 합치는 방법
# 앞 뒤 배열에 포인터를 하나씩 두고 비교, 작은거 기입, 기입하면 포인터 +1
[ 1 2 3 4 5 6 7 ]
```

- O(n)이 필요한 과정을 logn번 반복

# Quick Select

- 리트코드 215번
- 정렬되지 않은 array에서 N번째로 큰 수를 찾는 것
- sort() 사용하는 경우 → O(nlogn)
- Heap 사용하는 경우 → O(nlogk)
- Partitioning: pivot두고 왼쪽, 오른쪽 작거나 큰 수만 두는 것(pivot은 랜덤해도됨)
- worst: O(n^2), best: O(n), avg: O(n)

# Quick Sort

- pivot 랜덤하게 잡고 마지막 숫자와 swap해줌
- 포인터를 두개 잡고 pivot을 기준으로 element를 pivot 앞뒤로 정렬해줌
- Best: O(nlogn), Worst: O(n^2), Avg: O(nlogn)
- unstable

# Heap Sort

- Max Heap의 경우, Heap을 pop하면 max값
- array의 맨 뒤로 보냄 → 다시 Heap정렬
- max찾는 O(n) + max값을 array의 맨 뒤로 보내는 O(logn) * n번 진행 = O(nlogn)
- unstable

# Counting Sort

- O(n + a)
- 주어진 배열을 counting해서 정렬

```python
[3,4,0,1,2]
# 가장 작은 수 0 가장 큰 수 4 -> 5개의 array생성
[1,1,1,1,1] (count array)
[1,2,3,4,5] (누적 카운트)
[0,1,2,3,4]
```

- 누적 카운트가 각 숫자의 끝 위치 정보를 갖고 있음

```python
[3,0,5,1,0,5]
```

- count: [2,1,0,1,0,2]
- 각 숫자가 몇번째 index에서 끝내는지 알아내기 위해 누적 카운트
    - [2,3,3,4,4,6] → [1,2,2,3,3,5]
    - array의 마지막 수부터 시작해서 index에 넣어주고 누적 카운트 -1해줌
- O(n+k) (k는 array의 길이) 가장 큰수 - 가장 작은수
- stable

# Radix Sort

```python
[391, 582, 50, 924, 134, 8, 192]
```

- counting sort: 900개 이상의 공간이 필요함
- radix sort: 자리수 별로 정리(1의 자리수 별로)
    - 무조건 stable해야함
    - 0~9까지 제한됨
- 1의 자리수를 기준으로 정렬함 : [50, 391, 582, 192, 924, 134, 08]
- 10의 자리수를 기준으로 정렬함 : [08, 924, 134, 50, 582, 391, 192]
- 100의 자리수를 기준으로 정렬함 : [ 8, 50, 134, 192, 392, 582, 924]
- O(n+k) (각 자리수별로 정렬할때 counting sort하는 시간 복잡도) x w(자리수)

→ O(w(n+k))