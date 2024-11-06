from plyer import camera  # Use plyer's camera
import os
import time

def open_camera():
    # Specify the directory to save the image
    image_dir = "captured_images"
    os.makedirs(image_dir, exist_ok=True)
    
    # Generate a unique filename for the image
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    image_path = os.path.join(image_dir, f"image_{timestamp}.jpg")

    # Open the camera and capture the image
    print("Opening camera...")
    camera.capture(image_path)  # This will open the camera and save the image

    print(f"Image captured and saved at {image_path}.")
    return image_path  # Return the path of the saved image
