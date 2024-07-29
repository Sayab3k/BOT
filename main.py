import telebot


bot = telebot.TeleBot('7348026715:AAGWECPJTYRlAYBC2VzNl2k2MSiaEMi2l9o')

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Здраствуйте!')
    
    
bot.polling(none_stop=True)   