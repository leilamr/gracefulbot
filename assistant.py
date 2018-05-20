from chatbotResponse import response

import telebot
#conexao com o bot
bot = telebot.TeleBot('tokenyourbot')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Olá, eu sou a Grace")
@bot.message_handler(func=lambda message:True)
def echo_message(message):
    bot.send_message(message.chat.id, response(message.text))

bot.polling()
