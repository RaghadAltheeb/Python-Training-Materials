raw_sensor_data = [15.5, -2.0, 18.1, 0.0, -99.9, 22.4]
filtered_data = list(filter(lambda x: x >= 0, raw_sensor_data))
print(filtered_data)
map_data = list(map(lambda x: x * 1.5 , filtered_data))
print(map_data)
