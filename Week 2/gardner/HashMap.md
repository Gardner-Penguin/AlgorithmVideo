# Hash Table

- Insertion, find O(1)
- Sort 불가능
- Key-Value 형식

# two sum

- sort + two pointers : O(nlogn) + O(n) = O(nlogn)
- Hash Table

```python
[ 13, 7, 5, 1, 3, 2 ], sum = 10

key | value
------------
13     0
7      1
5      2
1      3
3      4
2      5
```

- 각 element별로 10을 만들기 위해서 필요한 값을 table에서 찾으면 됨
- 13의 경우, -3 → 테이블에 없음
- 7의 경우, 3 → 있음, index: 4
- O(n), O(n)

# Find First Unique Character

- 리트코드 387번

```python
nocode program -> 이 중 반복되지 않는 첫번째 캐릭터를 리턴해라
```

- 포인터 하나를 옮겨가면서 해시 테이블 생성해주면 됨(총 등장횟수)
- 다시 포인터를 앞으로 옮겨서 가장 처음으로 value가 1인 캐릭터를 찾으면 됨

# Isomorphic String

- 두 단어의 패턴이 동일한지 판단, Bool 리턴

```python
[ aaa, ddk ]
[ aaaccd, xxxyyz ]
[ aaaffh, xyzhhh ]
```

- 각 문자열에 포인터를 하나씩 두고 key, value 해시 테이블을 생성해줌
- O(n), O(1)

# Valid Anagram

```python
[ "nocodeprogram", "promodernacog" ]
```

- 첫번째 string으로 각 알파벳이 몇 번 들었는지 해시 테이블 생성
- 두번째 string 돌면서 각 character 등장 횟수 빼주기
- 모든 value가 0인지 아닌지 판단

# Word Pattern

```python
[ "abba", "banna apple apple banna" ]
[ "acc", "kiwi grape apple" ]
```

- 각 character에 대해 해시맵 생성
- O(n), O(1)

# Top K frequent element

- 리트코드 692번
- 주어진 리스트 중 가장 많이 반복되는 단어 k개 리턴 + sorting rule
- 각 단어별로 등장 횟수 hash table 생성
    1. 배열 만들기
    
    ```python
    [ (no, 2), (code, 3), (program, 1) ]
    -> 두번재 값을 기준으로 정렬 후 리턴해주기
    ```
    
    1. key값에 해당하는 어레이 만들기
    - sorting기준: hash map의 value를 기준으로
- O(nlogn), O(n)
- 여기서 시간 복잡도를 nlogk로 만들어주고 싶으면 배열을 생성하는게 아니라 heap을 사용하면 됨
- 리트코드 347번