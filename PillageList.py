# Define a class for City
class City:
    def __init__(self, name, wood, wine, marble, crystal, sulfur):
        # Initialize the city's attributes
        self.name = name  # The name of the city
        self.wood = wood  # The amount of wood produced per hour
        self.wine = wine  # The amount of wine produced per hour
        self.marble = marble  # The amount of marble produced per hour
        self.crystal = crystal  # The amount of crystal produced per hour
        self.sulfur = sulfur  # The amount of sulfur produced per hour

    def __repr__(self):
        # Provide a string representation of the city for easy printing
        return (f"City(name={self.name}, wood={self.wood}, wine={self.wine}, "
                f"marble={self.marble}, crystal={self.crystal}, sulfur={self.sulfur})")

# Function to add a city
def add_city(cities, name, wood, wine, marble, crystal, sulfur):
    # Create a new City object and add it to the cities dictionary
    cities[name] = City(name, wood, wine, marble, crystal, sulfur)

# Function to display all cities
def display_cities(cities):
    # Print each city in the cities dictionary
    for city in cities.values():
        print(city)

# Example usage
cities = {}  # Create an empty dictionary to store cities
add_city(cities, 'Athens', 100, 50, 0, 0, 0)  # Add 'Athens' to the dictionary
add_city(cities, 'Sparta', 200, 0, 0, 75, 0)  # Add 'Sparta' to the dictionary

# Display all cities
display_cities(cities)  # Print all cities and their resource production