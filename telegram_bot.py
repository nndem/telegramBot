# pip3 install pytelegrambotapi

import telebot


_api_token = ""

bot = telebot.TeleBot(_api_token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard1.row("Привет", "Жизнь", "Пока")


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, ты написал мне /start", reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "привет мой создатель")
    elif message.text.lower() == "пока":
        bot.send_message(message.chat.id, "прощай мой создатель")
    elif message.text.lower() == "дон":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAMHX6w-kqne0bq_-nTLJknVeYVOoPsAAgYBAALBkbIkLCHHvc5EnqoeBA")
    elif message.text.lower() == "филя":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAMNX6xFjCbjwkm3p4O87ZPWTVSmz9YAAvEDAAI6uRUC4gJUWyH6Ck8eBA")


@bot.message_handler(content_types=["sticker"])
def sticker_id(message):
    print(message)


bot.polling()

