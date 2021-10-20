import telebot
from telebot import types
from TrueAnswer import parsing1
from asd import short_report
import time

bot = telebot.TeleBot("2036325211:AAGxlMxr4ty9uuoEGamhL3z-njenJojy3Bo")

@bot.message_handler(commands=['start'])
def send_welcome(message):

	# клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	but1 = types.KeyboardButton ("Быстрая сводка по ошибкам")
	but2 = types.KeyboardButton ("Просмотреть весь список (~8 минут)")
	but3 = types.KeyboardButton ("Хочу получать отчет по лендингам c ошибками каждые 5 минут")
	markup.add(but1)
	markup.add(but2)
	markup.add(but3)

	bot.reply_to(message, "Здравствуй,  господин {0.first_name}\nПредлагаю на выбор:".format(message.from_user),parse_mode='html',reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def menu(message):
	if message.chat.type == 'private':
		if message.text == "Просмотреть весь список (~8 минут)":
			bot.send_message(message.chat.id, 'Подожди немного, смотрю...'"\U0001F440")
			if len(parsing1()) > 4096:
				for x in range(0, len(parsing1()), 4096):
					bot.send_message(message.chat.id, (parsing1()[x:x + 4096]))
		if message.text == "Быстрая сводка по ошибкам":
			bot.send_message(message.chat.id, 'Подожди немного, смотрю...'"\U0001F440")
		#	if len(short_report()) > 4096:
			bot.send_message(message.chat.id, (short_report()))
		#	bot.send_message(message.chat.id, '~100 лендов отдают ошибки')
		#	else: bot.send_message(message.chat.id, (short_report()))
		if message.text == "Хочу получать отчет по лендингам c ошибками каждые 5 минут":
			bot.send_message(message.chat.id, 'Выбор принят')
			while True:
				time.sleep(300)
				bot.send_message(message.chat.id, (short_report()))

bot.polling(none_stop=True, interval=0, timeout=123)