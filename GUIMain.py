import tkinter

class minecraftCommandWindow():
    def __init__(self):
        top = tkinter.Tk()
        top.winfo_toplevel().title("Minecraft Command Generator")
        top.mainloop()

thisWindow = minecraftCommandWindow()