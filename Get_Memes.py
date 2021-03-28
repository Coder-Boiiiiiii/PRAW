#We import PRAW & Random
import praw
import random

#We give the import details
reddit = praw.Reddit(client_id = "Client_ID",
                     client_secret = "CLIENT_SECRET",
                     username = "USERNAME_ON_REDDIT",
                     password = "PASSWORD_OF_PROFILE",
                     user_agent = "pythonpraw")

#We get the memes
subreddit = reddit.subreddit("memes")
top = subreddit.top(limit = 100)
all_submissions = []

for submission in top:
    all_submissions.append(submission)
    
rand_sub = random.choice(all_submissions)
rand_sub_title = rand_sub.title
rand_sub_url = rand_sub.url
rand_sub_votes = rand_sub.score

if not submission.over_18:
    #Prints the title, URL & The votes.
    print("Title: " + rand_sub_title)
    print("URL: " + rand_sub_url)
    print("Votes: " + str(rand_sub_votes))