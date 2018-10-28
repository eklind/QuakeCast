from TwitterAPI import TwitterAPI


TRACK_TERM = 'pizza'


CONSUMER_KEY = 'iy5OwSaUBxMUley4xAihsMVIA'
CONSUMER_SECRET = 'e8RJzkNC4AIGYeE6AAwy1tymMH8ap5u6uNmsllhrsn31BxQaK3'
ACCESS_TOKEN_KEY = '200873390-penyP8vPQ7c4HpHtqLFK1taLry2PPFsUAa0m4a8q'
ACCESS_TOKEN_SECRET = 'UkDchSuXAT53cQ9N0w64QduWlOuMFp5FYLFRy8tUX55ZZ'


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

r = api.request('statuses/filter', {'track': TRACK_TERM})

for item in r:
    print(item['text'] if 'text' in item else item)
