"""
https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
"""

def swap_case(s:str):
    result = []
    for c in s:
        if c.islower(): 
            result.append(c.upper())
        else: 
            result.append(c.lower())

    return ''.join(result)    


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

