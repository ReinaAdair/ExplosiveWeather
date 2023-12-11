#test
#print("MineSweeperLibrary Run")

#imports 
import numpy
import random
from copy import deepcopy
#Board presets 
"I do it this way so that MineSweeperBoard can stay relatively clean as putting in these presets would bloat the code."
"PS if add a preset NEW_BOARD NEEDS TO BE UPDATED ACCORDINGLY"

"Board_Preset_1 Easy"
"-1  3  2  1  0"
" 2 -1 -1  1  0"
" 1  2  3  1  1"
" 1  1  2 -1  1"
" 1 -1  2  1  1"
Board_Preset_1_easy = [[-1, 3, 2, 1, 0],[2, -1, -1, 1, 0], [1, 2, 3, 1, 1], [ 1, 1, 2, -1, 1], [1, -1, 2, 1, 1]]

"Board_Preset_2_easy"
"-1  2  1  0  0"
" 3 -1  2  0  0"
" 2 -1  2  0  0"
" 2  2  1  0  0"
"-1  1  0  0  0"
Board_Preset_2_easy = [[-1, 2, 1, 0, 0],[3,-1, 2, 0, 0],[2,-1, 2, 0, 0],[2, 2, 1, 0, 0],[-1, 1, 0, 0, 0]]

"Board_Preset_3_easy"
"-1  1  0  0  0"
" 1  2  1  1  0"
" 0  1 -1  1  0"
" 0  1  1  2  1"
" 0  0  0  1 -1"
Board_Preset_3_easy = [[-1, 1, 0, 0, 0], [1, 2, 1, 1, 0], [0, 1, -1, 1, 0], [0, 1, 1, 2, 1], [0, 0, 0, 1, -1]]

"Board_Preset_4_easy"
" 0  0  2 -1  2"
" 0  0  2 -1  2"
" 1  2  3  2  1"
" 1 -1 -1  1  0"
" 1  2  2  1  0"
Board_Preset_4_easy = [[0, 0, 2, -1, 2], [0, 0, 2, -1, 2], [1, 2, 3, 2, 1], [1, -1, -1, 1, 0], [1, 2, 2, 1, 0]]


Board_Revealed_Preset_easy = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]


"Board_Preset_1_hard"
" 1  1  0  0  1  1  1  0"
"-1  1  1  1  2 -1  1  0"
" 2  2  2 -1  3  2  2  1"
"-1  1  2 -1  2  1 -1  1"
" 2  2  2  1  2  2  2  1"
" 1 -1  2  1  2 -1  2  1"
" 1  1  2 -1  1  2 -1  1"
" 0  0  1  1  1  1  1  1"
Board_Preset_1_hard = [[1, 1, 0, 0, 1, 1, 1, 0], [-1, 1, 1, 1, 2, -1, 1, 0], [2, 2, 2, -1, 3, 2, 2, 1], [-1, 1, 2, -1, 2, 1, -1, 1], [2, 2, 2, 1, 2, 2, 2, 1], [1, -1, 2, 1, 2, -1, 2, 1],[1, 1, 2, -1, 1, 2, -1, 1],[0, 0, 1, 1, 1, 1, 1, 1]]


"Board_Preset_2_hard"
" 0  1  1  1  1  1  1  0"
" 0  2 -1  2  2 -1  2  0"
" 1  3 -1  2  2 -1  3  1"
"-1  4  2  1  1  2  4 -1"
"-1 -1  3  1  1  3 -1 -1"
" 2 -1 -1  4  4 -1 -1  2"
" 1  3 -1 -1 -1 -1  3  1"
" 0  1  2  3  3  2  1  0"
Board_Preset_2_hard = [[0, 1, 1, 1, 1, 1, 1, 0],[ 0, 2, -1, 2, 2, -1, 2, 0],[1, 3, -1, 2, 2, -1, 3, 1],[-1, 4, 2, 1, 1, 2, 4, -1],[-1, -1, 3, 1, 1, 3, -1, -1],[2, -1, -1, 4, 4, -1, -1, 2],[1, 3, -1, -1, -1, -1, 3, 1],[0, 1, 2, 3, 3, 2, 1, 0]]


"Board_Preset_3_hard"
" 1  1  1  0  0  1  1  1"
" 1 -1  1  0  0  1 -1  1"
" 2  2  2  0  1  2  2  1"
" 1 -1  1  1  2 -1  1  0"
" 1  1  1  1 -1  2  1  0"
" 0  1  1  2  1  2  1  1"
" 0  1 -1  1  0  1 -1  1"
" 0  1  1  1  0  1  1  1"
Board_Preset_3_hard = [[ 1, 1, 1, 0, 0, 1, 1, 1], [1, -1, 1, 0, 0, 1, -1, 1], [2, 2, 2, 0, 1, 2, 2, 1], [1, -1, 1, 1, 2, -1, 1, 0], [1, 1, 1, 1, -1, 2, 1, 0], [0, 1, 1, 2, 1, 2, 1, 1], [0, 1, -1, 1, 0, 1, -1, 1], [0, 1, 1, 1, 0, 1, 1, 1]]


"Board_Preset_4_hard"
"-1 -1 -1 -1 -1 -1 -1 -1"
"-1 -1 -1 -1 -1 -1 -1 -1"
"-1 -1 -1 -1  5  3  5 -1"
"-1 -1 -1 -1  3  0  3 -1"
"-1 -1 -1 -1  5  3  5 -1"
"-1 -1 -1 -1 -1 -1 -1 -1"
"-1 -1 -1 -1 -1 -1 -1 -1"
"-1 -1 -1 -1 -1 -1 -1 -1"
Board_Preset_4_hard = [[-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, 5, 3, 5, -1], [-1, -1, -1, -1, 3, 0, 3, -1], [-1, -1, -1, -1, 5, 3, 5, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1]]

Board_Revealed_Preset_hard = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]]

"Class MineSweeperGame - A MinesweeperGame object was added to MineSweeperBoard"
"-This object encapsulates everything needed to keep track of the current game"
class MineSweeperGame:

  "-player score var, each time the user successfully guesses (square with no bomb), the score gets updated"
  #this was originally private but ive made it public
  player_score = 0

  "Returns current score"
  def score_get(self):
    return self.player_score
  
  "-Allows manual update of the score, adds whatever parameter to score"
  def Score_Manual_Update(self, int_score):
    self.player_score += int_score
  
  "-default AAA not needed but Im going to leave this in here in case it is needed"
  UserName ="AAA"

  "-Game difficulty determines the game board used"
  #options are 'Easy' and 'Hard'
  __GameDifficulty = "Easy"

  "-returns game difficulty"
  def difficulty_get(self):
    return self.__GameDifficulty

  "used to set the difficulty of the game"
  def difficulty_set(self, new_difficulty):
    
    if(new_difficulty == "Easy" or new_difficulty == "Hard"):#data validation, if invalid sets to Easy by default
      self.__GameDifficulty = new_difficulty
    else:
      self.__GameDifficulty = "Easy"

  "-Constructor"
  def __init__(self, difficulty):
    self.difficulty_set(difficulty)#sets difficulty



"Class MineSweeperBoard"
"-This object stores all data revelant to the minesweeper board and preforms any immediate relevant game tasks"
" PS for all functions the indexes are going to be automatically adjusted so you do not need to -1 on the indexes"
class MineSweeperBoard():
  
  "Board_Array"
  "-An array that stores bomb data of the board in a (x, y) format. the top left is considered to be the origin"
  "-Note: Bomb_data > 0 means the amount of bombs near that square, Bomb_data == 0, no bomb there or near"
  "-      Bomb_data == -1 means that there is a bomb there."
  #dummy values, you may have to import numpy in order to use funcs like .copy
  board_Array = numpy.array([0])

  "board_Array_Revealed"
  "-keeps track of whether or not the square has been revealed.  hidden =  0, revealed = 1, flagged == -1 "
  "then the square is non-revealed and flagged."
  board_Array_Revealed = numpy.array([0])

  "defines board size based on difficulty"
  __board_row_length = 5
  __board_column_length = 5

  "-keeps track of whether the game has been lost or won. I assumed doing it this way would make it easier for Jessica to watch for a loss condition"
  "instead of her also having to look for a loss/win condition. 1 (true) = won, 0 (neutral) =  no win/loss, -1 (false) = loss"
  Win_Loss_Flag = 0

  "-This holds the board preset that was randomly chosen, after board object constructor this wil mainly be used for debug."
  Board_Preset =  0

  "-I decided to move the minesweepergame data object into the minesweeper board instead of vice versa" 
  GameData = MineSweeperGame("Easy")

  #"constructor"
  "-Chooses from the board presets (based on difficulty) and populates the board."
  def __init__(self, difficulty):
    
    #changes difficulty
    self.GameData.difficulty_set(difficulty)
    
    #creates new board
    self.new_board()

  "-When the player selects a square that does not have a bomb or is next to one, Bomb_data == 0,"
  "The remaining touching squares are removed until squares touching bombs are revealed"
  "V4.2 - fixed a big logic error, the the func does not reveal the squares on the 'outer edge' of the cleared area that has bomb data/adjacent bombs"
  "V4.2 - also updated the x, y vars to make more sense for sense in reference to an array"
  #we are asssuming that the coordinates have already been converted into indexes
  @staticmethod
  def __Board_Bombless_Clear(self, row, col):
     #x = rows, y = columns, kinda weird but its makes sense to me

     #reveals the current location
     self.board_Array_Revealed[row][col] = 1
     
     #checks indexes one "up", "down", "left", "right", if the index exists and there is not a bomb there and the square has not been revealed, recursively call the func 
     #in order to check all bombless squares in section and reveal them
     if(row + 1 < self.__board_row_length and row + 1 > -1):#up, doesnt need x + 1 > -1 but kept it for consistancy
      if(self.board_Array[row+1][col] == 0 and self.board_Array_Revealed[row+1][col] != 1):
       self.__Board_Bombless_Clear(self, row+1, col)
       self.GameData.Score_Manual_Update(5)#updates game score
      else:
        self.board_Array_Revealed[row+1][col] = 1 #reveals edge
        self.GameData.Score_Manual_Update(10)

     if(row - 1 < self.__board_row_length and row - 1 > -1):#down, if index exists
      if(self.board_Array[row-1][col] == 0 and self.board_Array_Revealed[row-1][col] != 1):
       self.__Board_Bombless_Clear(self, row-1, col)
       self.GameData.Score_Manual_Update(5)#updates game score
      else:
        self.board_Array_Revealed[row-1][col] = 1 #reveals edge
        self.GameData.Score_Manual_Update(10)

     if(col - 1 < self.__board_column_length and col - 1 > -1):#left, if index exists 
      if(self.board_Array[row][col -1] == 0 and self.board_Array_Revealed[row][col-1] != 1):#if the square is bombless and non revealed
       self.__Board_Bombless_Clear(self, row, col -1)
       self.GameData.Score_Manual_Update(5)#updates game score
      else:
        self.board_Array_Revealed[row][col-1] = 1 #if it is a 'edge' with bomb data, reveal it
        self.GameData.Score_Manual_Update(10)

     if(col + 1 < self.__board_row_length and col + 1 > -1):#right, if index exists 
      if(self.board_Array[row][col+1] == 0 and self.board_Array_Revealed[row][col+1] != 1):#if the square is bombless and non revealed
       self.__Board_Bombless_Clear(self, row, col+1)
       self.GameData.Score_Manual_Update(5)#updates game score
      else:
        self.board_Array_Revealed[row][col+1] = 1 #if it is a 'edge' with bomb data, reveal it
        self.GameData.Score_Manual_Update(10)


  "-This function takes the players guess and reveals the specified square, If it is a bomb update the "
  " Win_loss_Flag and return a -1, otherwise return the Bomb_data. If the Bomb_data == 0, call Board_Bombless_Clear(x, y)."
  #takes coordinates based out of the top left
  def Player_Reveal_Guess(self, x, y):
     #Adjusting coords to indexes
     row_index = y-1
     col_index = x-1 
  
    #reveals square 
     self.board_Array_Revealed[row_index][col_index] = 1

    #checks for bomb
     if(self.board_Array[row_index][col_index] == -1): #if there is a bomb
      #trips loss conditions
      self.Win_Loss_Flag = -1
      return -1
     else: 
        if(self.board_Array[row_index][col_index] == 0): # if there are no bombs adjacent, clear area on board
           MineSweeperBoard.__Board_Bombless_Clear(self, row_index, col_index)

        #updates game score
        self.GameData.Score_Manual_Update(10)

        #if the guess was correct and there is no bomb there, return the number of bombs that are adjacent
        return self.board_Array[row_index][col_index] 
     

  
  "-this checks the board to see if the player has won or lost. First checks lost var, then increments through "
  "the Board_Array to find if there are any non revealed non bomb squares left. If won returns 'win', lost returns 'loss',"
  "no win or loss returns 'continue"
  def Win_Lose_Check(self):
   
   #checks if loss condition flag has been tripped
   if(self.Win_Loss_Flag == -1):
     return "loss"

   #index values
   row_index = 0
   col_index = 0
   
   #iterates through the boards to look for a win condition, if all bombless squares are revealed then the player has won. 
   while (row_index < self.__board_row_length):
     while (col_index < self.__board_column_length):
       #debug stuff
       #print("row: " + str(row_index)  + ", col: " + str(col_index))
       if(self.board_Array_Revealed[row_index][col_index] == 0 and self.board_Array[row_index][col_index] != -1):#if the current index location is both a non-bomb and is not revealed, return 'continue'
         return "continue" #player has not won because they still need to reveal some non-bomb square
       col_index = col_index + 1 # increments column
      
     #resets for next row 
     col_index = 0
     row_index =  row_index + 1 #increments row
   
   #win condition has been found 
   Win_Loss_Flag =  1
   return "win"
      

       
  "-this is mainly used for debugging minesweeperBoard or debugging in general. All it does is print out both"
  "of the current boards"
  def debug_board_console_print(self):

    #output string, the func iterates through both arrays and puts together a string for the final output as it goes
    BoardOutputString = ""
    RevealedOutputString =  ""
    #index values
    col = 0
    row = 0
    while(row < self.__board_row_length):
      while(col < self.__board_column_length):
            #debug print
            #print("col"+ str(col) + " " + "row" + str(row)+ " : " + str(self.board_Array[row][col]))

            #if statements to correct spacing due to negative numbers
            if(self.board_Array[row][col] >= 0): # if current board value is positive, add an additional space
               BoardOutputString += " "
            
            if(self.board_Array_Revealed[row][col] >= 0): # if current revealed board value is positive, add an additional space
               RevealedOutputString += " "
               
            #adds current board value to output string
            BoardOutputString += " " + str(self.board_Array[row][col])

            #adds current revealed board value to output string
            RevealedOutputString += " " + str(self.board_Array_Revealed[row][col])


            col = col + 1
      #resets for new row in board 
      BoardOutputString += "\n"
      RevealedOutputString += "\n"
      row = row + 1
      col = 0
    
    #debug output
    print("This is the main board array/bomb array")
    print(BoardOutputString)
    print("This is the revealed board array")
    print(RevealedOutputString)


  "-This flags a non-revealed square at the point x, y"
  def flag_square(self, x, y):
    
    #coordinates to indexes 
    row_index = y-1
    column_index = x-1

    #checks to make sure square isnt already revealed
    if(self.board_Array_Revealed[row_index][column_index] == 0):
      self.board_Array_Revealed[row_index][column_index] = -1 #flags the square


  "-used to validate user coordinate information, this is not used in any of the above methods. The above methods assume that the user data has"
  "already been validated. Accepts Coordinates NOT indexes, returns true if both coords are valid."
  @staticmethod
  def user_input_validation(self, x_coord, y_coord):
    if(x_coord > 0 and x_coord < self.__board_column_length):#validates x-coords
      if(y_coord > 0 and y_coord < self.__board_row_length ):#validates y-coords
          return True
      else:
        return False
    else:
      return False
    

  "-used to keep track of all of the previously played boards "
  previous_boards_easy = numpy.array([0])
  previous_boards_hard = numpy.array([0])


  "-used to select boards to either start or restart the game. Uses the previous boards arrays to avoid using the same board repeatively,  " 
  "Note: If you want to change the difficulty, change difficulty first and then call this func to make a new board with new difficulty"
  "V4.2 Also fixed bug where it would reuse old boards"
  def new_board(self):
    #random num used to select board 
    random_board_num = 0

    #updates index lengths for boards 
    if(self.GameData.difficulty_get() ==  "Easy"):
      self.__board_row_length = 5
      self.__board_column_length = 5
    else: #if game is hard
      self.__board_row_length = 8
      self.__board_column_length = 8



    #holds number of easy boards so that we know when to reset prvious boards 
    num_of_easy_boards = 4 + 1 #since the array cant be empty, add one for the array index that is never empty
    #akin to num_of_easy_boards
    num_of_hard_boards = 4 + 1

    #keeps generating new board numbers until an unused one is found
    while(True):
      random_board_num = random.randint(1,4)#new random num
      #print("random number " + str(random_board_num))#debug

      if(self.GameData.difficulty_get() == "Easy"):#easy difficulty boards 
        #print(self.previous_boards_easy) #debug stuff
        if(random_board_num in self.previous_boards_easy):#checks if current board has been used
          if(len(self.previous_boards_easy) >= num_of_easy_boards):#if all boards have been used
            self.previous_boards_easy = numpy.array([0])#resets used boards
          else:
           continue #easy board has already been used 
        else:#found an acceptable easy board
          self.previous_boards_easy = numpy.append(self.previous_boards_easy, random_board_num)#adds to used board
          self.board_Array_Revealed = deepcopy(Board_Revealed_Preset_easy)#resets revealed board, must use imported deepcopy(), otherwise its a shallow copy/point to the same object 
          break
      else: #hard difficulty boards
        if(random_board_num in self.previous_boards_hard):#checks if current board has been used
          if(len(self.previous_boards_hard) >= num_of_hard_boards):#if all boards have been used
            self.previous_boards_hard = numpy.array([0])#resets used boards
          else:
            continue #hard board has already been used 
        else:#found an acceptable hard board
          self.previous_boards_hard = numpy.append(self.previous_boards_hard, random_board_num)#adds to used boards
          self.board_Array_Revealed = deepcopy(Board_Revealed_Preset_hard)#resets revealed board, must use imported deepcopy(), otherwise its a shallow copy/point to the same object 
          break


    #debug stuff
    #print(self.previous_boards_easy)
    #print(self.previous_boards_hard)

    
    #actually sets the board
    if(self.GameData.difficulty_get() == "Easy"):
     match random_board_num: #a case needs to be made for each board preset
       case 1:
         self.board_Array = Board_Preset_1_easy.copy()
         self.Board_Preset = 1
       case 2:
         self.board_Array = Board_Preset_2_easy.copy()
         self.Board_Preset = 2
       case 3:
         self.board_Array = Board_Preset_3_easy.copy()
         self.Board_Preset = 3
       case 4:
         self.board_Array = Board_Preset_4_easy.copy()
         self.Board_Preset = 4
    else:#if difficulty hard
       match random_board_num: #a case needs to be made for each board preset
        case 1:
         self.board_Array = Board_Preset_1_hard.copy() 
         self.Board_Preset = 1
        case 2:
         self.board_Array = Board_Preset_2_hard.copy() 
         self.Board_Preset = 2
        case 3:
         self.board_Array = Board_Preset_3_hard.copy() 
         self.Board_Preset = 3
        case 4:
         self.board_Array = Board_Preset_4_hard.copy() 
         self.Board_Preset = 4