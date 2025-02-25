import telebot
from telebot import types


from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)

def create_keyboard():
    klava = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("кнопка")
    klava.add(button1)

    return klava

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message,"абаюдненько", reply_markup=create_keyboard())
@bot.message_handler(commands=['ahab'])
def start_messageee(message):
    bot.reply_to(message,"baha")
@bot.message_handler(content_types='text')
def start_messagee(message):
    if message.text == "как дела":
        bot.reply_to(message,"хззз")
    if message.text == "кнопка":
        bot.reply_to(message,"ты нажал на кнопку")
bot.infinity_polling()