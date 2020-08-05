import random
class MainGame():
    def __init__(self, reaching_number, increment, players, goesfirst):
        self.reaching_number = reaching_number
        self.increment = increment
        self.players = players
        self.goesfirst = goesfirst
        self.no_input_header = None
        self.no_input_choice = None
        self.input_header = None
        self.input_choice = None
        #*Keeps track of the previous numbers
        self.total = 0
        self.last_choice = 0
        self.current_choice = 0

        #*When printing out the results, I can use general variables.
        
        #*Finding the reaching_number - 1 number 
        self.ending_win_number = self.reaching_number - 1
        self.follow_increment = self.increment + 1
        self.starting_win_number = self.ending_win_number % self.follow_increment

        #*Rather than making the move based on  the past move, I should try to get it close to the win_number_list
        self.win_number_list = []
        

    def gotoplayerturn(self):
        if self.players == '0':
            #*I will add a function here
            self.no_input_header = "\nThe computer's turn:"
            self.no_input_choice = "The computer chooses: "
            self.no_input_lose = "The computer loses."
            self.input_header = "\nYour turn:"
            self.input_choice = "You choose: "
            self.input_lose = "You lose."

        
        elif self.players == '1':
            self.no_input_header = "\nYour turn: "
            self.no_input_choice = "You (should) choose: "
            self.no_input_lose = "You lose."
            self.input_header = "\nYour friend's turn: "
            self.input_choice = "What did your friend choose?: "
            self.input_lose = "Your friend loses."

        if self.goesfirst == '0':
            self.no_input_character()

        elif self.goesfirst == '1':
            self.input_character()

    def no_input_character(self):
        #*This function os for the characters without inputs (computer, you advice)
        print(self.no_input_header)
        print(f"\nCurrent total: {self.total}")
        if self.starting_win_number > self.total:
            self.current_choice = self.starting_win_number
            print(f"{self.no_input_choice} {self.current_choice}\n")
            self.total += self.current_choice
            self.last_choice = self.current_choice
            #self.input_character()

        elif self.starting_win_number < self.total:
            self.current_choice = self.follow_increment - self.last_choice
            print(f"{self.no_input_choice} {self.current_choice}\n")
            self.total += self.current_choice
            self.last_choice = self.current_choice
            #self.input_character()
        
        #*Just in case the player knows the strategy and there is no hope to win.
        #*I will pick a random int
        elif self.starting_win_number == self.total:
            self.current_choice = random.randint(1, self.increment)
            print(f"{self.no_input_choice} {self.current_choice}\n")
            self.total += self.current_choice
            self.last_choice = self.current_choice
        
        if self.total >= 30:
            print(self.no_input_lose)
        else:
            self.input_character()

    def input_character(self):
        #*This function is for the characters with inputs (you, your friend)
        not_valid = True
        while not_valid:
            print(self.input_header)
            print(f"\nCurrent total: {self.total}")
            self.input_num = input(f"Pick the increment (max:{self.increment}): ")
            try:
                self.input_num = int(self.input_num)
                if not 1 <= self.input_num <= self.increment:
                    raise(ValueError)
                else:
                    print(f"{self.input_choice} {self.input_num}\n")
                    self.total += self.input_num
                    self.last_choice = self.input_num
                    self.last_choice = self.input_num
                    not_valid = False
                    self.no_input_character()
            except ValueError:
                print("Enter valid command or integer.")
                not_valid = True


print("\nWelcome to the nim game! \nYou will count from 1 to the reaching number. \nYou will choose the max increment and the reaching number.\nSince the computer will perform the best possible moves to win, you can use this program to beat your friends!")
not_valid = True
while not_valid:
    print("\nThe reaching number has to be between 20 and 100 (inclusive).")
    reaching_number_str = input("Enter reaching number: ")
    print("\nThe max increment has to be between 3 and 10 (inclusive).")
    incement_str = input("Enter max increment: ")
    players = input("Enter '0' if you are playing against the computer.\nEnter '1' if you want to beat a friend. (You will input your friend's move into the game).\n>")


    try:
        reaching_number = int(reaching_number_str)
        increment = int(incement_str)
        not_valid = False
        if (not 20 <= reaching_number <= 100) or (not 3 <= increment <= 10) or (players not in ['0', '1']):
            raise(ValueError)
        else:
            if players == '0':
                zero_player = "The computer"
                one_player = "You"
            else:
                zero_player = "You (receive advice)"
                one_player = "Your friend"
            goesfirst = input(f"Who goes first: 0({zero_player}) or 1({one_player})>")
            game = MainGame(reaching_number, increment, players, goesfirst)
            game.gotoplayerturn()
        


    except ValueError:
        print("Enter a valid command or integer.")
        not_valid = True


        