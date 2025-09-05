from recipe_book_view import RecipeBookView
from recipe_book_viewmodel import RecipeBookViewModel
from recipe_book_model import RecipeBookModel

def main():
    model = RecipeBookModel()
    viewmodel = RecipeBookViewModel(model)
    view = RecipeBookView(viewmodel)
    view.mainloop()


if __name__ == "__main__":
    main()
