import logging
from os import environ as env
import g4f
import telebot
import openai
from env import BOT_API_KEY, OPENAI_API_KEY, USER_KEY

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(BOT_API_KEY)
openai.api_key = OPENAI_API_KEY
user_id = USER_KEY


@bot.message_handler(func=lambda message: True)
def get_response(message):
  if int(message.chat.id) != user_id:
    bot.send_message("This bot is not for public but private use only.")
  else:
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
    )
    bot.send_message(message.chat.id, f'{response["choices"][0]["text"]}', parse_mode="None")

bot.infinity_polling()
