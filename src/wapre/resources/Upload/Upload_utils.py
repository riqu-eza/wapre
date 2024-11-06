from toga import App, Box, Label
import asyncio
import requests
from toga.style import Pack
from toga.constants import COLUMN
from plyer import gps  # Ensure plyer is installed in your environment

async def get_geolocation():
    """Fetch the current geolocation of the device."""
    try:
        await asyncio.sleep(1)  # Allow time to establish a GPS fix
        location = gps.get_location()  # Fetch the GPS location on supported platforms
        return {"latitude": location['lat'], "longitude": location['lon']}
    except (ModuleNotFoundError, AttributeError):
        print("GPS not available in development; using fallback location.")
        return {"latitude": 37.7749, "longitude": -122.4194}  # Example: San Francisco
    except Exception as e:
        print(f"Error getting geolocation: {e}")
        return None

def reverse_geocode(lat, lng):
    """Get the address based on latitude and longitude."""
    url = f'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lng}&format=json'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('display_name', 'Address not found')
    except Exception as e:
        print(f"Error during reverse geocoding: {e}")
    return 'Address not found'

async def show_location(app):
    """Display the latitude, longitude, and address on the app."""
    location = await get_geolocation()  # Get geolocation
    if location:
        lat = location['latitude']
        lng = location['longitude']
        address = reverse_geocode(lat, lng)  # Get address using reverse geocoding

        app.main_window.content = Box(
            children=[
                Label(text=f"Latitude: {lat}", style=Pack(padding=5)),
                Label(text=f"Longitude: {lng}", style=Pack(padding=5)),
                Label(text=f"Address: {address}", style=Pack(padding=5))
            ],
            style=Pack(direction=COLUMN, padding=20)
        )
    else:
        app.main_window.content = Box(
            children=[
                Label(text="Failed to retrieve location.", style=Pack(padding=5))
            ],
            style=Pack(direction=COLUMN, padding=20)
        )