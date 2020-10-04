from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from accesskeys import mytokens

ACCESS_TOKEN = mytokens.ACCESS_TOKEN
ACCESS_SECRET = mytokens.ACCESS_SECRET
CONSUMER_KEY = mytokens.CONSUMER_KEY
CONSUMER_SECRET = mytokens.CONSUMER_SECRET

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])