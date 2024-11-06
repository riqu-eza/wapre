from toga import Button, Box, App, Label
from toga.style import Pack
from .Camera_utils import open_camera

def capture_image(app):
    def take_photo(widget):
        # Open the camera and capture a photo
        image_path = open_camera()
        if image_path:
            app.main_window.info_dialog("Photo", "Photo captured!")  # Show a message when the photo is captured
            
            # Here, you can store the image_path in your database and get its URL
            store_image_in_database(image_path)  # Implement this function to handle database storage

    # Create the capture button
    capture_button = Button(text="Take Photo", on_press=take_photo, style=Pack(padding=10))
    
    # Wrap the capture_button in a Box
    capture_box = Box(children=[capture_button], style=Pack(direction="column", padding=20))

    # Set the content of the main window to the capture box
    app.main_window.content = capture_box

def store_image_in_database(image_path):
    # Implement your database logic here to save the image path and other related data
    # You can generate a URL based on where you're hosting the images
    image_url = f"http://your-server/{image_path}"  # Adjust the URL format as needed
    print(f"Storing image URL in the database: {image_url}")
    # Your database logic goes here
