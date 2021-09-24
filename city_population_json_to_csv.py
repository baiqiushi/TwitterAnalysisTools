import csv
import json

###########################################################
#  city_population_json_to_csv.py
#
#  Purpose:
#    convert city_population.json to city_population.csv
#
#  Prerequisites:
#    city_population.json exits under the same directory with this file
#
#  Output: city_area.csv
#    [cityID, cityName, population]
#
#  Example:
#    python city_population_json_to_csv.py
#
#  Author:
#    Qiushi Bai (baiqiushi@gmail.com)
###########################################################

f = open("city_population.json",)
cities = json.load(f)
with open("city_population.csv", "w") as csv_out:
    csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    header = ["cityID", "cityName", "population"]
    csv_writer.writerow(header)
    for city in cities:
        row = [
            city["cityID"],
            city["name"],
            city["population"]
        ]
        csv_writer.writerow(row)
print("wrote to csv file city_population.csv.")

