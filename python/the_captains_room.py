"""
https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
"""

import time


if __name__ == '__main__':
    # Calcula tempo de exucação
    start = time.perf_counter()
    
    # ---------------------------------------- # 
    
    K = int(input())
    room_numbers = list(map(int, input().split()))
    set_room_numbers = set(room_numbers)


    res = [ i for i in set_room_numbers if room_numbers.count(i) == 1]
    print(res)
    

    # ---------------------------------------- #
    # Calcula tempo de exucação
    elapsed = time.perf_counter()
    e1 = elapsed - start
    print(f'Time spent in function is: {e1}')
    print('\n\n')


    # ---------------------------------------- #
    # ---------------------------------------- #
    # ---------------------------------------- #
    # Calcula tempo de exucação
    start1 = time.perf_counter()
    
    # ---------------------------------------- # 
    
    
    K = int(input())
    room_numbers = list(map(int, input().split()))
    set_room_numbers = set(room_numbers)


    for i in set_room_numbers:
        if room_numbers.count(i) == 1:
            print(i)


    # ---------------------------------------- #
    # Calcula tempo de exucação
    elapsed1 = time.perf_counter()
    e2 = elapsed1 - start1
    print(f'Time spent in function is: {e2}')