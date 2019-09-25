# coding: UTF-8
import json
import datetime
import pytz
import discord

import config
import twitter_oauth
import loginfo

client = discord.Client()

# UTCからJSTへ変換
def utc_to_jst(dt):
    utc    = pytz.timezone('UTC')
    utc_dt = utc.localize(dt)
    jst    = pytz.timezone('Asia/Tokyo')
    jst_dt = utc_dt.astimezone(jst)
    
    return jst_dt
    
# 該当ユーザーにTwitterのDMを送信
def begin_twitter_DM(message):
    
    user_id = config.USER_ID
    loginfo.send_directMessage(user_id, message)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client)) # BOTのログイン

@client.event
async def on_message(message):
    
    author        = message.author        # メッセージの送信元
    clean_content = message.clean_content # メッセージ内容
    channel       = message.channel       # チャンネル名
    attachments   = message.attachments   # 添付情報
    created_at    = message.created_at    # タイムスタンプ
    
    # 日本時間に変更
    created_at = utc_to_jst(created_at)
    
    begin_twitter_DM('To:' + author.name + '\n' + clean_content)
    

client.run(config.DISCORD_BOT_TOKEN)

