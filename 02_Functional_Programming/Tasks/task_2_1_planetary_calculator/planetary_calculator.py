def calculate_weight(mass, planet="Earth"):
    if planet == "Earth":
        gravity = 9.8
    elif planet == "Mars":
        gravity = 3.71
    elif planet == "Jupiter":
        gravity = 24.79
    return mass * gravity

earth_weight = calculate_weight(mass=100)
print(f"Weight on Earth: {earth_weight} ")

mars_weight = calculate_weight(mass=100, planet="Mars")
print(f"Weight on Mars: {mars_weight} ")

jupiter_weight = calculate_weight(mass=100, planet="Jupiter")
print(f"Weight on Jupiter: {jupiter_weight} ")