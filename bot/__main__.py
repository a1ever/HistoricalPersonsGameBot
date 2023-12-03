import os

import asyncio
import logging
from aiogram import Bot, Dispatcher
from sqlalchemy import URL

from bot.commands import register_user_commands

from storage.db import create_engine, get_session_maker, proceed_schemas, BaseModel


async def main():
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()
    bot = Bot(token=os.getenv('bot_token'))

    register_user_commands(dp)

    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=os.getenv("db_user"),
        # password="", TODO
        host="localhost",
        port=os.getenv("db_port"),
        database=os.getenv("db_name")
    )

    async_engine = create_engine(postgres_url)
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(async_engine, BaseModel.metadata)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
