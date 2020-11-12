# pip3 install pytelegrambotapi
import requests
import telebot
import re

telegram_api_token = ""
youtube_api_token = ""

bot = telebot.TeleBot(telegram_api_token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=None, one_time_keyboard=None)
keyboard1.row("Привет", "Жизнь", "Пока")

youtube_api = "https://www.googleapis.com/youtube/v3/videos?"


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
    elif message.text.lower() == "жизнь":
        video_id = "8ZiJsC11UDc"
        url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={youtube_api_token}&part=snippet"

        response = make_response(url)
        link = get_video_link(response)
        pic = get_video_pic(response)

        bot.send_photo(message.chat.id, pic)
        bot.send_message(message.chat.id, link)
        print(link, "\n", pic)


@bot.message_handler(content_types=["sticker"])
def sticker_id(message):
    print(message)


def make_response(url):
    response = requests.get(url).json()
    return response


def get_video_link(response):
    description = response.get("items")[0].get("snippet").get("description")
    link = re.split("www", description)[1]
    return "https://www"+link


def get_video_pic(response):
    pic = response.get("items")[0].get("snippet").get("thumbnails").get("default").get("url")
    return pic


bot.polling()

