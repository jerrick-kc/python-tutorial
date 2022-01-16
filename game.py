def comp_ans(number):
    start = 1
    end = 100
    computer_guess = (start+end)//2
    while computer_guess != number:
        computer_guess = (start+end)//2
        print("I think...", computer_guess)
        if computer_guess > number:
            end = computer_guess
        elif computer_guess < number:
            start = computer_guess + 1

    print('The answer was..', computer_guess,'!')


def main():
    number = int(input("Enter a number: "))
    if number < 1 or number > 100:
        print("Must be in range [1, 100]")
    else:
        comp_ans(number)

if __name__ == '__main__':
    main()