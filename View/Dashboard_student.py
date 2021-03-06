
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()



def nextPage():
    window.destroy()
    import before_exam

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
    828.0,
    fill="#023E8A",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("Dash_image_1.png"))
image_1 = canvas.create_image(
    165.9999999999999,
    152.00000000000006,
    image=image_image_1
)

canvas.create_text(
    56.000000000000114,
    321.00000000000006,
    anchor="nw",
    text="BirdEye",
    fill="#FFFFFF",
    font=("Satisfy Regular", 64 * -1)
)

canvas.create_rectangle(
    327.9999999999999,
    53.00000000000006,
    1311.0,
    834.0,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("Dash_button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=nextPage,
    relief="flat"
)
button_1.place(
    x=437.9999999999999,
    y=116.00000000000006,
    width=338.0,
    height=215.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("Dash_button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=nextPage,
    relief="flat"
)
button_2.place(
    x=853.9999999999999,
    y=372.00000000000006,
    width=338.0,
    height=215.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("Dash_button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=nextPage,
    relief="flat"
)
button_3.place(
    x=437.9999999999999,
    y=372.00000000000006,
    width=338.0,
    height=215.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("Dash_button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=nextPage,
    relief="flat"
)
button_4.place(
    x=853.9999999999999,
    y=116.00000000000006,
    width=338.0,
    height=215.0
)
window.resizable(False, False)
window.mainloop()
