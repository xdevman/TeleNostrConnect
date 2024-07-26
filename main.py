import telebot
from teleconnect import *
from config import *

bot = telebot.TeleBot(API_TOKEN)

@bot.channel_post_handler(func=lambda message: message.chat.id == CHANNEL_ID)
def handle_channel_message(message):
    print("Latest message from channel:", message.text)
    send_nostrtext(message.text)

# Start polling
bot.polling(none_stop=True)