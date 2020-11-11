import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

def oauth(consumer_key, consumer_secret):    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    
    verify_code = input("Authenticate at %s and then enter you verification code here > " % auth_url) 
    auth.get_access_token(verify_code)
    
    return tweepy.API(auth)

def delete_all(api):
    saveData = []    
    outFile = open("allTweets.txt", "w")

    for status in tweepy.Cursor(api.user_timeline).items():
        outFile.write(str(status.created_at) + " | " + str(status.text + "\n")

        try:
            api.destroy_status(status.id)
            print ("Deleted: ", status.id)
        except:
            print ("Failed to delete: ", status.id)
            
    outFile.close()
    
if __name__ == "__main__":
    auth = oauth(CONSUMER_KEY, CONSUMER_SECRET)
    delete_all(auth)