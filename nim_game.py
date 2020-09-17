import random
'''
Not to create objects but just to manage the methods. 
'''
class MainGame():
    def __init__(self, reaching_number, increment, goesfirst):
        self.reaching_number = reaching_number
        self.increment = increment
        self.goesfirst = goesfirst
        #*Keeps track of the previous numbers
        self.total = 0
        self.current_choice = 0

        #*Finding the reaching_number - 1 number 
        self.ending_win_number = self.reaching_number - 1
        self.follow_increment = self.increment + 1

        #*Rather than making the move based on  the past move, I should try to get it close to the win_number_list
        self.win_number_list = []
        for i in range(self.ending_win_number, 0, -1 * self.follow_increment):
            self.win_number_list.append(i)
        self.win_number_list = sorted(self.win_number_list)
    
        self.no_input_player = "The computer"
        self.no_input_header = "\nThe computer's turn:"
        self.no_input_choice = "The computer chooses: "
        self.no_input_lose = "The computer loses."
        self.input_player = "You"
        self.input_header = "\nYour turn:"
        self.input_choice = "You choose: "
        self.input_lose = "You lose."

    def gotoplayerturn(self):


        if self.goesfirst == '0':
            self.no_input_character()

        elif self.goesfirst == '1':
            self.input_character()

    def no_input_character(self):
        #*This function os for the characters without inputs (computer, you advice)
        print(self.no_input_header)
        print(f"\nCurrent total: {self.total}")

        if self.total not in self.win_number_list:
            for i in self.win_number_list:
                if i > self.current_choice and  i - self.total <= self.increment:
                    self.current_choice = i - self.total
            print(f"{self.no_input_choice} {self.current_choice}\n")
            self.total += self.current_choice
        
        #*Just in case the player knows the strategy and there is no hope to win,
        #*I will pick a random int
        elif self.total in self.win_number_list:
            self.current_choice = random.randint(1, self.increment)
            print(f"{self.no_input_choice} {self.current_choice}\n")
            self.total += self.current_choice
        
        if self.total >= self.reaching_number:
            print(f"{self.no_input_player} reached {self.reaching_number}.")
            print(self.no_input_lose)
        else:
            self.input_character()

    def input_character(self):
        #*This function is for the characters with inputs (you, your friend)
        not_valid = True
        while not_valid:
            print(self.input_header)
            print(f"\nCurrent total: {self.total}")
            print(f"Pick the increment (max:{self.increment})")
            self.input_num = input(f"{self.input_choice}")
            try:
                self.input_num = int(self.input_num)
                if not 1 <= self.input_num <= self.increment:
                    raise(ValueError)
                else:
                    self.total += self.input_num
                    self.current_choice = self.input_num
                    self.current_choice = self.input_num
                    not_valid = False
                    if self.total >= self.reaching_number:
                        print(f"{self.input_player} reached {self.reaching_number}.")
                        print(self.input_lose)
                    else:
                        self.no_input_character()
            except ValueError:
                print("Enter valid command or integer.")
                not_valid = True


print("\nWelcome to the nim game! \nYou will count from 1 to the reaching number. \nYou will choose the max increment and the reaching number.\nSince the computer will perform the best possible moves to win, you can use this program to beat your friends!")
not_valid = True
while not_valid:

    try:
        print("\nThe reaching number has to be between 20 and 100 (inclusive).")
        reaching_number_str = input("Enter reaching number: ")
        print("\nThe max increment has to be between 3 and 10 (inclusive).")
        incement_str = input("Enter max increment: ")
        reaching_number = int(reaching_number_str)
        increment = int(incement_str)
        not_valid = False
        if (not 20 <= reaching_number <= 100) or (not 3 <= increment <= 10):
            raise(ValueError)
        else:

            zero_player = "The computer"
            one_player = "You"
            goesfirst = input(f"Who goes first: 0({zero_player}) or 1({one_player})>")
            if goesfirst in ['1', '2']:
                game = MainGame(reaching_number, increment, goesfirst)
                game.gotoplayerturn()
            else:
                raise (ValueError)
        


    except ValueError:
        print("Enter a valid command or integer.")
        not_valid = True


        