import telebot

from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message,"абаюдненько")
@bot.message_handler(commands=['ahab'])
def start_messageee(message):
    bot.reply_to(message,"baha")
@bot.message_handler(content_types='text')
def start_messagee(message):
    if message.text == "как дела":
        bot.reply_to(message,"хззз")
bot.infinity_polling()