import tkinter as tk
from tkinter import ttk


class IngredientsWindow:
    def __init__(self, ingredients_window):
        self.__ingredients_window = ingredients_window

        self.__ingredients_label = ttk.Label(self.__ingredients_window, text="Enter Ingredient:")
        self.__ingredients_label.grid(row=1, column=0, padx=5, pady=5)

        self.__ingredients_info_view = ttk.Entry(self.__ingredients_window, width=30)
        self.__ingredients_info_view.grid(row=1, column=1, padx=5, pady=5)

        self.__add_button = ttk.Button(self.__ingredients_window, text="Add Recipy", command=self.add_ingredient)
        self.__add_button.grid(row=3, column=1)

        self.__delete_button = ttk.Button(self.__ingredients_window, text="Delete", command=self.delete_ingredient)
        self.__delete_button.grid(row=5, column=1)

        self.__ingredients = tk.Listbox(self.__ingredients_window, width=40)
        self.__ingredients.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def add_ingredient(self):
        ingredient = self.__ingredients_info_view.get()
        self.__ingredients.insert(tk.END, ingredient)
        self.__ingredients_info_view.delete(0, tk.END)

    def delete_ingredient(self):
        selected_ingredient = self.__ingredients.curselection()
        if selected_ingredient:
            self.__ingredients.delete(selected_ingredient)

    def get_ingredients(self) -> list[str]:
        ingredients = self.__ingredients.get(0, tk.END)
        ingredients = list(ingredients)
        return ingredients
