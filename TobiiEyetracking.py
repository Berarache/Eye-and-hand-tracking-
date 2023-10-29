import tkinter as tk
from PIL import Image, ImageTk
from djitellopy import Tello

def scroll_start(event):
    print ('scroll ', event.x, event.y)
def scroll_move(event):
    if event.x >= 200 and event.x <= 450 and event.y >= 8 and event.y <= 120:
        print ('takeoff')
        command=action0()
    elif event.x >= 430 and event.x <= 620 and event.y >= 120 and event.y <= 270:
        print ('right')
        command=action4()
    elif event.x >= 16 and event.x <= 120 and event.y >= 150 and event.y <= 260:
        print ('left')
        command=action5()
    elif event.x >= 200 and event.x <= 360 and event.y >= 180 and event.y <= 420:
        print ('land')
        command= action14()
    else:
        print ('nada')

def action0():
    global tello
    tello = Tello()
    tello.connect()
    tello.takeoff()

def action4():
    global tello
    tello.move_right(50)

def action5():
    global tello
    tello.move_left(50)


def action14():
    global tello
    tello.land()





root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo')

image = Image.open("Imagen2.png")
image = image.resize((600, 400), Image.ANTIALIAS)

bg = ImageTk.PhotoImage(image)


canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.create_image(0, 0, image=bg, anchor="nw")

canvas.pack(anchor=tk.CENTER, expand=True)
canvas.bind("<ButtonPress-1>", scroll_start)
canvas.bind("<Motion>", scroll_move)
root.mainloop()
