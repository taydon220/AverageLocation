class Location:
    def __init__(self, name, lat, lon, weight=1):
        self.name = name  # String, name of city. Ex) Houston, TX
        self.lat = lat  # Float, decimal value latitude.
        self.lon = lon  # Float, decimal value longitude.
        self.weight = weight  # Float, years spent in this location.
        self.coords = (lat, lon)

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Coordinates: {self.coords}")
        print(f"Weight: {self.weight} year(s).\n")