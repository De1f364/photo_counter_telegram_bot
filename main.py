#!/usr/bin/env
# By ch3rrydrunk <@ch3rrydrunk>
# Built with grace on python-telegram-bot
import logging as log
import os

from telegram import *
from telegram.ext import *
from telegram.ext import CommandHandler as CMH 
from telegram.ext import MessageHandler as MSH

from imageai.Detection import ObjectDetection
import os
import os.path

"""for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    """

####### SETTINGS #######
#~~~~~~~ Logging ~~~~~~#
log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=log.INFO)
logger = log.getLogger(__name__)

#~~~~~~~ ImageAI ~~~~~~#
execution_path = os.getcwd()

######### LOGICS ########
#~~~~~~~ Commands ~~~~~~#


def start(update, context):
	update.message.reply_text("Выберите кого/что хотите посчитать?",
								reply_markup=choice_menu_markup())
	return CHOICE


def start_human(update, context):
	query = update.callback_query
	query.edit_message_text("Сколько примерно человек будет на вашем фото?",
								reply_markup=start_menu_markup())
	return MAIN_HUMAN


def start_ship(update, context):
	query = update.callback_query
	query.edit_message_text("Сколько примерно овец будет на вашем фото?",
								reply_markup=start_menu_sheep())
	return MAIN_SHEEP


def first_menu(update, context):
	query = update.callback_query
	query.edit_message_text(
		text="Начнем?\n"
								"Просто сфотографируй группу,"
								"чтобы быстро посчитать количество человек!\n"
	)
	return MENU


def second_menu(update, context):
	query = update.callback_query
	query.edit_message_text(
		text="Начнем?\n"
			 "Просто сфотографируй группу,"
			 "чтобы быстро посчитать количество человек!\n"
	)
	return MENU_10


def third_menu(update, context):
	query = update.callback_query
	query.edit_message_text(
		text="Начнем?\n"
			 "Просто сфотографируй группу,"
			 "чтобы быстро посчитать количество человек!\n"
	)
	return MENU_50


def first_menu_sheep(update, context):
	query = update.callback_query
	query.edit_message_text(
		text="Начнем?\n"
								"Просто сфотографируй группу,"
								"чтобы быстро посчитать количество овец!\n"
	)
	return MENU_SHEEP


def second_menu_sheep(update, context):
	query = update.callback_query
	query.edit_message_text(
		text="Начнем?\n"
			 "Просто сфотографируй группу,"
			 "чтобы быстро посчитать количество овец!\n"
	)
	return MENU_10_SHEEP


def third_menu_sheep(update, context):
	query = update.callback_query
	query.edit_message_text(
		text="Начнем?\n"
			 "Просто сфотографируй группу,"
			 "чтобы быстро посчитать количество овец!\n"
	)
	return MENU_50_SHEEP

def help(update, context):
	update.message.reply_text("Серьезно? :)\n"
								"Просто присылай фото "
								"или набери '/start' для перезагрузки!",
								reply_markup=markup)
	return MAIN_HUMAN


#~~~~~~~~ Functions ~~~~~~~#

def count_x(update, context):
	image_id = update.message.photo[-1]
	image = bot_core.bot.get_file(image_id)
	image.download('img.jpg')
	while True:
		if os.path.isfile("img.jpg") == True:
			break
	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel()
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "img.jpg"), output_image_path=os.path.join(execution_path , "imgnew.jpg"), minimum_percentage_probability = 50)
	file = open('imgnew.jpg', 'rb')
	i = 0
	for each in detections:
		if (each["name"] == "person" and each["percentage_probability"] > 50):
			i += 1
	update.message.reply_text("На фото - {} объектов\n".format(i),
								reply_markup=markup)
	update.message.reply_photo(file)
	return MAIN_HUMAN


def count_x_10(update, context):
	image_id = update.message.photo[-1]
	image = bot_core.bot.get_file(image_id)
	image.download('img.jpg')
	while True:
		if os.path.isfile("img.jpg") == True:
			break
	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel()
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "img.jpg"), output_image_path=os.path.join(execution_path , "imgnew.jpg"), minimum_percentage_probability = 40)
	file = open('imgnew.jpg', 'rb')
	i = 0
	for each in detections:
		if (each["name"] == "person" and each["percentage_probability"] > 40):
			i += 1
	update.message.reply_text("На фото - {} объектов\n".format(i),
								reply_markup=markup)
	update.message.reply_photo(file)
	return MAIN_HUMAN


def count_x_100(update, context):
	image_id = update.message.photo[-1]
	image = bot_core.bot.get_file(image_id)
	image.download('img.jpg')
	while True:
		if os.path.isfile("img.jpg") == True:
			break
	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel()
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "img.jpg"), output_image_path=os.path.join(execution_path , "imgnew.jpg"), minimum_percentage_probability = 10)
	file = open('imgnew.jpg', 'rb')
	i = 0
	for each in detections:
		if (each["name"] == "person" and each["percentage_probability"] > 10):
			i += 1
	update.message.reply_text("На фото - {} объектов\n".format(i),
								reply_markup=markup)
	update.message.reply_photo(file)
	return MAIN_HUMAN


def count_x_sheep(update, context):
	image_id = update.message.photo[-1]
	image = bot_core.bot.get_file(image_id)
	image.download('img.jpg')
	while True:
		if os.path.isfile("img.jpg") == True:
			break
	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel()
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "img.jpg"), output_image_path=os.path.join(execution_path , "imgnew.jpg"), minimum_percentage_probability = 56)
	file = open('imgnew.jpg', 'rb')
	i = 0
	for each in detections:
		if (each["name"] == "sheep" and each["percentage_probability"] > 56):
			i += 1
	update.message.reply_text("На фото - {} объектов\n".format(i),
								reply_markup=markup)
	update.message.reply_photo(file)
	return MAIN_SHEEP


def count_x_10_sheep(update, context):
	image_id = update.message.photo[-1]
	image = bot_core.bot.get_file(image_id)
	image.download('img.jpg')
	while True:
		if os.path.isfile("img.jpg") == True:
			break
	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel()
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "img.jpg"), output_image_path=os.path.join(execution_path , "imgnew.jpg"), minimum_percentage_probability = 40)
	file = open('imgnew.jpg', 'rb')
	i = 0
	for each in detections:
		if (each["name"] == "sheep" and each["percentage_probability"] > 40):
			i += 1
	update.message.reply_text("На фото - {} объектов\n".format(i),
								reply_markup=markup)
	update.message.reply_photo(file)
	return MAIN_SHEEP


def count_x_100_sheep(update, context):
	image_id = update.message.photo[-1]
	image = bot_core.bot.get_file(image_id)
	image.download('img.jpg')
	while True:
		if os.path.isfile("img.jpg") == True:
			break
	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel()
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "img.jpg"), output_image_path=os.path.join(execution_path , "imgnew.jpg"), minimum_percentage_probability = 10)
	file = open('imgnew.jpg', 'rb')
	i = 0
	for each in detections:
		if (each["name"] == "sheep" and each["percentage_probability"] > 10):
			i += 1
	update.message.reply_text("На фото - {} объектов\n".format(i),
								reply_markup=markup)
	update.message.reply_photo(file)
	return MAIN_SHEEP


def to_contact(update, context):
	update.message.reply_text("Сделано с любовью командой RAW OCV\n"
								"Исходный код проекта доступен по ссылке:\n"
								"https://github.com/ch3rrydrunk/countX.git\n"
								"Спасибо, что вы с нами!",
								reply_markup=markup)
	return MAIN_HUMAN


def cancel(update, context):
	logger.info(str(update))
	user = update.message.from_user
	logger.info("User %s canceled the conversation.", user.first_name)
	update.message.reply_text('До свидания! Наберите /start, чтобы попробовать еще раз!',
								reply_markup=ReplyKeyboardRemove())

	return ConversationHandler.END



def error(update, context):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, context.error)

####### REPLY_MARKUP #######

def choice_menu_markup():
	keyboard = [[InlineKeyboardButton('1⃣ Люди', callback_data='m1')],
				[InlineKeyboardButton('2⃣ Овцы', callback_data='m2')],]
	return InlineKeyboardMarkup(keyboard)


def start_menu_markup():
	keyboard = [[InlineKeyboardButton('1⃣ До 10 человек', callback_data='m1_1')],
				[InlineKeyboardButton('2⃣ До 50 человек', callback_data='m1_2')],
				[InlineKeyboardButton('3⃣ Больше 50 человек', callback_data='m1_3')]]
	return InlineKeyboardMarkup(keyboard)


def start_menu_sheep():
	keyboard = [[InlineKeyboardButton('1⃣ До 10 овец', callback_data='m2_1')],
				[InlineKeyboardButton('2⃣ До 50 овец', callback_data='m2_2')],
				[InlineKeyboardButton('3⃣ Больше 50 овец', callback_data='m2_3')]]
	return InlineKeyboardMarkup(keyboard)


####### IGNITION #######
# To set API token set env variable (do "export BOT_API_TOKEN=your_token")
TOKEN = os.getenv("BOT_API_TOKEN")
bot_core = Updater(TOKEN, use_context=True)
bot = bot_core.dispatcher

#======= LOGICS =======#

#˜˜˜˜˜˜  KEYMAP  ˜˜˜˜˜˜#
reply_keyboard = [['📲 Свяжись с нами! 📲']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

#˜˜˜˜˜˜  MANAGER ˜˜˜˜˜˜#
MENU, MENU_10, MENU_50, MENU_SHEEP, MENU_10_SHEEP, MENU_50_SHEEP, CHOICE, MAIN_HUMAN, MAIN_SHEEP = range(9)

conv_handler = ConversationHandler(
	entry_points=[CMH('start', start)],

	states={
		MENU:	[MSH(Filters.regex('^📲 Свяжись с нами! 📲$'), to_contact),
					MSH(Filters.photo, count_x)],

		MENU_10: [MSH(Filters.regex('^📲 Свяжись с нами! 📲$'), to_contact),
					MSH(Filters.photo, count_x_10)],

		MENU_50: [MSH(Filters.regex('^📲 Свяжись с нами! 📲$'), to_contact),
					MSH(Filters.photo, count_x_100)],

		MENU_SHEEP:	[MSH(Filters.regex('^📲 Свяжись с нами! 📲$'), to_contact),
					MSH(Filters.photo, count_x_sheep)],

		MENU_10_SHEEP: [MSH(Filters.regex('^📲 Свяжись с нами! 📲$'), to_contact),
					MSH(Filters.photo, count_x_10_sheep)],

		MENU_50_SHEEP: [MSH(Filters.regex('^📲 Свяжись с нами! 📲$'), to_contact),
					MSH(Filters.photo, count_x_100_sheep)],


		CHOICE:	[CallbackQueryHandler(start_human, pattern='m1'),
					CallbackQueryHandler(start_ship, pattern='m2')],


		MAIN_HUMAN:	[CallbackQueryHandler(first_menu, pattern='m1_1'),
					CallbackQueryHandler(second_menu, pattern='m1_2'),
					CallbackQueryHandler(third_menu, pattern='m1_3')],

		MAIN_SHEEP:	[CallbackQueryHandler(first_menu_sheep, pattern='m2_1'),
					CallbackQueryHandler(second_menu_sheep, pattern='m2_2'),
					CallbackQueryHandler(third_menu_sheep, pattern='m2_3')],
	},
	fallbacks=[CMH('cancel', cancel)]
	)
bot.add_handler(conv_handler)
#Extra Commands

#Errors
bot.add_error_handler(error)

#˜˜˜˜˜˜ Gogogo ˜˜˜˜˜˜#
bot_core.start_polling()
bot_core.idle()
