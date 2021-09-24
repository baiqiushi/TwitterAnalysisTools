
# (1) load user_screen_name_sentiment_score.csv
# user_screen_names = {"__twalker__": {},
#                      "...":{}
#                     }

# (2) load tweets_geo_vaccine_us_nov_2020_to_mar_2021.csv
# tweets = [{"user_screen_name": "__twalker__", "cityID": 23},
#           ...]

# (3) loop tweets
#       for each tweet:
#         user_screen_name = tweet["user_screen_name"]
#         cityID = tweet["cityID"]
#         if user_screen_name in user_screen_names.keys():
#              cityIDs = user_screen_names[user_screen_name]
#              if cityID in cityIDs.keys():
#                 cityIDs[cityID] += 1
#              else:
#                 cityIDs[cityID] = 1

# (4) loop user_screen_names
#       for user_screen_name, cityIDs in user_screen_names.items():
#          most_frequent_cityID = None
#          most_frequent_cityID_count = 0
#          for cityID, count in cityIDs.items():
#             if count > most_frequent_cityID_count:
#                most_frequent_cityID = cityID
#                most_frequent_cityID_count = count
#          user_screen_names[user_screen_name] = most_frequent_cityID

# (5) output user_screen_names {"__twalker__": 23,
#                               ...}

