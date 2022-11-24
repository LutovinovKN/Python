import telebot

bot = telebot.TeleBot("5942849137:AAHp4UxlAKETIp0NAezUjRZNiKLlcm8Zf8U", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
# bot.infinity_polling()
bot.polling(non_stop = True, interval = 1)

content_types=["text"]