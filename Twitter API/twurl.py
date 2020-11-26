import urllib.request, urllib.parse, urllib.error
import oauth
import hidden

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

consumer_key= "q5iuf6h59dJFmDSTbSxhMQ2v1",
consumer_secret= "RY0Va46EoKQO8cu7kDPAEmOhCV9zTRYhcPresDX7Wq03VLl963"
token_key= "445899591-OjmUWi71pesThKMnq8bblMpMGGpUnR8M6IKHAHhk"
token_secret= "LKdfRbu6k7qiQGDmfUm4y70jux5R2yxBl6QgBEOo6HsQl"

def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'],
                                   secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                    token=token, http_method='GET', http_url=url,
                    parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)
    return oauth_request.to_url()