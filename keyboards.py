from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопка геолокации
location_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
location_keyboard.add(KeyboardButton('Моя геолокация', request_location=True))

# Меню с выбором дня прогноза
period_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
period_buttons = ['/Сегодня', '/Завтра']
period_keyboard.row(*period_buttons)
period_keyboard.row('/Отмена')

# В начало
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_keyboard.add(KeyboardButton('/start'))
