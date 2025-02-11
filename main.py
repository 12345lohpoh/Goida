import telebot

from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message,"абаюдненько")
@bot.message_handler(commands=['skinyArt'])
def start_messageee(message):
    bot.reply_to(message,"вообще тут стоит функция в которую можно многое засунуть, всякие формулы и разные штуки")
@bot.message_handler(content_types=['kall'])
def start_messagee(message):
    bot.reply_to(message,"и сразу пуки каки")
bot.infinity_polling()