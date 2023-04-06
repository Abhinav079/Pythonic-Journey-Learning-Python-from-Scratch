import tkinter as tk

# Create a new tkinter window
window = tk.Tk()

# Set the window title and size
window.title("Label Example")
window.geometry("400x300")

# Create a label with some text
label_text = tk.Label(window, text="Hello, world!")
label_text.pack()

# Create a label with an image
photo = tk.PhotoImage(file="example.png")
label_image = tk.Label(window, image=photo)
label_image.pack()

#
icon = tk.PhotoImage(file="example.png")
window.iconphoto(True,icon)
window.config(background="#5cfcff")

# Create a clickable label
def on_label_click(event):
    print("Label clicked!")
label_clickable = tk.Label(window, text="Click me!")
label_clickable.pack()
label_clickable.bind("<Button-1>", on_label_click)

# Update a label's contents dynamically
import time
def update_time():
    label_time.config(text=time.strftime("%H:%M:%S"))
    window.after(1000, update_time) # call this function again in 1 second
label_time = tk.Label(window, text="")
label_time.pack()
update_time() # start the timer

# Use labels for layout
label_spacer = tk.Label(window, text="", height=10)
label_spacer.pack()
label_separator = tk.Label(window, text="---------------")
label_separator.pack()

# Run the tkinter event loop
window.mainloop()
