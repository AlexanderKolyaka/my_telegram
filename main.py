import telebot;

bot = telebot.TeleBot('7935793397:AAHmGyLrBbIw9hqap5MgmvQhXuxLhlIPuPY')



@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, "Ты нажал на легендарную кнопку старта")

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")

bot.infinity_polling(interval=0, timeout=20)
