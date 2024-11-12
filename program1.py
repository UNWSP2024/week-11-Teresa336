# Programmer: Teresa Fischer
# Date: 11/15/24
# Program # 1

import tkinter

class MyGUI:
    def __init__(self):
        # Creates main window widget
        self.main_window = tkinter.Tk()
        # Displays title
        self.main_window.title('Teresa\'s GUI')
        # Create and pack label
        self.label = tkinter.Label(self.main_window, text = '\" Not all of us can do great things. \n But we can do small things with great love.\" \n -Mother Teresa', borderwidth=2,relief='ridge')
        self.label.pack()

        # Enters the tkinter main loop
        tkinter.mainloop()

# Creates an instance of MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()