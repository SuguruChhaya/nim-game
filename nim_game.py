print("\nWelcome to the nim game! \nYou will count from 1 to the reaching number. \nYou will choose the max increment and the reaching number.\nSince the computer will perform the best possible moves to win, you can use this program to beat your friends!")
not_valid = True
while not_valid:
    print("\nThe reaching number has to be between 20 and 100 (inclusive).")
    reaching_number_str = input("Enter reaching number: ")
    print("\nThe max increment has to be between 3 and 10 (inclusive).")
    inciment_str = input("Enter max increment: ")

    try:
        reaching_number = int(reaching_number_str)
        increment = int(inciment_str)
        not_valid = False
        if not 20 <= reaching_number <= 100 or not 3 <= increment <= 10:
    except ValueError:
        print("Choose a valid integer.")
        not_valid = True
        