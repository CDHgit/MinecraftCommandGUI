import tkinter
import os
import logging
class minecraftCommandWindow():
    def __init__(self):
        self.top = tkinter.Tk()
        #Window Specifics (Title, Icon, Size)
        self.top.winfo_toplevel().title("Minecraft Command Generator")
        path = os.getcwd()
        icon_path = path + '\commandguiicon.ico'
        logging.debug(icon_path)
        self.top.iconbitmap(icon_path)
        self.top.geometry("1000x500")
        #Find all icons for pictures used in the app
        self.item_icons = {}
        # self.item_icons['d_sword'] = PhotoImage(file="item_icons/diamondsword.png")
        # self.item_icons['i_sword'] = PhotoImage(file="item_icons/ironsword.png")
        # self.item_icons['s_sword'] = PhotoImage(file="item_icons/stonesword.png")
        # self.item_icons['w_sword'] = PhotoImage(file="item_icons/woodsword.png")
        # self.item_icons['d_shovel'] = PhotoImage(file="item_icons/diamondshovel.png")
        # self.item_icons['i_shovel'] = PhotoImage(file="item_icons/ironshovel.png")
        # self.item_icons['s_shovel'] = PhotoImage(file="item_icons/stoneshovel.png")
        # self.item_icons['w_shovel'] = PhotoImage(file="item_icons/woodshovel.png")
        # self.item_icons['d_pick'] = PhotoImage(file="item_icons/diamondpick.png")
        # self.item_icons['i_pick'] = PhotoImage(file="item_icons/ironpick.png")
        # self.item_icons['s_pick'] = PhotoImage(file="item_icons/stonepick.png")
        # self.item_icons['w_pick'] = PhotoImage(file="item_icons/woodpick.png")
        # self.item_icons['d_hoe'] = PhotoImage(file="item_icons/diamondhoe.png")
        # self.item_icons['i_hoe'] = PhotoImage(file="item_icons/ironhoe.png")
        # self.item_icons['s_hoe'] = PhotoImage(file="item_icons/stonehoe.png")
        # self.item_icons['w_hoe'] = PhotoImage(file="item_icons/woodhoe.png")
        # self.item_icons['d_axe'] = PhotoImage(file="item_icons/diamondaxe.png")
        # self.item_icons['i_axe'] = PhotoImage(file="item_icons/ironaxe.png")
        # self.item_icons['s_axe'] = PhotoImage(file="item_icons/stoneaxe.png")
        # self.item_icons['w_axe'] = PhotoImage(file="item_icons/woodaxe.png")




        choiceFrame = tkinter.Frame(self.top)
        choiceFrame.grid(column=0, row=0)#sticky=('N', 'W', 'E', 'S'))
        choiceFrame.columnconfigure(0, weight=1)
        choiceFrame.rowconfigure(0, weight=1)
        choiceFrame.pack(pady=100, padx=100)
        choices = {"Give", "Enchant", "Teleport"}
        choiceString = tkinter.StringVar(self.top)
        choiceString.set("Give")
        choiceMenu = tkinter.OptionMenu(choiceFrame, choiceString, *choices)
        tkinter.Label(choiceFrame, text="Choose a command").grid(row=1, column=1)
        choiceMenu.grid(row=2, column=1)

        # resultFrame = tkinter.Frame(self.top)
        # resultFrame.grid(column=0, row=0)  # sticky=('N', 'W', 'E', 'S'))
        # resultFrame.columnconfigure(0, weight=1)
        # resultFrame.rowconfigure(0, weight=1)
        # resultFrame.pack(pady=100, padx=100)

        self.top.mainloop()
#    def displayItems(self):




thisWindow = minecraftCommandWindow()