from langdetect import detect
import language.lang_text as lang_text
from googletrans import LANGUAGES


class Message:

    def __init__(self, bot, translator, dest='ru'):
        self.bot = bot
        self.translator = translator
        self.dest = dest  # Задаем целевой язык

    def start(self, message):
        """Метод когда человек введёт /start или /help"""
        if message.text == '/start':
            self.bot.reply_to(
                message,
                lang_text.START_TEXT
                )
        else:
            self.bot.reply_to(
                message,
                lang_text.HELP_TEXT
                )

    def change_language(self, message):
        """Метод смены языка в переводчике, комманда /settings"""
        if message.text in LANGUAGES:
            self.dest = message.text
            self.bot.send_message(
                message.chat.id, "Язык сменён на " + self.dest
                )
        else:
            self.bot.send_message(
                    message.chat.id,
                    lang_text.ERROR_TEXT
                )

    def translate_message(self, message, str_message=None):
        """Метод, когда человек введёт текст и он его переведёт"""
        # Определяем какой тип данных поступает
        # если str заполнен,то подана картинка
        if str_message is None:
            src = detect(message.text)
            # Берем полученное сообщение и переводим его
            translated_text = self.translator.translate(
                message.text, src=src, dest=self.dest
            ).text
        else:
            src = detect(str_message)
            # Берем полученное сообщение и переводим его
            translated_text = self.translator.translate(
                str_message, src=src, dest=self.dest
            ).text

        # Отправляем переведенное сообщение
        self.bot.send_message(message.chat.id, translated_text)
