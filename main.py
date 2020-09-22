import random

class MainGame():
    def __init__(self, reaching_number, increment, goesfirst):
        self.reaching_number = reaching_number
        self.increment = increment
        self.goesfirst = goesfirst
        
        #Total 
        self.total = 0
        self.current_choice = 0

        #ending win number
        self.ending_win_number = self.reaching_number - 1
        self.follow_increment = self.increment + 1

        self.win_number_list = []

        for i in range(self.ending_win_number, 0, -1 * self.follow_increment):
            self.win_number_list.append(i)

        self.win_number_list = sorted(self.win_number_list)

    def gotoplayerturn(self):

        if self.goesfirst == '0':
            self.no_input_character()
        
        elif self.goesfirst == '1':
            self.input_character()

    def no_input_character(self):
        print("The computer's turn:")
        print(f"\nCurrent total: {self.total}")

        if self.total not in self.win_number_list:
            #Input player not following winning strategy
            for i in self.win_number_list:
                if i > self.total and i - self.total <= self.increment:
                    self.current_choice = i -self.total

            print(f"The computer chooses: {self.current_choice}\n")
            
            self.total += self.current_choice

        elif self.total in self.win_number_list:
            #Input player is following winning strategy
            self.current_choice = random.randint(1, self.increment)
            print(f"The computer chooses: {self.current_choice}\n")
            self.total += self.current_choice

        if self.total >= self.reaching_number:
            #Game over
            print(f"The computer reached {self.reaching_number}.")
            print('The computer loses.')
        
        else:
            self.input_character()

    def input_character(self):
        #Input player's turn
        not_valid = True 
        while not_valid:
            print('\nYour turn:')
            print(f"\nCurrent total: {self.total}")
            print(f"Pick the increment (max: {self.increment})")
            self.current_choice = input("You choose: ")
            try:
                self.current_choice = int(self.current_choice)
                if not (1 <= self.current_choice <= self.increment):
                    #Input is invalid
                    raise(ValueError)

                else:
                    #Valid input
                    self.total += self.current_choice
                    not_valid = False
                    if self.total >= self.reaching_number:
                        print(f"You reached {self.reaching_number}")
                        print("You lose.")
                    else:
                        self.no_input_character()

            except ValueError:
                print("Enter valid command or integer.")
                not_valid = True

            #!We cannot check if larger here

                    



print('\nWelcome to the nim game! \nYou will count from 1 to the reaching number. \nSince the computer will perform the best possible moves to win, you can also use the program to beat your friend!')

not_valid = True
while not_valid:
    try:
        print("\nThe reaching number has to be between 20 and 100 inclusive")
        reaching_number_str = input("Enter reaching number: ")
        print('\nThe increment has to be between 3 and 10 (inclusive)')
        increment_str = input("Enter max increment: ")
        reaching_number = int(reaching_number_str)
        increment = int(increment_str)
        if (not 20 <= reaching_number <= 100) or (not 3 <= increment <= 10):
            #not valid
            raise(ValueError)
        else:
            #valid
            goesfirst = input("Who goes first 0(The computer) or 1 (player)>")
            if goesfirst in ['0', '1']:
                game = MainGame(reaching_number, increment, goesfirst)
                game.gotoplayerturn()
                not_valid = False
            else:
                raise(ValueError)
            

    except ValueError:
        print('Enter a valid command or integer')
        not_valid = True
