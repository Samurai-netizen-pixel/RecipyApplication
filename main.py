from application import Application

application = Application('Recipies.txt')

application.try_get_info_from_file()
application.run()
