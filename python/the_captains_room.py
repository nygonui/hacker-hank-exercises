"""
https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
"""
from collections import Counter


if __name__ == '__main__':
    
    # Método 1 -- estourou limite de tempo
    # K = int(input())
    # room_numbers = list(map(int, input().split()))
    # set_room_numbers = set(room_numbers)


    # res = [ i for i in set_room_numbers if room_numbers.count(i) == 1]
    # print(res[0])
    
    
    # Método 2 -- estourou limite de tempo
    # K = int(input())
    # room_numbers = list(map(int, input().split()))
    # set_room_numbers = set(room_numbers)


    # for i in set_room_numbers:
    #     if room_numbers.count(i) == 1:
    #         print(i)
    #         break

    # Método 3 -- OK
    K = int(input())
    room_numbers = list(map(int, input().split()))
    counter_room = Counter(room_numbers)
    sorted_counter_room = sorted(counter_room.items(), key=lambda x: x[1])

    print(sorted_counter_room[0][0])
