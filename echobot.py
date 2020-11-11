#!/usr/bin/env python

import telebot

token = "1478647169:AAHHq4wWR_0mFxeV34_JAySskVCp48SCqfE"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()
