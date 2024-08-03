import telebot
from telebot import types
bot = telebot.TeleBot('7348026715:AAGWECPJTYRlAYBC2VzNl2k2MSiaEMi2l9o')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Меню')
    item2 = types.KeyboardButton('Ф.И.О')
    
    markup.add(item1,item2)
    
    bot.send_message(message.chat.id, 'Привет!'.format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])    
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == ('Ф.И.О'):
         bot.send_message(message.chat.id, 'Ваше имя:{0.first_name}'.format(message.from_user))
        elif message.text == ('Меню'):     
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Пицца,цена:2000')
            item2 = types.KeyboardButton('Суши с креветками,цена:4000')
            back = types.KeyboardButton('Назад')
            markup.add(item1,item2,back)
           
            bot.send_message(message.chat.id, '"Широкое меню"'.format(message.from_user), reply_markup=markup)
            
        elif message.text == ('Назад'):    
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Меню')
            item2 = types.KeyboardButton('Ф.И.О')
            markup.add(item1,item2)
            
            bot.send_message(message.chat.id, 'Вы в меню', reply_markup=markup)
            
            
            
            
        if message.chat.type == 'private':
          if message.text == ('Пицца'):
             bot.send_message(message.chat.id, 'Хороший выбор,время ожидания:10мин'.format(message.from_user))
             
        if message.chat.type == 'private':
          if message.text == ('Суши с креветками'):
             bot.send_message(message.chat.id, 'Хороший выбор,Время ожидания:5мин'.format(message.from_user))  
                
            
            
        
            
    
    
bot.polling(none_stop=True , interval=0)     