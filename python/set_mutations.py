"""
https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
"""

if __name__ == '__main__':

    n_elements_A = int(input())
    A = set(map(int, input().split()))

    N = int(input())
    for i in range(N):
        operation, len_set = input().split()
        len_set = int(len_set)

        other_set = set(map(int, input().split()))

        if operation == 'intersection_update':
            A.intersection_update(other_set)
        elif operation == 'update':
            A.update(other_set)
        elif operation == 'symmetric_difference_update':
            A.symmetric_difference_update(other_set)
        elif operation == 'difference_update':
            A.difference_update(other_set)
        
    print(sum(A))