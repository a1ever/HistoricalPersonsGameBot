from bot_instructions import *

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
# импорты
from config_reader import config
from services.json_service import GetRandomPerson

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher()


@dp.message(Command(START))
async def cmd_start(message: types.Message):
    pers = await GetRandomPerson()
    await message.answer(f"{pers.Name}: \n {pers.GetRandomFact()}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())