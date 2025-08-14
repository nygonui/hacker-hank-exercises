"""
https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    

    i_list = [i for i in range(x+1)]
    j_list = [j for j in range(y+1)]
    k_list = [k for k in range(z+1)]

    
    r = [[i,j,k] for i in i_list for j in j_list for k in k_list if sum([i,j,k]) != n]
    
    print(r)



