import sys
import ast
import json

###########################################################
#  to_json.py
#
#  Purpose:
#    For some reason, using the Python sample code suggested by Twitter Developer website,
#    the tweets dumped onto disk are in invalid json format
#    (e.g., single quoted and True instead of true for boolean values).
#    This script is intended to clean such data files and covert them into valid json format files.
#
#  Requirement:
#    Python3.7+
#
#  Example:
#    gunzip -c coronavirus_12-27-2020.gz | python3 to_json.py >> coronavirus_12-27-2020.json
#
#  Author:
#    Qiushi Bai (baiqiushi@gmail.com)
###########################################################


if __name__ == '__main__':
    for line in sys.stdin:
        tweet_dict = ast.literal_eval(line)
        tweet_json = json.dumps(tweet_dict)
        print(tweet_json)

