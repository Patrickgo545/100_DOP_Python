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

highest_temp = data['temp'].max()
# print(highest_temp)

# GET DATA IN COLUMNS   
# print(data['condition'])
# print(data.condition)

# PRINT A ROW
# print(data[data.day == 'Monday'])

# CHALLENGE - print row with the highest tem
# print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
# print(monday.condition)
# print((monday.temp * 9/5) + 32)

# CREATE A DATAFRAME FROM SCRATCH
dict_data = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 57, 65]
}

new_dataframe = pd.DataFrame(dict_data)
new_dataframe.to_csv("new_data.csv")