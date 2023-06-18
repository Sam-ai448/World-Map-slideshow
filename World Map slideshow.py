import tkinter

pnum = 0

def photograph():
    global pnum
    canvas.delete("PH")
    canvas.create_image(600, 400, image=Picture[pnum], tag="PH")
    pnum = pnum + 1
    if pnum >= len(Picture):
        pnum = 0
    root.after(200, photograph)

root = tkinter.Tk()
root.title("World Map Slideshow")
root.configure(bg="black")  # Set the background color of the window

canvas = tkinter.Canvas(root, width=1024, height=768, bg="blue")  # Set the background color of the canvas
canvas.pack()

Picture = [
    tkinter.PhotoImage(file="亞洲.png"),
    tkinter.PhotoImage(file="歐洲.png"),
    tkinter.PhotoImage(file="非洲.png"),
    tkinter.PhotoImage(file="美洲.png"),
    tkinter.PhotoImage(file="大洋洲.png"),
    tkinter.PhotoImage(file="南極洲.png")
]

photograph()
root.mainloop()