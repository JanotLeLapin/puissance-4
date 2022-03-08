from tkinter import *
import random

# Default values
W = 7  # Table width
H = 6  # Table height
L = 500  # Window width and height
CL = L  # Canvas width and height

# Create table
niggas = [[0 for _ in range(W)] for _ in range(H)]  # WxH size table

# Create window
win = Tk()

# Create main canvas
c = Canvas(
    win,
    width=L,
    height=L,
    bg="blue"
)
c.pack()


# Win conditions


def horizontal(player: int):
    for line in niggas:
        for i in range(4):
            if line[i] == player and line[i] == line[i+1] and line[i] == line[i+2] and line[i] == line[i+3]:
                return True
    return False


def vertical(player: int):
    for i in range(6):
        for j in range(3):
            if niggas[j][i] == player and niggas[j][i] == niggas[j+1][i] and niggas[j][i] == niggas[j+2][i] and niggas[j][i] == niggas[j+3][i]:
                return True
    return False


def diagonal_left(player: int):
    for i in range(3, 6):
        for j in range(4):
            if niggas[i][j] == player and niggas[i][j] == niggas[i-1][j+1] and niggas[i][j] == niggas[i-2][j+2] and niggas[i][j] == niggas[i-3][j+3]:
                return True
    return False


def diagonal_right(player: int):
    for i in range(3):
        for j in range(4):
            if niggas[i][j] == player and niggas[i][j] == niggas[i+1][j+1] and niggas[i][j] == niggas[i+2][j+2] and niggas[i][j] == niggas[i+3][j+3]:
                return True
    return False


def victory(player: int):
    return horizontal(player) or vertical(player) or diagonal_left(player) or diagonal_right(player)


def play(player: int, col: int) -> bool:
    for y in range(H - 1, -1, -1):
        if y < 0:
            return False
        if niggas[y][col] == 0:
            niggas[y][col] = player
            draw()
            return True


def ai_play():
    col = random.randint(0, W - 1)
    play(2, col)


def draw():
    for y in range(H):
        for x in range(W):
            v = niggas[y][x]
            c.create_oval(
                x*(CL/W),
                y*(CL/H),
                (x+1)*(CL/W),
                (y+1)*(CL/H),
                fill="white" if v == 0 else "yellow" if v == 1 else "red",
                outline="",
            )


def key_press(event):
    if event.char == 'q':
        win.destroy()

    code = event.keycode
    if code >= 49 and code < 57:
        play(1, code - 49)
    else:
        return

    if victory(1):
        print("Player 1 wins")
        return

    ai_play()
    if victory(2):
        print("Player 2 wins")
        return


draw()

win.bind('<KeyPress>', key_press)
win.mainloop()
