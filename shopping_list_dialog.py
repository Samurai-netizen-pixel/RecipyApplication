import tkinter as tk
from tkinter import ttk, messagebox

from recipe_book_viewmodel import RecipeBookViewModel


class ShoppingListDialog(tk.Toplevel):
    def __init__(self, parent, viewmodel: RecipeBookViewModel):
        super().__init__(parent)
        self.__viewmodel = viewmodel
        self.__parent = parent
        self.title("Generate Shopping List")
        self.geometry("450x450")
        self.transient(parent)

        self.__selected_recipes = []

        self._setup_ui()
        self.populate_recipe_selection()

    def _setup_ui(self):
        selection_frame = ttk.Frame(self, padding="10")
        selection_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(selection_frame, text="Select recipes for your shopping list:", font=("Arial", 11, "bold")).pack(
            anchor=tk.NW)

        self.__recipe_selection_listbox = tk.Listbox(selection_frame, selectmode=tk.MULTIPLE, height=10,
                                                     font=("Arial", 10))
        self.__recipe_selection_listbox.pack(fill=tk.BOTH, expand=True, pady=5)

        list_scrollbar = ttk.Scrollbar(selection_frame, orient=tk.VERTICAL,
                                       command=self.__recipe_selection_listbox.yview)
        self.__recipe_selection_listbox.config(yscrollcommand=list_scrollbar.set)
        list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        button_frame = ttk.Frame(self, padding="10")
        button_frame.pack(fill=tk.X)

        generate_button = ttk.Button(button_frame, text="Generate List", command=self.generate_and_display_list)
        generate_button.pack(side=tk.LEFT, padx=5)

        close_button = ttk.Button(button_frame, text="Close", command=self.destroy)
        close_button.pack(side=tk.RIGHT, padx=5)

    def populate_recipe_selection(self):
        for vm in self.__viewmodel.get_current_view_recipes():
            self.__recipe_selection_listbox.insert(tk.END, vm.display_name)

    def generate_and_display_list(self):
        selected_indices = self.__recipe_selection_listbox.curselection()
        self.__selected_recipes = [
            self.__viewmodel.get_current_view_recipes()[index].display_name

            for index in selected_indices
        ]

        if not self.__selected_recipes:
            messagebox.showwarning("No Selection", "Please select at least one recipe.", parent=self)
            return

        shopping_list_text = self.__viewmodel.generate_shopping_list(self.__selected_recipes)
        messagebox.showinfo("Shopping List", shopping_list_text, parent=self)
