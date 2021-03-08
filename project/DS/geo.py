class Geopoint:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def closest_parallel(self):
        return round(self.latitude)
    def get_time(self):
        pass
tokyo = Geopoint(latitude = 35.7, longitude = 139.7)
print(tokyo.closest_parallel())
