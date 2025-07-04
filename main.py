import tkinter as tk

from application import Application

root = tk.Tk()
app = Application('Recipies.txt', root)
app.try_get_info_from_file()
root.mainloop()
