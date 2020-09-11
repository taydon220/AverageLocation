import webbrowser
import config
from center_geolocation import find_weighted_center, find_center


if __name__ == "__main__":
    coords = []
    for c, location in enumerate(config.my_locations, 1):
        print(f"Location #{c}:")
        location.print_info()
        coords.append(location.coords)
    center = find_center(coords)
    weighted_center = find_weighted_center(config.my_locations)
    print(f"Un-weighted center: {center}")
    print(f"Weighted center: {weighted_center}")
    print("")
    center_map = input("Would you like to see the maps? (Y)")
    if center_map.lower() == "y":
        webbrowser.open(f"https://www.google.com/maps/search/{center}")
        webbrowser.open(f"https://www.google.com/maps/search/{weighted_center}")

