import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

from add_recipe_dialog import AddRecipeDialog
from recipe import Ingredient, Recipe
from recipe_book_viewmodel import RecipeBookViewModel, RecipeViewModel
from shopping_list_dialog import ShoppingListDialog


class RecipeBookView(tk.Tk):
    def __init__(self, viewmodel: RecipeBookViewModel):
        super().__init__()
        self.__viewmodel = viewmodel
        self.title("Recipe Book")
        self.geometry("800x600")

        self._setup_ui()
        self.load_initial_data()

    def _setup_ui(self):
        control_frame = ttk.Frame(self, padding="10")
        control_frame.pack(side=tk.TOP, fill=tk.X)

        list_frame = ttk.Frame(self, padding="10")
        list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        details_frame = ttk.Frame(self, padding="10")
        details_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Add New Recipe", command=self.open_add_recipe_dialog)
        file_menu.add_command(label="Generate Shopping List", command=self.open_shopping_list_dialog)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        ttk.Label(control_frame, text="Search by Ingredient:").pack(side=tk.LEFT, padx=(0, 5))
        self.__search_entry = ttk.Entry(control_frame, width=30)
        self.__search_entry.pack(side=tk.LEFT, padx=5)
        self.__search_entry.bind("<KeyRelease>", self.handle_search_key_release)

        ttk.Label(list_frame, text="Recipes:", font=("Arial", 12, "bold")).pack(anchor=tk.NW)

        self.__recipe_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, font=("Arial", 11))
        self.__recipe_listbox.pack(fill=tk.BOTH, expand=True)
        self.__recipe_listbox.bind("<<ListboxSelect>>", self.handle_recipe_selection)

        list_scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.__recipe_listbox.yview)
        self.__recipe_listbox.config(yscrollcommand=list_scrollbar.set)
        list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        ttk.Label(details_frame, text="Recipe Details:", font=("Arial", 12, "bold")).pack(anchor=tk.NW)
        self.__recipe_details_text = scrolledtext.ScrolledText(details_frame, wrap=tk.WORD, state=tk.DISABLED,
                                                               font=("Arial", 10))
        self.__recipe_details_text.pack(fill=tk.BOTH, expand=True)

    def load_initial_data(self):
        self.__viewmodel.load_initial_data()
        self.update_recipe_listbox()

    def update_recipe_listbox(self):
        self.__recipe_listbox.delete(0, tk.END)

        if self.__viewmodel.get_current_view_recipes():

            for vm in self.__viewmodel.get_current_view_recipes():
                self.__recipe_listbox.insert(tk.END, vm.display_name)

        else:
            self.__recipe_listbox.insert(tk.END, "No recipes available.")

        self.clear_recipe_details()

    def clear_recipe_details(self):
        self.__recipe_details_text.config(state=tk.NORMAL)
        self.__recipe_details_text.delete("1.0", tk.END)
        self.__recipe_details_text.config(state=tk.DISABLED)

    def display_recipe_details(self, recipe_vm: RecipeViewModel):
        if recipe_vm:
            details_str = f"Name: {recipe_vm.display_name}\n\n"
            details_str += f"Ingredients:\n {recipe_vm.display_ingredients}\n\n"
            details_str += f"Instructions:\n{recipe_vm.display_instructions}"

            self.__recipe_details_text.config(state=tk.NORMAL)
            self.__recipe_details_text.delete("1.0", tk.END)
            self.__recipe_details_text.insert(tk.END, details_str)
            self.__recipe_details_text.config(state=tk.DISABLED)
        else:
            self.clear_recipe_details()

    def handle_recipe_selection(self, event):
        if event:
            selected_indices = self.__recipe_listbox.curselection()
            if not selected_indices:
                return

            selected_index = selected_indices[0]

            if len(self.__viewmodel.get_current_view_recipes()):
                selected_vm = self.__viewmodel.get_current_view_recipes()[selected_index]
                self.display_recipe_details(selected_vm)
            else:
                self.clear_recipe_details()

    def handle_search_key_release(self, event):
        if event:
            search_term = self.__search_entry.get()
            self.__viewmodel.search_by_ingredient(search_term)
            self.update_recipe_listbox()

    def open_add_recipe_dialog(self):
        dialog = AddRecipeDialog(self, title="Добавление рецепта")
        new_recipe_data = dialog.get_result()

        if new_recipe_data:
            try:
                recipe_name, ingredients_str, instructions = new_recipe_data.split("::")

                ingredients_list = []

                for ing_pair in ingredients_str.split(","):

                    if ":" in ing_pair:
                        ing_name, ing_qty = ing_pair.split(":", 1)
                        ingredients_list.append(Ingredient(ing_name.strip(), ing_qty.strip()))
                    elif ing_pair.strip():
                        ingredients_list.append(Ingredient(ing_pair.strip(), ""))

                if not recipe_name or not instructions or not ingredients_list:
                    messagebox.showerror("Error",
                                         "Invalid recipe data. Ensure all fields are provided and ingredients are formatted correctly.")
                    return

                new_recipe = Recipe(recipe_name.strip(), ingredients_list, instructions.strip())
                self.__viewmodel.add_recipe(new_recipe)
                self.update_recipe_listbox()  # Update list after adding
                messagebox.showinfo("Success", f"Recipe '{recipe_name.strip()}' added!")

            except ValueError:
                messagebox.showerror("Error", "Invalid format. Use 'Name::Ing1:Qty1,Ing2:Qty2::Instructions'")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def open_shopping_list_dialog(self):
        ShoppingListDialog(self, self.__viewmodel)
