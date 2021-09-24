import csv
import json

###########################################################
#  city_geo_json_to_csv.py
#
#  Purpose:
#    convert city_geo.json to city_area.csv
#
#  Prerequisites:
#    city_geo.json exits under the same directory with this file
#
#  Output: city_area.csv
#    [stateID, stateName, countyID, countyName, cityID, cityName, landArea, waterArea]
#
#  Example:
#    python city_geo_json_to_csv.py
#
#  Author:
#    Qiushi Bai (baiqiushi@gmail.com)
###########################################################

f = open("city_geo.json",)
data = json.load(f)
cities = data["features"]
with open("city_area.csv", "w") as csv_out:
    csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    header = ["stateID", "stateName", "countyID", "countyName", "cityID", "cityName", "landArea", "waterArea"]
    csv_writer.writerow(header)
    for city in cities:
        properties = city["properties"]
        row = [
            properties["stateID"],
            properties["stateName"],
            properties["countyID"],
            properties["countyName"],
            properties["cityID"],
            properties["name"],
            properties["landArea"],
            properties["waterArea"]
        ]
        csv_writer.writerow(row)
print("wrote to csv file city_area.csv.")

