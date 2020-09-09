import math
import webbrowser


class Location:
    def __init__(self, name, lat, lon, weight=None):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.weight = weight
        if weight is not None:
            self.weightedlat = lat * weight
            self.weightedlon = lon * weight


def find_center(locations):
    """
    :param locations: [(lat1,lon1),(lat2, lon2)] list of pairs of coordinates in degrees form.
    :return: (center_lat, center_lon) pair of decimal coordinates.
    """
    x = 0
    y = 0
    z = 0

    for lat, lon in locations:
        lat = math.radians(float(lat))
        lon = math.radians(float(lon))
        x += math.cos(lat) * math.cos(lon)
        y += math.cos(lat) * math.sin(lon)
        z += math.sin(lat)

    x = x / len(locations)
    y = y / len(locations)
    z = z / len(locations)

    center_lon = math.atan2(y, x)
    center_sq_root = math.sqrt(x * x + y * y)
    center_lat = math.atan2(z, center_sq_root)

    return math.degrees(center_lat), math.degrees(center_lon)


def find_weighted_center(locations):
    weights = []
    lat_lon_coords = []
    for location in locations:
        weights.append(location.weight)
        lat_lon_coords.append((math.radians(location.lat), math.radians(location.lon)))
    total_weight = sum(weights)
    cartesian_coords = []
    for pair in lat_lon_coords:
        x = 0
        y = 0
        z = 0
        x += math.cos(pair[0]) * math.cos(pair[1])
        y += math.cos(pair[0]) * math.sin(pair[1])
        z += math.sin(pair[0])
        cartesian_coords.append((x,y,z))
    total_x = 0
    total_y = 0
    total_z = 0
    for i in range(len(cartesian_coords)):
        total_x += cartesian_coords[i][0] * weights[i]
        total_y += cartesian_coords[i][1] * weights[i]
        total_z += cartesian_coords[i][2] * weights[i]
    average_x = total_x/total_weight
    average_y = total_y/total_weight
    average_z = total_z/total_weight
    center_lon = math.atan2(average_y, average_x)
    center_sq_root = math.sqrt(average_x * average_x + average_y * average_y)
    center_lat = math.atan2(average_z, center_sq_root)

    return math.degrees(center_lat), math.degrees(center_lon)


if __name__ == "__main__":
    my_locations = []  # List of Location class objects.
    weighted_center = find_weighted_center(my_locations)
    print(f"The weighted center coordinates are: {weighted_center}")
    webbrowser.open(f"https://www.google.com/maps/search/{weighted_center}")
