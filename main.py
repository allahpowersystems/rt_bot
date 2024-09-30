import requests
import telebot
import config
import time

bot = telebot.TeleBot(config.TOKEN)
oldTitle = ""

while True:
    try:
        resp = requests.get("https://russian.rt.com/rss") # отредактируйте это говно так, как нужно вам (лучше юзайте бсоуп это я просто гвонокодер)
        item = resp.text.split("item>")[1].split("CDATA[")
        title = item[1].split("]]")[0]
        desc = item[4].split("<br/>")[0]
        msg = f"💥 {title}\n\n{desc}\n\n{config.LINK}".strip()

        if title != oldTitle and "http" not in msg: # мне лень делать обработку фотографий (мб в следующей обнове завезу)
            bot.send_message(chat_id=config.CHANNEL_ID, text=msg)
            oldTitle = title

        time.sleep(config.UPDATE_TIME)
    except: pass