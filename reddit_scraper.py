import praw
import pandas as pd
import datetime as dt
#NOTE: Reddit's request limit is 1000



topics_dict = { "title":[], 
                "score":[], 
                "id":[], "url":[],  
                "comms_num": [], 
                "created": [], 
                "body":[]}

reddit = praw.Reddit(client_id='P', \
                    client_secret='C', \
                    user_agent='Post_Generator', \
                    username='NAME', \
                    password='PASS')


subreddit = reddit.subreddit('greentext')

top_subreddit = subreddit.top(limit=5)
for submission in subreddit.top(limit=1):
    print(submission.title, submission.url)


for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

print(topics_data)
