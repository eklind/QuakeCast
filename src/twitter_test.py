from TwitterAPI import TwitterAPI


TRACK_TERM_1 = 'sweden'
TRACK_TERM_2 = 'dog'
TRACK_TERM_3 = 'bird'
LOCATION = -122.75,36.8,-121.75,37.8 #San Fransisco
LOCATION2 = -74,40,-73,41
LOCATION3= 75.08,35.2

# TRACK_TERM_4 = ''
#TRACK_TERM_5 = ''


CONSUMER_KEY = 'iy5OwSaUBxMUley4xAihsMVIA'
CONSUMER_SECRET = 'e8RJzkNC4AIGYeE6AAwy1tymMH8ap5u6uNmsllhrsn31BxQaK3'
ACCESS_TOKEN_KEY = '200873390-penyP8vPQ7c4HpHtqLFK1taLry2PPFsUAa0m4a8q'
ACCESS_TOKEN_SECRET = 'UkDchSuXAT53cQ9N0w64QduWlOuMFp5FYLFRy8tUX55ZZ'


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

#r1 = api.request('statuses/filter', {'track': TRACK_TERM_1, 'locations': LOCATION})
r1 = api.request('statuses/filter', {'track': TRACK_TERM_2,'locations': LOCATION})
r2 = api.request('statuses/filter', {'locations': LOCATION})


for item in r1:
   print(item['text'] if 'text' in item else item)
   print('Stop')

