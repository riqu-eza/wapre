from ..Database.Model import UploadData
from toga import App, Box, Label, Button, DateInput,TextInput
from toga.style import Pack
from .Upload_utils import get_geolocation
import asyncio  # Import asyncio for awaiting
from toga.constants import COLUMN, ROW
from ..Camera.camera import capture_image



async def show_upload_view(app, user):
    # Debugging: print the user object to see its structure
    print("User object:", user)  # Debug line to check user data structure

    # Safely access user data
    user_email = user.get('email', 'noemail@example.com')  # Default value for email

    # Get user's geolocation
    location = await get_geolocation()  # Fetch geolocation asynchronously

    # Create UI components for the upload form
    email_label = Label(text=f"Email: {user_email}", style=Pack(padding=10, font_size=16))

    # Create the DateInput for user to select date
    date_input = TextInput(placeholder="YYYY-MM-DD", style=Pack(padding=10, font_size=16))

    image_path = None

    async def perform_capture(widget):
        nonlocal image_path
        image_path = await capture_image(app)  # Capture image and store its path

    # Create the capture button for photo-taking
    capture_button = Button(text="Take Photo", on_press=perform_capture, style=Pack(padding=10, background_color="blue", color="white"))
    
    def perform_upload(widget):
        # Collect data from inputs
        date_of_purchase = date_input.value
        
        # Create a new UploadData entry
        upload_entry = UploadData(user=user, date_of_purchase=date_of_purchase, address=location ,  )
        
        # Save the entry and show a confirmation message
        upload_entry.save()
        app.main_window.info_dialog("Upload", "Data uploaded successfully!")
 
    # Create the upload button
    upload_button = Button(text="Submit Upload", on_press=perform_upload, style=Pack(padding=10, font_size=16, background_color="blue", color="white"))

    # Arrange UI components in a box layout
    content_box = Box(
        children=[
            Label(text="Upload Gadget Information", style=Pack(font_size=24, padding=(20, 0))),
            email_label,  # Use Label instead of TextInput
            date_input, 
            capture_button,# TextInput for date
            upload_button
        ],
        style=Pack(direction="column", alignment="center", padding=20, background_color="lightgray", width=300)  # Change to 'column'
    )

    # Set the main window content to the upload form
    app.main_window.content = content_box
