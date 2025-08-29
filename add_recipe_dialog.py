import tkinter as tk
from tkinter import simpledialog, ttk, messagebox


class AddRecipeDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.__parent = parent
        self.__result = None
        super().__init__(parent, title)

    def body(self, master):
        self.__recipe_name_var = tk.StringVar()
        self.__ingredients_var = tk.StringVar()
        self.__instructions_var = tk.StringVar()

        ttk.Label(master, text="Recipe Name:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.__name_entry = ttk.Entry(master, textvariable=self.__recipe_name_var, width=40)
        self.__name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(master, text="Ingredients (e.g., Egg:2, Milk:1 cup):").grid(row=1, column=0, sticky=tk.W, padx=5,
                                                                              pady=5)
        self.__ingredients_entry = ttk.Entry(master, textvariable=self.__ingredients_var, width=40)
        self.__ingredients_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(master, text="Instructions:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.__instructions_text = tk.Text(master, height=5, width=40, wrap=tk.WORD)
        self.__instructions_text.grid(row=2, column=1, padx=5, pady=5)

    def apply(self):
        recipe_name = self.__recipe_name_var.get().strip()
        ingredients_str = self.__ingredients_var.get().strip()
        instructions = self.__instructions_text.get("1.0", tk.END).strip()

        if not recipe_name or not ingredients_str or not instructions:
            messagebox.showerror("Input Error", "Please fill in all fields.", parent=self)
            return

        self.__result = f"{recipe_name}::{ingredients_str}::{instructions}"

    def get_result(self):
        return self.__result
