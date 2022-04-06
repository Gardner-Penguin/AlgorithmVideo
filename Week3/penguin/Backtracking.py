""" 이론
# Decision Space / Candidate
# 가능성이 없는 경우 가지치기 (pruning)
# 대표적 문제 Permutation, Comination, Nqueen 등..
# recursive 하게 푸는 경우 많음
# DFS 등
# 종료조건 / 현재 단계에서 실행해야 할부분(process) / 다음 단계에서 실행해야 할 부분(recursive call)이 필요
"""

""" Subsets """
# 부분집합 구하기
# ex) [a, b, c] => (), (a), (b), (c), (a, b), (a, c), (b, c), (a, b, c)
# index == len(arr) -> 종료
# recursive(index+1, ans + cur_char) 와 recursive(index+1, cur_char)

""" Permutation """
def gen_permutations(arr, n): 
    result = [] 
    if n == 0:
        return [[]] 
    for i, elem in enumerate(arr): 
        for P in gen_permutations(arr[:i] + arr[i+1:], n-1):
            result += [[elem]+P] 
            return result
