from user import User


class ApplicationOperations:
    def __init__(self, user: User):
        self.__user = user

    def make_info_for_editing(self, selected_recipy_index):
        selected_recipy_index = self.get_selected_index(selected_recipy_index)
        selected_recipy = self.__user.get_recipies()[selected_recipy_index]
        selected_recipy = selected_recipy.__repr__()

        first_splitter = ': '
        second_splitter = ';'
        first_splitter_index = selected_recipy.find(first_splitter)
        second_splitter_index = selected_recipy.find(second_splitter)
        third_splitter_index = selected_recipy.rfind(first_splitter)

        ingredients_info = selected_recipy[first_splitter_index + 1: second_splitter_index].strip()
        description = selected_recipy[third_splitter_index + 1:]
        selected_recipy_info = ingredients_info + ';' + description

        return selected_recipy_info

    def get_selected_index(self, selected_recipy: tuple):
        selected_recipy_info = map(str, selected_recipy)
        selected_recipy_index_info = ''.join(selected_recipy_info)
        selected_recipy_index = int(selected_recipy_index_info)
        return selected_recipy_index
