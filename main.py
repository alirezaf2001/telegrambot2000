import telebot
#import time
from telebot import types

 from flask import Flask, request
 import os

# bot_token = '1172046559:AAHr1UufCkTaYramIStU-7ePYzokfMk84Vc'
bot_token = process.env.token
 server = Flask(__name__)


bot = telebot.TeleBot(token=bot_token)


log_flag={}
sendmessage_flag = {}
user = []

# def listener(messages):
#     for a in messages:
#         if a.content_type =='text':
#             cid = a.chat.id
#             if cid == 115619427:
#                 if sendmessage_flag[cid] == 1:
#                     for m in messages:
#                         if m.content_type == 'text':
#                             bot.send_message(625619975, str(m.chat.fist_name) + " [" + str(m.chat.id) + "]:" + m.text)
#             elif cid == 625619975 :
#                 if sendmessage_flag[cid] == 1:
#                     for m in messages:
#                         if m.content_type == 'text':
#                             bot.send_message(115619427, str(m.chat.fist_name) + " [" + str(m.chat.id) + "]:" + m.text)
#                 elif log_flag[115619427] == 1:
#                     for m in messages:
#                         if m.content_type == 'text':
#                             bot.send_message(115619427, str(m.chat.fist_name) + " [" + str(m.chat.id) + "]:" + m.text)




def flag_status(uid):
    if uid in log_flag:
        return log_flag[uid]

@bot.message_handler(commands=['sendkiss'])
def send_kiss(message):
    cid = message.chat.id
    if cid ==115619427:
        bot.send_message(625619975, '💋')
    elif cid == 625619975:
        bot.send_message(115619427, '💋')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    cid = message.chat.id
    if cid not in user:
        if cid == 115619427:
            user.append(cid)
            log_flag[cid] = 0
            sendmessage_flag[cid] = 0
            bot.send_message(cid, 'Welcome to the platform Master')
        elif cid == 625619975:
            user.append(cid)
            log_flag[cid] = 0
            sendmessage_flag[cid] = 0
            bot.send_message(cid, 'Welcome to the platform Zahra')
        else:
            bot.send_message(cid, 'You do not have access, please leave the bot')
    else:
        log_flag[cid] = 0
        if cid == 625619975:
            bot.send_message(cid, 'Welcome back Zahra :)')
        elif cid == 115619427:
            bot.send_message(cid, 'Welcome back Master!')



# @bot.message_handler(commands=['toggle_log'])
# def send_meesage(message):
#     cid = message.chat.id
#     if log_flag[cid] == 0:
#         log_flag[cid] = 1
#         bot.send_message(cid, 'Monitoring messages is Online')
#     elif log_flag[cid] == 1:
#         log_flag[cid] = 0
#         bot.send_message(cid, 'Monitoring messages is Offline')
#
# @bot.message_handler(commands=['toggle_sendMessage'])
# def send_meesage(message):
#     cid = message.chat.id
#     if sendmessage_flag[cid] == 0:
#         sendmessage_flag[cid] = 1
#         bot.send_message(cid, 'Sending messages is Online')
#     elif sendmessage_flag[cid] == 1:
#         sendmessage_flag[cid] = 0
#         bot.send_message(cid, 'Sending messages is Offline')

@bot.message_handler(commands=['love'])
def send_welcome(message):
    bot.reply_to(message, 'I LOVE YOU ZAHRA :)')


@bot.message_handler(func=lambda msg: msg.text is not None and 'I love you' in msg.text or 'i love you' in msg.text)
def send_message(message):
    bot.reply_to(message, u'\U00002764')
    bot.reply_to(message, u'\U0001F618')


@bot.message_handler(func=lambda msg: msg.text is not None and 'خستم' in msg.text)
def send_welcome(message):
    bot.reply_to(message, 'خسته نباشی نفسم')

@bot.message_handler(commands='my_id')
def send_message(message):
    bot.reply_to(message, message.chat.id)

# bot.set_update_listener(listener)

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)


#  @server.route('/' + bot_token, methods=['POST'])
#  def getMessage():
#      bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#      return "!", 200


#  @server.route("/")
#  def webhook():
#      bot.remove_webhook()
#      bot.set_webhook(url='https://young-springs-39254.herokuapp.com/' + bot_token)
#      return "!", 200

#  if __name__ == "__main__":
#      server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
