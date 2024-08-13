import praw
import config

comments_replied_to = []

def bot_login():
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="testscript by matt")
    return r  # Return the Reddit instance

def run_bot(r, comments_replied_to):
    print("Checking 25 comments")
    for comment in r.subreddit('test').comments(limit=25) :
        if "curry" in comment.body and comment.id not in comments_replied_to:
            print("String with \"curry\" found in comment with comment ID: " + comment.id)
            #comment.reply("I love curry! :D")
            print("Replied to comment " + comment.id)
            comments_replied_to.append(comment.id)
            print(comments_replied_to)
  
def saved_file(comments_replied_to):
    with open("comments.txt", "w") as f:
        for comment_id in comments_replied_to:
            f.write(comment_id + "\n")

# Use the returned Reddit instance from bot_login()

test = bot_login()

run_bot(test, comments_replied_to)
