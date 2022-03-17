""" twoSum O(n) """
# 양수로 주어진 nums중에서 두 수의 합이 target이 되는 index들을 return하여라
# 합하면 타겟이 되는 수와 인덱스를 저장
from typing import List  

def two_sum(nums: List[int], target: int) -> List[int]:
    hash_table = { hash_table[target - num]: idx for idx, num in enumerate(nums) }  
    # { -3: 0, 3: 1, 5: 2, 9: 3, 7: 4, 8: 5}
    for idx, num in enumerate(nums):
        if hash_table.get(num):
            return [idx, hash_table[num]]

indices = two_sum(nums = [13, 7, 5, 1, 3, 2], target=10)
print(indices) # [1, 4]

""" find first unique char O(n) """
# 제일 먼저 등장하는 유니크한 문자값 리턴
def firstUniqueChar(s: str) -> int:
    count = {}
    for c in s:
        crnt_count = count.get(c)
        if crnt_count is None:
            count[c] = 1
            continue      
        count[c] += 1

    for idx,c in enumerate(s):
        if count[c] == 1:
            return idx

    return -1

""" isomorphic strings O(n) """
# 구조가 같은 스트링 
# ex) aaaccd == xxxyyz
# 두 배열을 포인터를 두고 같이 움직이며 대응되는 친구를 키값으로 저장한 뒤 다르면 false
# {'a': 'x', 'c': y, 'd': 'z'}

""" valid Anagram O(n) """
# 글자와 갯수를 저장하고 동일한지 확인
# Collections Counter 쓰면 좋을 듯
# 혹은 sorting하여 하나씩 비교 => O(nlogn)

""" word Pattern O(n) """
# ["abba", "banana apple apple banana"] => true
# ["acc", "kiwi grape apple"] => false
# isomorphic strings 와 동일

""" Top K Frequent Elements O(nlogn) """
# 가장 많이 반복되는 k개
# Collections Counter의 mostCommon 쓰면 좋을 듯
# 힙을 쓰면 O(nlogk)
def topKFrequent(nums: List[int], k: int) -> List[int]:
    table = {}    
    for num in nums:
        count = table.get(num)
        if count is None:
            table[num] = 0      
        table[num] += 1
    #heap 
    freq_heap = []
    for num, count in table.items():
        heapq.heappush(freq_heap,(count, num))
        if k < len(freq_heap):
            heapq.heappop(freq_heap)
    
    k_freq = []
    while freq_heap:
        count , num = freq_heap[0]
        heapq.heappop(freq_heap)
        k_freq.append(num)
    k_freq.reverse()
    
    return k_freq
