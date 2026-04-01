class Player:
    def __init__(self, symbol, name): #to give a player a symbol and name
        self.symbol = symbol
        self.name = name
        self.score = 0

    def __str__(self): #what happens when we print it
        return f"{self.name} ({self.symbol})"
    
    def increase_score(self): #increasing the score of wins
        self.score += 1

class Game:#class for the game
    def __init__(self, name_x, name_o):
        self.board = [] #that's where we play
        self.player_x = Player('X', name_x) #name of x player
        self.player_o = Player('O', name_o) #name of o player
        self.reset_game() #to reset the game and play again

    def reset_game(self):
        """Start the new game by getting board and player"""
        self.init_board()
        self.current_player = self.player_x

    def init_board(self):
        """Making an empty board"""
        self.board = [
            ['-','-','-'],['-','-','-'],['-','-','-']
        ]
    
    def display_board(self):
        """display it properly"""
        for r in range(3):
            for c in range(3):
                print(self.board[r][c], end=' ')
            print()

    def play(self,row,col): #the gameplay phase
        """
        make sure row and col are in range of 1-3
        make sure that row-col is available
        assign it to the player
        change player
        """

        if row < 1 or row > 3 or col < 1 or col > 3: #checking for range, if out - return
            print("Invalid row or col")
            return
        row -=1 #for the index of the list
        col -=1
        if self.board[row][col] != '-':#checking if its taken already
            print("Position taken")
            return
        self.board[row][col] = self.current_player.symbol #put the symbol
        if self.current_player == self.player_x:#change player, if its x then to o, else to x
            self.current_player = self.player_o
        else:
            self.current_player = self.player_x

    def check_winner(self):
        #check every row
        for r in range(3):
            if self.board[r][0] == self.board[r][1] == self.board[r][2] and self.board[r][0] != '-': 
                #check if they are the same in a row and that they are not '-'
                return self.board[r][0]#return the symbol of the winner
        #check every column
        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] and self.board[0][c] != '-':
                return self.board[0][c]
        #check right diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '-':
            return self.board[0][0]
        #check left diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '-':
            return self.board[0][2]
        #no winner found
        return None
        
    def check_tie(self):
        """check that there are still dashes '-' and say its not tie until it is"""
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == '-':
                    return False
        #when no '-' found - assume its a tie
        return True

    def update_score(self, winner): #increase score depending on who won, if there is no win - invalid player
        if winner == 'X':
            self.player_x.increase_score()
        elif winner == 'O':
            self.player_o.increase_score()
        else:
            print("invalid player")
        
    def save_score(self):
        """we save it into file"""
        file = open('Homeworks/Homework6/tictactoe_score.csv', 'a')
        row = f"{self.player_x.name}, {self.player_o.name}, {self.player_x.score}, {self.player_o.score}\n"
        file.write(row)
        file.close


#getting the names
name_x = input("Player x name: ")
name_o = input("Player o name: ")
game = Game(name_x, name_o)

play_again = 'y'

#as long as we say "y" to play again - this will work
while play_again == 'y':
    game.display_board() #show the board
    print(f"{game.current_player} plays:")
    row = int(input("give row (1-3): "))
    col = int(input("give col (1-3): "))
    game.play(row,col) #player does the play
    winner = game.check_winner()
    if winner is not None:
        game.display_board()
        print(f"Winner {game.check_winner()}")
        game.update_score(winner) #we check for winner, if not - other player moves


    #we check for a tie
    tie = False
    if winner is None:
        tie = game.check_tie()
        if tie:
            game.display_board()
            print("Its a tie")

    #when we got a winner, do we play again?
    if winner is not None or tie:
        play_again = input("play again? y/n ")
        if play_again == 'y':
            game.reset_game()

#saving the score into .csv file
game.save_score()

print("bye")