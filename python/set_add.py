"""
https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
"""
if __name__ == '__main__':
    coutrys = set()
    for _ in range(int(input())):
        coutry = input()
        coutrys.add(coutry)
        
    print(len(coutrys))