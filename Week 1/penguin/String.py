""" String Matching O(n) """
# abcdefgh / defgh 비교
# => 포인터 두고 같은 지점부터 비교
# KMP 알고리즘 ) 어려움 -> 반복된 부분 저장
# Rolling hash 알고리즘 사용권장
# -> widow sliding으로 hash값을 계산하여 충돌이 나면 find하게 됨

# + 추가) String Rotation
import re
# rotation 형태 -> 보통 이어 붙이면 접근 쉬움 
def is_substring(str1, str2):
    return len(str1) == len(str2) and bool(re.search(str2, str1*2))

""" Palindrom O(n) """
# 투 포인터 사용하여 중앙지점까지 비교

# 재귀적 풀이
def is_palindrome2(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return is_palindrome2(word[1:-1])

# 스택사용 / 링크드 리스트 구조일때
def is_palindrome3(head):
    slow, fast = head, head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow, fast = slow.next, fast.next.next

    # 홀수개일때 가운데꺼 스킵
    if fast:
        slow = slow.next

    while slow:
        if slow.data != stack[-1]:
            return False
        else:
            stack.pop()
            slow = slow.next

    return True

""" Add Strings O(n) """
# 두 스트링을 int로 변환하지 않고 더해서 반환
# 뒷자리부터 계산하며 / 값을 carry로 기록 % 값을 result에 붙여줌
# 마지막에 result를 reverse하여 return 

""" Group Anagrams O(n) """
# anagram끼리 묶는 문제
# sort한 후 키값으로 셋팅후 hash map에 넣음 ->O(n*mlogm)
# 키값을 알파벳 갯수로 셋팅 ex)a2b1
# ['abc', 'cba', 'def', 'acb', 'fed', 'ff', 'ee']
from collections import Counter, defaultdict
def group_anagrams(arr):
    anagram_table = defaultdict(list)
    result = []

    for word in arr:
        anagram_key = str(Counter(word))
        anagram_table[anagram_key] += [word]

    for arr in anagram_table.values():
        result += arr

    return result

""" Longet Substring Without Repeats O(n) """
# 반복 요소 없는 가장 긴 요소 찾기
# a b (c g a b d) d => c g a b d => 5
# 두 포인터를 사용하여 반복 요소가 없으면 right이동
# 반복요소가 있으면 left이동
# 각 단계에서 maxLength 저장
# 반복요소 체크는 hash로 index 저장하여 left index+1로 이동
# right가 바깥으로 나가면 종료