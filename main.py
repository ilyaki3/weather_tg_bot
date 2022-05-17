from config import TOKEN, API_TOKEN
import keyboards as kb
import logging
from weather import get_today_weather
from aiogram import Bot, types, Dispatcher, executor

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start', 'Начать_заново'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Привет, {message.from_user.first_name}! В каком городе узнать погоду?\n"
                           "Введите город или отправьте свою геолокацию", reply_markup=kb.location_keyboard)


@dp.message_handler(content_types=['location'])
async def set_location(message: types.Message):
    global location
    location = message['location']
    await bot.send_message(message.from_user.id, 'Прогноз на какое время?', reply_markup=kb.period_keyboard)


@dp.message_handler(commands=['Сегодня', 'Завтра', 'На 5 дней'])
async def set_period(message: types.Message):
    global period
    period = message.text
    await bot.send_message(message.from_user.id, get_today_weather(location, period, API_TOKEN))

#
# @dp.message_handler()
# async def set_city(message: types.Message):
#     global city
#     city = message.text
#     await bot.send_message(message.from_user.id, 'Прогноз на какое время?', reply_markup=kb.period_keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
