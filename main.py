import random
from enum import Enum
from colorama import init, Fore, Back, Style

red_fields = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_fields = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green_tiles = [0]

init()

class Color(Enum):
    GREEN = [0]
    RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    BLACK = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


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


def print_bet_result(result):
    if result is True:
        print(Fore.GREEN + "won" + Style.RESET_ALL)
    elif result is False:
        print(Fore.RED + "lost" + Style.RESET_ALL)
    else:
        print(Back.RED + "error" + Style.RESET_ALL)


def main():
    for i in range(10):
        print_bet_result(bet(Color.BLACK))

    print_bet_result("awd")


if __name__ == '__main__':
    main()

