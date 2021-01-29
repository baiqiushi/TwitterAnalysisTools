#! /usr/bin/env python
import json
import re
import csv
import sys


def convert_adm_to_csv(file_name: str):
    headers = ['id', 'created_at', 'text', 'in_reply_to_status_id', 'in_reply_to_user_id', 'favorite_count',
               'retweet_count',
               'lang', 'retweeted', 'hashtags', 'user_mentions', "user_id", "user_name", "user_screen_name",
               "user_location", "user_description", "user_followers_count", "user_friends_count", "user_statues_count",
               "stateName", "countyName",
               "cityName", "country", "bounding_box"]
    with open(f"{file_name}.csv", 'w') as output_file:
        w = csv.writer(output_file)
        first = True
        with open(file_name, 'r') as file:
            for i, line in enumerate(file):
                line = re.sub(r"(datetime\()(\"\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d\.\d\d\dZ\")(\))", r"\2", line)
                line = re.sub(r"(date\()(\"\d\d\d\d-\d\d-\d\d\")(\))", r"\2", line)
                line = re.sub(r"(rectangle\()(\"-?\d*\.\d*,-?\d*\.\d* -?\d*\.\d*,-?\d*\.\d*\")(\))", r"\2", line)
                line = re.sub(r"(point\()(\"-?\d*\.\d*,-?\d*\.\d*\")(\))", r"\2", line)
                line = re.sub(r"({{)", r"[", line)
                line = re.sub(r"(}})", r"]", line)
                if first:
                    w.writerow(headers)
                    first = False
                res = []
                payload = json.loads(line.strip())
                for header in headers:

                    if header in ["bounding_box", "country"] and payload.get("place"):
                        value = payload.get("place").get(header)
                    elif header in ["stateName", "countyName", "cityName"] and payload.get("geo_tag"):
                        value = payload.get("geo_tag").get(header)
                    elif header in ["user_id", "user_name", "user_screen_name", "user_location", "user_description",
                                    "user_followers_count", "user_friends_count", "user_statues_count"] \
                            and payload.get("user"):
                        value = payload.get("user").get(header[5:])
                    elif header in 'created_at':
                        value = payload.get('create_at')
                    elif header in 'retweeted':
                        value = int(payload.get('is_retweet'))
                    elif header in ['in_reply_to_status_id', 'in_reply_to_user_id']:
                        value = payload.get(header[:-3])
                    else:
                        value = payload.get(header)
                    res.append(value)
                w.writerow(res)


if __name__ == '__main__':
    convert_adm_to_csv(sys.argv[1])
