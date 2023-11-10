import PySimpleGUI as sg
from random import randint ##temp



sg.theme('BluePurple')

#main game window - persistent

menu_def = [['File', ['Exit']],
            ['Settings'],
            ['Help'],]

layoutMine = [
    [sg.Menu(menu_def, )],
    [[sg.Button('?', size=(4, 2), key=(i, j), pad=(0,0)) for j in range(5)] for i in range(5)]      #the 5 for row and column are placeholder values
    ]

#test###########
board = [[randint(0,1) for j in range(5)] for i in range(5)]  #placeholder
######################

window = sg.Window('Minesweeper', layoutMine)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    window[event].update(board[event[0]][event[1]], button_color=('white','black'))


window.close()
##### while true loop for window

#button for new game
#button for settings
#button to switch between flagging and clicking/differentiate between right and left clicks





#death window - persistent until new game

#button for new game
#button for settings




#settings window

#change ui color??
#change weather location????


#weather menu


