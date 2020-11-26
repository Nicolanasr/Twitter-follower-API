import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/followers/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
# cursor = -1

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    # while cursor != 0 :
    #     response_dictionary = twurl.augment(TWITTER_URL,
    #                                         {'screen_name': acct, 'count': '200', 'cursor': cursor})
    #     print('Retrieving', response_dictionary )
    #     connection = urllib.request.urlopen(response_dictionary, context=ctx)
    #     data = connection.read().decode()

    #     js = json.loads(data)
    #     # print(json.dumps(js, indent=2))
    #     cursor = js['next_cursor']
    #     # for u in js['users']:
    #     #     print(u['screen_name'])
    #     # print("--------------------------------")

    response_dictionary = twurl.augment(TWITTER_URL,
                                            {'screen_name': acct, 'count': '200'})
    connection = urllib.request.urlopen(response_dictionary, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    # print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    
    if count == 0 :
        followersnow = list()
        followerscheck = list()
        count = count + 1
        for u in js['users']:
            followersnow.append(u['screen_name'])
        followerscheck = followersnow
        print("check: ",len(followerscheck))
    else:
        followersnow = list()
        for u in js['users']:
            followersnow.append(u['screen_name'])
        followersnowtmp = followersnow[:20]
        check =  all(item in followerscheck for item in followersnowtmp)
        if check is not True :
            for user in followersnowtmp :
                if user not in followerscheck :
                    print("New Follower: ", user)
            followerscheck = followersnow
        else:
            if check is True and followersnowtmp != followerscheck[:20]:
                print("Follower lost!")
                followerscheck = followersnow
            else:
                print("Everything is still the same")
        