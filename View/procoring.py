
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
def video():
    os.system("C:\Users\RAHEEM2000\Documents\BirdEye\BirdEye\View\Recording.avi")



window.geometry("1531x828")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 828,
    width = 1531,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"

)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1531.0,
    832.0,
    fill="#023E8A",
    outline="")

canvas.create_rectangle(
    1096.0,
    579.0,
    1448.0,
    803.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    591.0,
    579.0,
    943.0,
    803.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    88.0,
    575.0,
    440.0,
    799.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    88.0,
    305.0,
    440.0,
    529.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    164.0,
    325.0,
    anchor="nw",
    text="person 4",
    fill="#000000",
    font=("Satisfy Regular", 64 * -1)
)

canvas.create_rectangle(
    88.0,
    31.0,
    440.0,
    255.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    592.0,
    305.0,
    944.0,
    529.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    589.0,
    31.0,
    941.0,
    255.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    1096.0,
    305.0,
    1448.0,
    529.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    1096.0,
    31.0,
    1448.0,
    254.9110870361328,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    1172.0,
    601.0,
    anchor="nw",
    text="person 9",
    fill="#000000",
    font=("Satisfy Regular", 64 * -1)
)

canvas.create_text(
    668.0,
    327.0,
    anchor="nw",
    text="person 5",
    fill="#000000",
    font=("Satisfy Regular", 64 * -1)
)

canvas.create_text(
    668.0,
    601.0,
    anchor="nw",
    text="person 8",
    fill="#000000",
    font=("Satisfy Regular", 64 * -1)
)

canvas.create_text(
    163.0,
    601.0,
    anchor="nw",
    text="person 7",
    fill="#000000",
    font=("Satisfy Regular", 64 * -1)
)

canvas.create_text(
    170.0,
    52.0,
    anchor="nw",
    text="person 1",
    fill="#000000",
    font=("Satisfy Regular", 64 * -1)
)

canvas.create_text(
    668.0,
    52.0,
    anchor="nw",
    text="person 2",
    fill="#000000",
    font=("Satisfy Regular", 64 * -1)
)

canvas.create_text(
    1172.0,
    325.0,
    anchor="nw",
    text="person 6",
    fill="#000000",
    font=("Satisfy Regular", 64 * -1)
)

canvas.create_text(
    1172.0,
    52.0,
    anchor="nw",
    text="person 3",
    fill="#000000",
    font=("Satisfy Regular", 64 * -1)
)
window.resizable(False, False)
window.mainloop()