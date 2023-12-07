# with open("./weather_data.csv") as weather:
#     data = weather.readlines()

# print(data)


# # CSV LIBRARY
# import csv

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

#     # EXTRACT TEMPERATURES FROM FILE LIST
#     for temp in data:
#         if temp[1] != "temp":
#             temperatures.append(int(temp[1]))

# print(temperatures)


import pandas as pd

data = pd.read_csv("./weather_data.csv")
# print(data)
# print(data["temp"])

# TYPE CHECK
    # series - list
    # data Frame - The table
# print(type(data['temp']))

# CREATE DICTIONARY
data_dict = data.to_dict()
# print(data_dict)

# TEMP TO LIST
temp_list = data["temp"].to_list()
# print(temp_list)

# AVERAGE TEMPERATURE

average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

average_temp_function = data['temp'].mean()
# print(average_temp_function)