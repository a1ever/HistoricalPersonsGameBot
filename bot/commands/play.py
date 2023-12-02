from aiogram import types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from aiogram.utils.keyboard import (
    InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
)


async def command_play(message : types.Message):
    play_markup = InlineKeyboardBuilder()
    play_markup.button(
        text="Угадать",
        switch_inline_query_current_chat="guess",
    )
    await message.answer('Игра', reply_markup=play_markup.as_markup(resize_keyboard=True))


async def command_answer(inline_query: types.InlineQuery) -> None:
    res = [InlineQueryResultArticle(id="qpwind",
        title="Попытка",
        input_message_content=InputTextMessageContent(
           message_text="Хорошая попытка"
        ),
                                    )]

    await inline_query.answer(results=res, is_personal=True)

