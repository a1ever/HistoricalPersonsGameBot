import asyncio
import logging
import os

import numpy
from aiogram import Bot, Dispatcher

from bot.commands import register_user_commands
from storage.db import create_pool, get_session_maker, proceed_schemas, BaseModel


async def main():
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()
    bot = Bot(token=os.getenv('bot_token'))

    register_user_commands(dp)

    async_engine = create_pool(f"sqlite+aiosqlite:///{os.getenv('db_path')}")
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(async_engine, BaseModel.metadata)

    await dp.start_polling(bot, session_maker=session_maker)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
