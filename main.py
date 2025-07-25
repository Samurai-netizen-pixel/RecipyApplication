import tkinter as tk

from application import Application

root = tk.Tk()
app = Application('Recipies.txt', root)
app.insert_recipies_from_file()
root.mainloop()
