import csv
import datetime
import sys
import json
from collections import OrderedDict

###########################################################
#  json_to_csv.py
#
#  Purpose:
#    convert tweets json to csv with reduced columns
#
#  Example:
#    cat coronavirus_us.json | python json_to_csv.py >> coronavirus_us.csv
#
#  Author:
#    Qiushi Bai (baiqiushi@gmail.com)
###########################################################
schema = OrderedDict()
schema['id'] = 'bigint'
schema['created_at'] = 'datetime'
schema['text'] = 'varchar(500)'
schema['in_reply_to_status'] = 'varchar(25)'
schema['in_reply_to_user'] = 'varchar(25)'
schema['favorite_count'] = 'int'
schema['retweet_count'] = 'int'
schema['lang'] = 'varchar(10)'
schema['is_retweet'] = 'tinyint'
schema['hashtags'] = 'varchar(500)'
schema['user_mentions'] = 'varchar(500)'
schema['user_id'] = 'varchar(25)'
schema['user_name'] = 'varchar(500)'
schema['user_screen_name'] = 'varchar(500)'
schema['user_location'] = 'varchar(500)'
schema['user_description'] = 'varchar(500)'
schema['user_followers_count'] = 'int'
schema['user_friends_count'] = 'int'
schema['user_statues_count'] = 'int'
schema['stateName'] = 'varchar(100)'
schema['countyName'] = 'varchar(100)'
schema['cityName'] = 'varchar(100)'
schema['country'] = 'varchar(100)'
schema['bounding_box'] = 'varchar(100)'

if __name__ == '__main__':
    # print out converted csv to stdout
    csv_writer = csv.writer(sys.stdout)
    for line in sys.stdin:
        tweet_json = json.loads(line)
        csv_row = []
        for column_name, column_type in schema.items():
            if column_name in ["bounding_box", "country"] and tweet_json.get("place"):
                value = tweet_json.get("place").get(column_name)
            elif column_name in ["stateName", "countyName", "cityName"] and tweet_json.get("geo_tag"):
                value = tweet_json.get("geo_tag").get(column_name)
            elif column_name in ["user_id", "user_name", "user_screen_name", "user_location", "user_description",
                                 "user_followers_count", "user_friends_count", "user_statues_count"] \
                    and tweet_json.get("user"):
                value = tweet_json.get("user").get(column_name[5:])
            elif column_name == 'is_retweet' and tweet_json.get(column_name):
                value = int(tweet_json.get(column_name))
            elif column_name == 'created_at' and tweet_json.get(column_name):
                value = datetime.datetime.strptime(tweet_json.get(column_name), '%a %b %d %H:%M:%S %z %Y')
            else:
                value = tweet_json.get(column_name)
            csv_row.append(value)
        csv_writer.writerow(csv_row)
