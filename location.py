class Location:
    def __init__(self, name, lat, lon, weight=1):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.weight = weight
        self.coords = (lat, lon)