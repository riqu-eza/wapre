from toga import App, Box, Button, Label, MainWindow
from toga.style import Pack
from toga.constants import COLUMN, ROW
from .resources.Database.Db import init_db
from .resources.Auth.Login import show_login_view

class MyApp(App):
    def startup(self):
        # Initialize the database
        init_db()

        # Create the main window
        self.main_window = MainWindow(title="MyApp")  # Create a new MainWindow instance
        self.main_window.show()  # Show the main window

        # Load the login page as the first view
        show_login_view(self)

def main():
    return MyApp("MyApp", "com.example.myapp")

if __name__ == '__main__':
    main().main_loop()
