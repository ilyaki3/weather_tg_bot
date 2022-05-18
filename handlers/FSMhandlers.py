from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import keyboards as kb
from config import API_TOKEN
from create_bot import bot
from weather import get_weather


class FsmHandlers(StatesGroup):
    location = State()
    period = State()


async def start_command(message: types.Message):
    await FsmHandlers.location.set()
    await bot.send_message(message.from_user.id,
                           f"Привет, {message.from_user.first_name}! В каком городе узнать погоду?\n"
                           "Отправьте свою геолокацию", reply_markup=kb.location_keyboard)


async def set_location(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['location'] = message['location']
        await FsmHandlers.next()
        await bot.send_message(message.from_user.id, 'Прогноз на какое время?', reply_markup=kb.period_keyboard)


async def set_period(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['period'] = message.text
        await bot.send_message(message.from_user.id,
                               get_weather(data['location'], data['period'], API_TOKEN), reply_markup=kb.start_keyboard)
    await state.finish()


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.from_user.id, 'Отменено', reply_markup=kb.start_keyboard)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'], state=None)
    dp.register_message_handler(set_location, content_types=['location'], state=FsmHandlers.location)
    dp.register_message_handler(set_period, commands=['Сегодня', 'Завтра'], state=FsmHandlers.period)
    dp.register_message_handler(cancel_handler, state='*', commands='Отмена')
