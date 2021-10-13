import random


def play():
    result = random.randint(0, 37)
    return result


def bet(color):
    result = play()
    return check_win(color, result)


def check_win(color, result):
    if result in color.value:
        return True
    else:
        return False
