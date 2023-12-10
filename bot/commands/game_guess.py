from aiogram import types
from sqlalchemy.orm import sessionmaker

from bot.commands.keyboards.bot_keyboards import generate_round_keyboard, get_game_keyboard
from storage.DataBaseAdapter import get_name, output_game_state, get_current_game_state, update_score, \
    update_user_campaign_status, delete_game_state


async def message_guess(message: types.Message, session_maker: sessionmaker):
    print(message.text)
    guess = message.text
    words = guess.split()
    if len(words) > 2:
        return await message.answer("В сообщении может быть максимум 2 слова.\nВозможные ответы: [Фамилия] или [Имя], или [Фамилия][пробел][Имя] персонажа.")
    answer = await get_name(message.from_user.id, session_maker)
    if len(words) == 2 and words[0] in answer and words[1] in answer or guess in answer:
        game = await get_current_game_state(message.from_user.id, session_maker)
        points = 120 - game.minus_points
        await update_score(message.from_user.id, points, session_maker)
        await update_user_campaign_status(message.from_user.id, session_maker)
        await delete_game_state(message.from_user.id, game.type_of_game, session_maker)
        await message.answer(text=f"Победа!\n Очков за уровень: {points}", reply_markup=get_game_keyboard())
    elif answer == "":
        return
    else:
        ans = await output_game_state(message.from_user.id, session_maker)
        await message.answer(text="Не верный ответ!\n"+ans[0], reply_markup=await generate_round_keyboard(message.from_user.id,
                                                                                                 session_maker))