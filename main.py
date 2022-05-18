import logging
from aiogram import executor
from handlers import FSMhandlers
from create_bot import dp


logging.basicConfig(level=logging.INFO)

FSMhandlers.register_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
