# Programmer: Teresa Fischer
# Date: 11/15/24
# Program # 2

import tkinter

class InfoGUI:
    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()
        # creates the two frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # creates blank label for top frame
        self.value = tkinter.StringVar()
        self.address_label = tkinter.Label(self.top_frame, textvariable=self.value)
        # creates the two buttons for the bottom frame
        self.address_button = tkinter.Button(self.bottom_frame,
                                             text = 'Show info', command = self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text = 'Quit', command = self.main_window.destroy)

        # pack the label, buttons, and frames
        self.address_label.pack()
        self.address_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        self.top_frame.pack()
        self.bottom_frame.pack()

        # enter the mainloop
        tkinter.mainloop()

    def show_info(self):
        self.value.set('Teresa Fischer\n1115 Crestwood Lane\nNew Ulm, MN 56073')

# instance of infoGUI
show_info = InfoGUI()
