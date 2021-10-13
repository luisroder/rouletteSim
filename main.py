from roulette import bet
from colorama import init, Fore, Back, Style
from color import Color


init()


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

