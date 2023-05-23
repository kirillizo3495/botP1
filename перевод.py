import telebot
from googletrans import Translator
from langdetect import detect

# Создаем переводчик
translator = Translator()

# Определяем функцию для обработки сообщений
@bot.message_handler(func=lambda m: True)
def translate_message(message):
  # Определяем язык исходного текста
  src = detect(message.text)

  # Задаем целевой язык
  dest = 'ru'

  # Берем полученное сообщение и переводим его
  translated_text = translator.translate(message.text, src=src, dest=dest).text

  # Отправляем переведенное сообщение
  bot.send_message(message.chat.id, translated_text)

# Запускаем бота
bot.polling()
















































