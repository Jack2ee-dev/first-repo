def get_input():
    print("숫자를 입력하세요: ")
    try:
        number = int(input())
        return number
    except ValueError:
        get_input()
