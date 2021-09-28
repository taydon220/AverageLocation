import webbrowser
from config import my_locations
from geopy import distance
from center_geolocation import find_weighted_center, find_center


if __name__ == "__main__":
    coords = []
    for c, location in enumerate(my_locations, 1):
        print(f"Location #{c}:")
        location.print_info()
        coords.append(location.coords)
    center = find_center(coords)
    weighted_center = find_weighted_center(my_locations)
    distance = distance.distance(center, weighted_center).miles
    print(f"Un-weighted center: {center}")
    print(f"Weighted center: {weighted_center}")
    print(f"The distance between the two is ~{int(distance)} miles.")
    print("")
    center_map = input("Would you like to see the maps? ")
    if center_map.lower() == "y":
        webbrowser.open(f"https://www.google.com/maps/search/{center}")
        webbrowser.open(f"https://www.google.com/maps/search/{weighted_center}")

