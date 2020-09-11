import webbrowser
from config import my_locations
from center_geolocation import find_weighted_center, find_center


if __name__ == "__main__":
    coords = []
    for location in my_locations:
        coords.append(location.coords)
    center = find_center(coords)
    weighted_center = find_weighted_center(my_locations)
    print(f"Your un-weighted center coordinates are: {center}")
    print(f"Your weighted center coordinates are: {weighted_center}")
    webbrowser.open(f"https://www.google.com/maps/search/{center}")
    webbrowser.open(f"https://www.google.com/maps/search/{weighted_center}")
