# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TWITTER_CONSUMER_KEY    = os.environ.get("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN            = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET     = os.environ.get("ACCESS_TOKEN_SECRET")
USER_ID                 = os.environ.get("USER_ID")
DISCORD_BOT_TOKEN       = os.environ.get("DISCORD_BOT_TOKEN")