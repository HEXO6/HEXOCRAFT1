import os
import telebot 
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot (API KEY)
@bot.message_handler (commands = ['greet'])
def greet (message) :
  bot.reply_to (message,"hey there its working")
  bot.polling()
