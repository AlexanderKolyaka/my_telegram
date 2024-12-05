import telebot
from googletrans import Translator
from handlers.commands import Message
from language.lang_text import change_languae
import pytesseract
from PIL import Image
import io


if __name__ == '__main__':
    bot = telebot.TeleBot('7935793397:AAHmGyLrBbIw9hqap5MgmvQhXuxLhlIPuPY')
    translator = Translator()
    message_handler = Message(bot, translator)

    # Обработчик команды /start
    @bot.message_handler(commands=['start', 'help'])
    def handle_start(message):
        message_handler.start(message)

    @bot.message_handler(commands=['settings'])
    def handle_settings(message):
        bot.reply_to(
                message,
                change_languae
                )
        bot.register_next_step_handler(
            message, message_handler.change_language
            )

    # Обработчик всех сообщений
    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        message_handler.translate_message(message)

    @bot.message_handler(content_types=['photo'])
    def handle_photo(message):
        # Получаем файл изображения
        file_info = bot.get_file(message.photo[-1].file_id)
        file = bot.download_file(file_info.file_path)
        # Конвертируем данные в изображение
        image = Image.open(io.BytesIO(file))

        # Используем Tesseract для распознавания текста
        text = pytesseract.image_to_string(image, lang='eng')

        message_handler.translate_message(message, text)

    bot.infinity_polling(interval=0, timeout=20)
