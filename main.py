import telebot
from googletrans import Translator
from handlers.commands import Message


if __name__ == '__main__':
    bot = telebot.TeleBot('7935793397:AAHmGyLrBbIw9hqap5MgmvQhXuxLhlIPuPY')
    translator = Translator()
    message_handler = Message(bot, translator)

    # Обработчик команды /start
    @bot.message_handler(commands=['start', 'help'])
    def handle_start(message):
        message_handler.start(message)
    # Обработчик всех сообщений

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        message_handler.translate_message(message)

    @bot.message_handler(content_types=['photo'])
    def handle_photo(message):
        photo = message.photo[-1]
        file_info = bot.get_file(photo.file_id)
        bot.send_message(type(photo), type(file_info))

    bot.infinity_polling(interval=0, timeout=20)
