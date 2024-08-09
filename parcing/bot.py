import requests
from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('Bu yerni token uchun qoldirib ketaman.')

@bot.message_handler(commands=['start'])
def reaction_start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"Assalomu aleykum!\nYangiliklar botimizga xush kelibsiz!/latest buyurug'ini kiriting va so'nggi soatlardagi yangiliklardan xabardor bo'ling")

@bot.message_handler(commands=['latest'])
def reaction_latest(message: Message):
    chat_id = message.chat.id
    response = requests.get('http://127.0.0.1:8000/api/news/')
    news = response.json()

    if not news:
        bot.send_message(chat_id,'Yangiliklar yoq')
        return
    for item in news[:5]:
        text = f"<b>{item['title']}</b>\nSana: {item['date']}\n<a href='{item['link']}'>Ba'tafsil bu yerda o'qing</a>\nKo'rishlar soni: <b>{item['visibility']}</b> ta"
        bot.send_message(chat_id,text,parse_mode='HTML')



if __name__ == '__main__':
    bot.infinity_polling()
