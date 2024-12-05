from langdetect import detect
import language.lang_text as lang_text


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
                lang_text.start_text
                )
        else:
            self.bot.reply_to(
                message,
                lang_text.help_text
                )
            
    def change_language(self, message):
        self.dest = message.text

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
