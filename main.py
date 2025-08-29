from recipe_book_view import RecipeBookView
from recipe_book_viewmodel import RecipeBookViewModel


def main():
    viewmodel = RecipeBookViewModel()
    view = RecipeBookView(viewmodel)
    view.mainloop()


if __name__ == "__main__":
    main()
