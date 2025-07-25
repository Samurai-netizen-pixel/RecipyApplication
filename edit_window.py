from tkinter import ttk, Tk

from recipy_creator import RecipyCreator
from user import User


class EditWindow:
    def __init__(self, edit_window: Tk, selected_recipy: str, user: User, selected_recipy_index: tuple):
        self.__edit_window = edit_window
        self.__selected_recipy = selected_recipy
        self.__user = user
        self.__recipy_creator = RecipyCreator()
        self.__selected_recipy_index = selected_recipy_index

        self.__edit_label = ttk.Label(self.__edit_window, text="Edit Recipy:")
        self.__edit_label.grid(row=1, column=1, padx=5, pady=5)

        self.__edit_entry = ttk.Entry(self.__edit_window, width=30)
        self.__edit_entry.grid(row=2, column=1, padx=5, pady=5)
        self.__edit_entry.insert(0, self.__selected_recipy)

        self.__ok_button = ttk.Button(self.__edit_window, text='OK', command=self.confirm_editing)
        self.__ok_button.grid(row=3, column=1, padx=5, pady=5)

    def confirm_editing(self):
        new_recipy = self.__edit_entry.get()
        new_recipy = new_recipy.split(';')
        ingredients = new_recipy[0].split(', ')
        description = new_recipy[1]

        selected_info = map(str, self.__selected_recipy_index)
        selected_index_info = ''.join(selected_info)
        selected_index = int(selected_index_info)

        recipies = self.__user.get_recipies()
        recipy = self.__recipy_creator.create(ingredients, description)
        recipies.pop(selected_index)
        recipies.append(recipy)
        self.__edit_window.destroy()
