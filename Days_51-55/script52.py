# Day 52 of 100 Days of Code Challenge
# Instagram follower bot
# follows all the accounts that are following a specific creator

import os
from script52_insta_bot import InstaFollower

# instagram constants
INSTA_USER = "snake_lot123"
INSTA_PASS = os.environ.get("INSTA_PASS")
ACCOUNT = "snake.wild"

insta_bot = InstaFollower()
insta_bot.login(user=INSTA_USER, password=INSTA_PASS)
insta_bot.find_followers(ACCOUNT)
insta_bot.follow()
