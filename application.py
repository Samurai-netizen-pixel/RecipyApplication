import tkinter as tk
from tkinter import ttk

from application_operations import ApplicationOperations
from edit_window import EditWindow
from file_handler import FileHandler
from ingredients_window import IngredientsWindow
from user import User


class Application:
    def __init__(self, file_name: str, main_window):
        self.__edit_window = None
        self.__ingredients_window = None
        self.__user = User()
        self.__file_handler = FileHandler(file_name)
        self.__main_window = main_window
        self.__application_operations = ApplicationOperations(self.__user)

        self.__main_window.title("Recipies")

        self.__add_ingredients = ttk.Button(self.__main_window, text="Add Ingredients",
                                            command=self.make_ingredients_window)
        self.__add_ingredients.grid(row=1, column=1, padx=5, pady=5)

        self.__description_label = ttk.Label(self.__main_window, text="Enter Description:")
        self.__description_label.grid(row=2, column=0, padx=5, pady=5)

        self.__description_info = ttk.Entry(self.__main_window, width=30)
        self.__description_info.grid(row=2, column=1, padx=5, pady=5)

        self.__add_button = ttk.Button(self.__main_window, text="Add Recipy", command=self.add_recipy)
        self.__add_button.grid(row=3, column=1)

        self.__edit_button = ttk.Button(self.__main_window, text="Edit Recipy", command=self.make_edit_window)
        self.__edit_button.grid(row=4, column=1)

        self.__save_button = ttk.Button(self.__main_window, text="Save", command=self.save)
        self.__save_button.grid(row=5, column=1)

        self.__delete_button = ttk.Button(self.__main_window, text="Delete", command=self.delete_recipy)
        self.__delete_button.grid(row=6, column=1)

        self.__recipies = tk.Listbox(self.__main_window, width=40)
        self.__recipies.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def make_ingredients_window(self):
        root = tk.Toplevel()
        self.__ingredients_window = IngredientsWindow(root, self.__user)
        root.mainloop()

    def add_recipy(self):
        ingredients_list = []
        ingredients = self.__ingredients_window.get_ingredients()

        for ingredient in ingredients:
            ingredient = self.__user.create_ingredient(ingredient)
            ingredients_list.append(ingredient)

        description = self.__description_info.get()

        if ingredients is not None and description is not None:
            self.__user.create_recipy(ingredients_list, description)
            self.update_listbox()

        self.__description_info.delete(0, tk.END)
        print(self.__user.get_recipies())

    def delete_recipy(self):
        selected_recipy = self.__recipies.curselection()
        if selected_recipy:
            selected_index = self.__application_operations.get_selected_index(selected_recipy)
            self.__user.remove_recipy(selected_index)
            self.update_listbox()
            print(self.__user.get_recipies())

    def make_edit_window(self):
        selected_recipy_index = self.__recipies.curselection()

        if selected_recipy_index:
            selected_recipy_info = self.get_info_for_editing(selected_recipy_index)
            root = tk.Tk()
            self.__edit_window = EditWindow(root, selected_recipy_info, self.__user, selected_recipy_index)
            root.mainloop()

    def save(self):
        recipies = self.__user.get_recipies_info()
        self.__file_handler.write_recipies(recipies)

    def insert_recipies_from_file(self):
        try:
            main_splitter = '\n'
            first_splitter = '['
            second_splitter = ']'
            third_splitter = ': '
            recipies_info = self.__file_handler.read_recipies()

            if recipies_info:
                recipies_list_info = recipies_info.split(main_splitter)

                for recipy_info in recipies_list_info:
                    first_splitter_index = recipy_info.find(first_splitter)
                    second_splitter_index = recipy_info.find(second_splitter)
                    third_splitter_index = recipy_info.rfind(third_splitter)

                    ingredients_info_list = recipy_info[first_splitter_index + 1: second_splitter_index].strip().split(
                        ', ')
                    description = recipy_info[third_splitter_index + 2:]
                    ingredients = []

                    for ingredient_info in ingredients_info_list:
                        ingredient = self.__user.create_ingredient(ingredient_info)
                        ingredients.append(ingredient)

                    recipy = self.__user.create_recipy(ingredients, description)
                    self.__recipies.insert(tk.END, recipy)
        except:
            print(0)

    def get_info_for_editing(self, selected_recipy_index):
        selected_recipy_info = self.__application_operations.make_info_for_editing(selected_recipy_index)

        return selected_recipy_info

    def update_listbox(self):
        self.__recipies.delete(0, tk.END)
        for recipy in self.__user.get_recipies_info():
            self.__recipies.insert(tk.END, recipy)
