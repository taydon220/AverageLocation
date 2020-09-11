class Location:
    def __init__(self, name, lat, lon, weight=1):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.weight = weight
        self.coords = (lat, lon)

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Coordinates: {self.coords}")
        print(f"Weight: {self.weight} year(s).\n")