# coding: UTF-8
import twitter_oauth
import json, datetime, logging

# ログファイルへの書き出し
def write_logs(txt):
    
    LOG_LEVEL_FILE = 'INFO'
    LOG_LEVEL_CONSOLE = 'INFO'
    _detail_formatting = '%(asctime)s %(levelname)-8s [%(module)s#%(funcName)s %(lineno)d] %(message)s'
    now = datetime.datetime.now()
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL_FILE),
        format=_detail_formatting,
        filename='./logs/' + '{0:%Y_%m_%d}'.format(now) + '.log'
    )
    console = logging.StreamHandler()
    console.setLevel(getattr(logging, LOG_LEVEL_CONSOLE))
    console_formatter = logging.Formatter(_detail_formatting)
    console.setFormatter(console_formatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(console)
    logging.getLogger("datetime_module").addHandler(console)
    
    logging.info(txt)

# DM送信
def send_directMessage(user_id, txt):
    
    url = 'https://api.twitter.com/1.1/direct_messages/events/new.json'
    headers = {'content-type': 'application/json'}
    params = {
        "event":{
            "type": "message_create",
            "message_create": {
                "target": {
                    "recipient_id": user_id
                },
                "message_data": {
                    "text": txt
                }
           }
        }
    }
    params = json.dumps(params)
    res = twitter_oauth.twitter.post(url, headers=headers, data=params)
    if not res.status_code == 200:
        loginfo.logging.info("DM send failed. status_code: " + str(res.status_code))