from input import get_input


def do_fizzbuzz():
    try:
        user_input = get_input()
        end = user_input
        curr = 1
        while curr < end:
            if curr % 3 == 0:
                print("fizz")
            elif curr % 5 == 0:
                print("buzz")
            elif curr % 15 == 0:
                print("fizzbuzz")
            else:
                print(curr)
            curr += 1
    except ValueError:
        return


if __name__ == "__main__":
    do_fizzbuzz()
