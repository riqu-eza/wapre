from ..Database.Model import User
from toga import App, Box, Label, TextInput, Button
from toga.style import Pack
from toga.constants import COLUMN  # Add this line

def show_signup_view(app):
    def signup_user(widget):
        Firstname = Firstname_input.value
        Secondname = Secondname_input.value
        Email = email_input.value
        Password = password_input.value
        
        # Create the user
        User.create(Firstname, Secondname, Email, Password)
        app.main_window.info_dialog("Signup", "Signup successful")
        
        # Navigate back to the login view
        from ..Auth.Login import show_login_view
        show_login_view(app)

    # Create UI components
    Firstname_input = TextInput(placeholder="Firstname", style=Pack(padding=10, font_size=16))
    Secondname_input = TextInput(placeholder="Secondname", style=Pack(padding=10, font_size=16))
    email_input = TextInput(placeholder="email", style=Pack(padding=10, font_size=16))

    password_input = TextInput(placeholder="Password",  style=Pack(padding=10, font_size=16))
    signup_button = Button("Signup", on_press=signup_user, style=Pack(padding=10, font_size=16))

    # Arrange widgets in a box layout
    content_box = Box(
        children=[
            Label("Signup Page", style=Pack(font_size=24, padding=(20, 0))),
            Firstname_input,
            Secondname_input,
            email_input,
            password_input,
            signup_button
        ],
        style=Pack(direction=COLUMN, alignment="center", padding=20, background_color="white", width=300)
    )

    # Set the main window content
    app.main_window.content = content_box
