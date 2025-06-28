import tkinter as tk
from tkinter import ttk

from application_view import ApplicationView
from file_handler import FileHandler
from user import User


class Application:
    def __init__(self, file_name: str, main_window):
        self.__user = User()
        self.__file_handler = FileHandler(file_name)
        self.__application_view = ApplicationView()
        self.__main_window = main_window

        main_window.title("To-Do List")

        self.__id_label = ttk.Label(main_window, text="Enter Recipy ID:")
        self.__id_label.grid(row=0, column=0, padx=5, pady=5)

        self.__recipy_id_info = ttk.Entry(main_window, width=30)
        self.__recipy_id_info.grid(row=0, column=1, padx=5, pady=5)

        self.__ingredients_label = ttk.Label(main_window, text="Enter Ingredients:")
        self.__ingredients_label.grid(row=1, column=0, padx=5, pady=5)

        self.__ingredients_info_view = ttk.Entry(main_window, width=30)
        self.__ingredients_info_view.grid(row=1, column=1, padx=5, pady=5)

        self.__description_label = ttk.Label(main_window, text="Enter Description:")
        self.__description_label.grid(row=2, column=0, padx=5, pady=5)

        self.__description_info = ttk.Entry(main_window, width=30)
        self.__description_info.grid(row=2, column=1, padx=5, pady=5)

        self.__add_button = ttk.Button(main_window, text="Add Recipy", command=self.add_recipy)
        self.__add_button.grid(row=3, column=1)

        self.__save_button = ttk.Button(main_window, text="Save", command=self.save)
        self.__save_button.grid(row=4, column=1)

        self.__delete_button = ttk.Button(main_window, text="Delete", command=self.delete_recipy)
        self.__delete_button.grid(row=5, column=1)

        self.__recipies = tk.Listbox(main_window, width=40)
        self.__recipies.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def add_recipy(self):
        self.__recipy_id = self.__recipy_id_info.get()
        self.__ingredients = self.__ingredients_info_view.get()
        self.__description = self.__description_info.get()
        self.__ingredients = self.__ingredients.split(',')

        if self.__recipy_id != '' and self.__ingredients != '' and self.__description != '':
            recipy = self.__user.create_recipy(self.__ingredients, self.__recipy_id, self.__description)
            self.__recipies.insert(tk.END, recipy.__repr__())

        self.__recipy_id_info.delete(0, tk.END)
        self.__ingredients_info_view.delete(0, tk.END)
        self.__description_info.delete(0, tk.END)

    def delete_recipy(self):
        selected = self.__recipies.curselection()
        if selected:
            self.__recipies.delete(selected)
            print(selected)

    def save(self):
        recipies = self.__user.get_recipies_info()
        self.__file_handler.write(recipies)

    def t(self):
        try:
            self.__recipies_info = self.__file_handler.read()
            self.__recipies_list_info = self.__recipies_info.split('\n')

            for recipy_info in self.__recipies_list_info:
                self.__first_splitter_index = recipy_info.find(': ')
                self.__second_splitter_index = recipy_info.find(';')
                self.__third_splitter_index = recipy_info.find('ID: ')
                self.__fourth_splitter_index = recipy_info.rfind(';')
                self.__fifth_splitter_index = recipy_info.rfind(': ')

                self.__ingredients_info = list(
                    recipy_info[self.__first_splitter_index + 1: self.__second_splitter_index].strip())
                self.__id_info = recipy_info[self.__third_splitter_index + 4: self.__fourth_splitter_index].strip()
                self.__description = recipy_info[self.__fifth_splitter_index + 2:]
                recipy = self.__user.create_recipy(self.__ingredients_info, self.__id_info, self.__description)
                self.__recipies.insert(tk.END, recipy.__repr__())

        except:
            return ''
