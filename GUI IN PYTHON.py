import tkinter as tk

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("My GUI")
        
        self.label = tk.Label(master, text="Hello, World!")
        self.label.pack()
        
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

root = tk.Tk()
my_gui = MyGUI(root)
root.mainloop()
