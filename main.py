import random

red_fields = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_fields = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green_tiles = [0]

def play(j):
    results = []
    for i in range(j):
        result = random.randint(0, 37)
        results.append(result)
    return results

print(play(10))