- FILO (First In Last Out)
- 새로 element 넣는 push
- 가장 위의 element빼는 pop
- 가장 위의 element에 접근하는 top

# Valid Parentheses

- (), {}, []로 이루어진 배열
- 괄호 셋이 valid한지 아닌지 판단

# min/max Stack

- 직접 stack data container 만드는 문제
- push, pop, top, **+ max()** 를 제공하는 stack 만들기
- stack을 두 개 생성 (하나는 일반 스택, 하나는 max 명령만을 위한 스택)
    - max 스택에는 현재 top값보다 작은 값이 들어오면 무시하고 그냥 top값을 하나 더 올려주는 형태로 진행
    - pop의 경우에도 일반, max 둘 다 pop 해줘야 그 상태에서의 max에도 접근이 가능함~
        - 조금 더 space complexity를 줄이고 싶다면 max 스택의 top보다 작은 값이 들어오면 아예 추가를 더 안함
        - 그 상태에서 pop을 시키면 일반 스택은 pop을 하고 pop된 해당값과 max스택의 top을 비교해서 일반 스택의 pop된 값이 max스택의 top보다 작으면 max스택은 변형 x
    - 스택에 반복된 숫자를 넣지 않고 (해당 숫자, 등장 횟수) 이렇게 페어로 넣어주면 공간을 조금 더 줄일 수 있음

# Remove Adjacent Duplicates

- 리트코드 1047

```python
abbcbbcdef -> adef
# stack에 넣어주다가 top과 현재 넣어주는 알파벳이 동일하면 pop
```

- 문자열과 함께 연속된 알파벳의 갯수가 주어지는 경우(중급)
    - 리트코드 1209

```python
abbcddde, k = 2
-> acde
abbcddde, k = 3
-> abbce
abbcddde, k = 4
-> abbcddde
```

- 두 개의 스택 생성, 하나의 스택에 각 알파벳이 몇개씩 있는지 기록

```python
ab
11

abb
12

abbc
121

abbcdd
1212 -> k-1과 동일하기 때문에 pop

abbce
1211
```