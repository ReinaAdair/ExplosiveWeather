import MineSweeperLibrary as MineSweeperBackEnd


"An example of how the minesweeper funcs can be strung together to run the game"
def main():
    print("main")
    MineSweeperObject = MineSweeperBackEnd.MineSweeperBoard("Easy")

    while(True):

        "You will have to write some kind of func in the GUI end that reads in the two board arrays to show the game board. This would replace this func."
        MineSweeperBackEnd.MineSweeperBoard.debug_board_console_print(MineSweeperObject)

        print("Please enter a negative number to end game. Otherwise just enter guess coordinates")

        x_coord = int(input("X: "))
        y_coord = int(input("Y: "))

        #loop breakout
        if (x_coord < 0  or y_coord < 0):
           if(input("Please Enter \'Y\' to restart game." )):
            MineSweeperObject.new_board()#restarts game/new board
           else:#if they dont want to restart 
            break
        else:#player guess
           MineSweeperBackEnd.MineSweeperBoard.Player_Reveal_Guess(MineSweeperObject, x_coord, y_coord)

        #win/lose check
        if(MineSweeperBackEnd.MineSweeperBoard.Win_Lose_Check(MineSweeperObject) ==  "win"):
           print("YOU WIN: " + str(MineSweeperObject.GameData.player_score))
           break
        else:
           if(MineSweeperBackEnd.MineSweeperBoard.Win_Lose_Check(MineSweeperObject) == "loss"):
             print("You are a FREAKING LOSER MAN: " + str(MineSweeperObject.GameData.player_score))
             break








#have this at the bottom of the page as this runs main 
if __name__ == "__main__":
    main()