import os, praw, random, time
from icrawler.builtin import GoogleImageCrawler
from keepalive import keepalive
from os import listdir
from os.path import isfile, join

words = open("words.txt", "r+")
allwords = words.readlines()
list_of_words = []

for lines in allwords:
  list_of_words.append(lines)

words.close()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("SECRET"),
    password=os.getenv("PASSWORD"),
    user_agent="Reddit Image Poster by u/",
    username=os.getenv("USERNAME"),
)

reddit.validate_on_submit = True

keepalive()
while True:
  try:
    randomword = str((list_of_words[random.randint(0,len(list_of_words)-1)]).rstrip())
    google_crawler = GoogleImageCrawler(storage={'root_dir': f"./dataset/{randomword} meme"})
    google_crawler.crawl(keyword=f"{randomword} meme", max_num=1)
    onlyfiles = [f for f in listdir(f"./dataset/{randomword} meme/") if isfile(join(f"./dataset/{randomword} meme/", f))]
    for file in onlyfiles:
      reddit.subreddit("me_irl").submit_image("me_irl", f"./dataset/{randomword} meme/{file}")
      os.remove(f"./dataset/{randomword} meme/{file}")
      os.rmdir(f"./dataset/{randomword} meme/")
      time.sleep(1800)
  except:
    continue

import praw, os

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("SECRET"),
    password=os.getenv("PASSWORD"),
    user_agent="Reddit Image Poster",
    username=os.getenv("USERNAME"),
)

redditor = reddit.redditor("")

i = 0
for post in redditor.controversial("all"):
    post.delete()
    i+=1
    if i == 3: 
      break
