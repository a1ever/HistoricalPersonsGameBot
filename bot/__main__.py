import asyncio
import logging
import os

from aiogram import Bot, Dispatcher

from bot.commands import register_user_commands
from storage.db import create_pool, get_session_maker, proceed_schemas, BaseModel


async def main():
    dp = Dispatcher()
    bot = Bot(token=os.getenv('bot_token'))

    register_user_commands(dp)

    url = f"mysql+aio{os.getenv('db_path')}"

    async_engine = create_pool(url)
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(async_engine, BaseModel.metadata)

    await dp.start_polling(bot, session_maker=session_maker)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())