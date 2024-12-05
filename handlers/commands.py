from langdetect import detect


class Message:

    def __init__(self, bot, translator):
        self.bot = bot
        self.translator = translator

    def start(self, message):
        """Метод когда человек введёт /start или /help"""
        if message.text == '/start':
            self.bot.reply_to(
                message,
                'Привет, это бот переводчик.Нажми /help '
                'для дополнительной информации.'
                )
        else:
            self.bot.reply_to(
                message,
                'Напишите свой текст и нажмите enter, бот '
                'переведёт его на русский язык.'
                )

    def translate_message(self, message, str_message=None):
        """Метод, когда человек введёт текст и он его переведёт"""
        # Задаем целевой язык
        dest = 'ru'
        # Определяем какой тип данных поступает, если str заполнен то подана картинка
        if str_message is None:
            src = detect(message.text)
            # Берем полученное сообщение и переводим его
            translated_text = self.translator.translate(
                message.text, src=src, dest=dest
            ).text
        else:
            src = detect(str_message)
            # Берем полученное сообщение и переводим его
            translated_text = self.translator.translate(
                str_message, src=src, dest=dest
            ).text
        # Отправляем переведенное сообщение
        self.bot.send_message(message.chat.id, translated_text)
