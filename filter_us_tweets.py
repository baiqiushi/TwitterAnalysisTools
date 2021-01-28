import sys
import ast
import json

###########################################################
#  filter_us_tweets.py
#
#  Purpose:
#    filter out tweets located in the US.
#    filter logic is the following:
#      tweet.place.country_code == 'US'
#
#  Example:
#    gunzip -c coronavirus_12-27-2020.gz | python3 filter_us_tweets.py >> coronavirus_12-27-2020_us.json
#
#  Author:
#    Qiushi Bai (baiqiushi@gmail.com)
###########################################################


def is_us_tweet(tweet_dict):
    if 'place' in tweet_dict.keys():
        if tweet_dict['place'] is not None:
            if 'country_code' in tweet_dict['place'].keys():
                if tweet_dict['place']['country_code'].lower() == 'us':
                    return True
    return False


if __name__ == '__main__':
    for line in sys.stdin:
        tweet_dict = ast.literal_eval(line)
        if is_us_tweet(tweet_dict):
            tweet_json = json.dumps(tweet_dict.encode('utf-8').strip())
            print(tweet_json)

