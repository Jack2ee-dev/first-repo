from input import get_input

def do_fizzbuzz():
    user_input = get_input()
    start = 1
    end = user_input
    curr = 1
    while curr < end:
	if curr % 3 == 0:
	    print("fizz")
	else if curr % 5 == 0:
	    print("buzz")
	else if curr % 15 == 0:
	    print("fizzbuzz")
	else:
	    print(curr)
	curr += 1

if __name__ == "__main__":
    do_fizzbuzz()
