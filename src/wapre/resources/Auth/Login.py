from ..Database.Model import User
from toga import App, Box, Label, TextInput, Button
from toga.style import Pack
from toga.constants import COLUMN, ROW
from ..Upload.Upload import show_upload_view

def show_login_view(app):
    # Define the login logic
    async def login_user(widget):
        email = email_input.value
        password = password_input.value

        # Authentication logic here
        user = User.authenticate(email, password)
        if user:
            app.main_window.info_dialog("Login", "Login successful")
            await show_upload_view(app, user)
        else:
            app.main_window.info_dialog("Login", "Login failed")

    # Navigate to the signup view
    def go_to_signup(widget):
        from ..Auth.Signup import show_signup_view
        show_signup_view(app)

    # Create UI components with styling
    email_input = TextInput(placeholder="Username", style=Pack(padding=10, font_size=16))
    password_input = TextInput(placeholder="Password",  style=Pack(padding=10, font_size=16))
    login_button = Button("Login", on_press=login_user, style=Pack(padding=10, font_size=16, background_color="blue", color="white"))
    signup_button = Button("Don't have an account? Sign up here", on_press=go_to_signup, style=Pack(padding=10, font_size=12, color="blue", background_color="lightgray"))

    # Arrange widgets in a box layout
    content_box = Box(
        children=[
            Label("Login Page", style=Pack(font_size=24, padding=(20, 0))),
            email_input,
            password_input,
            login_button,
            signup_button
        ],
        style=Pack(direction=COLUMN, alignment="center", padding=20, background_color="white", width=300)
    )

    # Set the main window content
    app.main_window.content = content_box
