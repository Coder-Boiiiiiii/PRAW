#Imports
import praw
import random

#Providing the ecessary info
reddit = praw.Reddit(client_id = "Client_ID",
                     client_secret = "CLIENT_SECRET",
                     username = "USERNAME_ON_REDDIT",
                     password = "PASSWORD_OF_PROFILE",
                     user_agent = "pythonpraw")

#The code
jokes = []

subreddit = reddit.subreddit("jokes")
top = subreddit.top(limit = 100)
all_submissions = []

for submission in top:
    all_submissions.append(submission)
    
rand_sub = random.choice(all_submissions)
rand_sub_title = rand_sub.title
rand_sub_text = rand_sub.selftext
rand_sub_url = rand_sub.url
upvotes = rand_sub.score

if not submission.over_18:
    print("TITLE: " + rand_sub_title)
    print("Joke: " + rand_sub_text)
    print("URL: " + rand_sub_url)
    print("Upvotes: " + str(upvotes))