from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
#window.config(width=200,height = 200,bg=BACKGROUND_COLOR)
Canvas = Canvas(width=800, height=526)
logo = PhotoImage(file="./images/card_front.png")
Canvas.create_image(100, 100, image=logo)

window.mainloop()

