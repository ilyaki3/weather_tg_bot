from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

location_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
location_keyboard.add(KeyboardButton('Моя геолокация', request_location=True))

period_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
period_buttons = ['/Сегодня', '/Завтра']
period_keyboard.row(*period_buttons)
period_keyboard.row('/Начать_заново')
