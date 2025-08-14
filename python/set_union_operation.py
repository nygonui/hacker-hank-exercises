"""
https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
"""
qtd_e = int(input())
n_e = set(map(int, input().split()))

qtd_f = int(input())
n_f = set(map(int, input().split()))

set_result = n_e.union(n_f)
print(len(set_result))