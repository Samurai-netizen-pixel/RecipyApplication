import tkinter as tk
from tkinter import ttk

from file_handler import FileHandler
from ingredients_window import IngredientsWindow
from user import User


class Application:
    def __init__(self, file_name: str, main_window):
        self.__ingredients_window = None
        self.__user = User()
        self.__file_handler = FileHandler(file_name)
        self.__main_window = main_window

        self.__main_window.title("Recipies")

        self.__add_ingredients = ttk.Button(self.__main_window, text="Add Ingredients",
                                            command=self.enter_ingredients)
        self.__add_ingredients.grid(row=1, column=1, padx=5, pady=5)

        self.__description_label = ttk.Label(self.__main_window, text="Enter Description:")
        self.__description_label.grid(row=2, column=0, padx=5, pady=5)

        self.__description_info = ttk.Entry(self.__main_window, width=30)
        self.__description_info.grid(row=2, column=1, padx=5, pady=5)

        self.__add_button = ttk.Button(self.__main_window, text="Add Recipy", command=self.add_recipy)
        self.__add_button.grid(row=3, column=1)

        self.__save_button = ttk.Button(self.__main_window, text="Save", command=self.save)
        self.__save_button.grid(row=4, column=1)

        self.__delete_button = ttk.Button(self.__main_window, text="Delete", command=self.delete_recipy)
        self.__delete_button.grid(row=5, column=1)

        self.__recipies = tk.Listbox(self.__main_window, width=40)
        self.__recipies.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def enter_ingredients(self):
        root = tk.Toplevel()
        self.__ingredients_window = IngredientsWindow(root)
        root.mainloop()

    def add_recipy(self):
        ingredients = self.__ingredients_window.get_ingredients()
        description = self.__description_info.get()

        if ingredients is not None and description is not None:
            recipy = self.__user.create_recipy(ingredients, description)
            self.__recipies.insert(tk.END, recipy.__repr__())

        self.__description_info.delete(0, tk.END)
        print(self.__user.get_recipies())

    def delete_recipy(self):
        selected_recipy = self.__recipies.curselection()
        if selected_recipy:
            self.__recipies.delete(selected_recipy)
            selected_info = map(str, selected_recipy)
            selected_index_info = ''.join(selected_info)
            selected_index = int(selected_index_info)
            self.__user.remove_recipy(selected_index)
            print(self.__user.get_recipies())

    def save(self):
        recipies = self.__user.get_recipies_info()
        self.__file_handler.write(recipies)

    def try_get_info_from_file(self):
        try:
            main_splitter = '\n'
            first_splitter = ': '
            second_splitter = ';'
            recipies_info = self.__file_handler.read()
            recipies_list_info = recipies_info.split(main_splitter)

            for recipy_info in recipies_list_info:
                first_splitter_index = recipy_info.find(first_splitter)
                second_splitter_index = recipy_info.find(second_splitter)
                third_splitter_index = recipy_info.rfind(first_splitter)

                ingredients_info = list(
                    recipy_info[first_splitter_index + 1: second_splitter_index].strip())
                description = recipy_info[third_splitter_index + 1:]
                recipy = self.__user.create_recipy(ingredients_info, description)
                self.__recipies.insert(tk.END, recipy.__repr__())

        except:
            return ''
