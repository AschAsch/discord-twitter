# coding: UTF-8
import config
from requests_oauthlib import OAuth1Session

CK      = config.TWITTER_CONSUMER_KEY
CS      = config.TWITTER_CONSUMER_SECRET
AT      = config.ACCESS_TOKEN
ATS     = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理