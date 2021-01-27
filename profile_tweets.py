import sys
import ast


###########################################################
#  profile_tweets.py
#
#  Purpose:
#    count among tweets processed:
#    (1) How many have not-none 'place' attribute at root level?
#    (2) How many have in US 'place' attribute at root level?
#    (3) How many have not-none 'place' attribute inside the 'quoted_status' nested tweet?
#    (4) How many have in US 'place' attribute inside the 'quoted_status' nested tweet?
#    (5) How many have not-none 'place' attribute inside the 'retweeted_status' nested tweet?
#    (6) How many have in US 'place' attribute inside the 'retweeted_status' nested tweet?
#
#  Example:
#    gunzip -c coronavirus_12-27-2020.gz | python3 profile_tweets.py
#
#  Author:
#    Qiushi Bai (baiqiushi@gmail.com)
###########################################################

def count_place(dict_obj):
    if 'place' in dict_obj.keys():
        if dict_obj['place'] is not None:
            return 1
    return 0


def count_place_us(dict_obj):
    if 'place' in dict_obj.keys():
        if dict_obj['place'] is not None:
            if 'country_code' in dict_obj['place'].keys():
                if dict_obj['place']['country_code'].lower() == 'us':
                    return 1
    return 0


if __name__ == '__main__':
    countries = {}
    count = 0
    count_root_place = 0
    count_quoted_status_place = 0
    count_retweeted_status_place = 0
    count_root_us = 0
    count_quoted_status_us = 0
    count_retweeted_status_us = 0
    for line in sys.stdin:
        tweet = ast.literal_eval(line)
        count += 1
        count_root_place += count_place(tweet)
        count_root_us += count_place_us(tweet)
        if 'quoted_status' in tweet.keys():
            if tweet['quoted_status'] is not None:
                count_quoted_status_place += count_place(tweet['quoted_status'])
                count_quoted_status_us += count_place_us(tweet['quoted_status'])
        if 'retweeted_status' in tweet.keys():
            if tweet['retweeted_status'] is not None:
                count_quoted_status_place += count_place(tweet['retweeted_status'])
                count_quoted_status_us += count_place_us(tweet['retweeted_status'])
    print('--------------------------------------------')
    print(str(count) + ' tweets has been processed.')
    print(str(count_root_place) + " has place.")
    print(str(count_root_us) + " has place in US.")
    print(str(count_quoted_status_place) + " has place in quoted_status.")
    print(str(count_quoted_status_us) + " has place in US in quoted_status.")
    print(str(count_retweeted_status_place) + " has place in retweeted_status.")
    print(str(count_retweeted_status_us) + " has place in US in retweeted_status.")



