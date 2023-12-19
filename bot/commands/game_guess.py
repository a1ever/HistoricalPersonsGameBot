from aiogram import types
from aiogram.types import URLInputFile
from sqlalchemy.orm import sessionmaker

from bot.commands.keyboards.bot_keyboards import generate_round_keyboard, get_game_keyboard
from storage.DataBaseAdapter import get_name, output_game_state, get_current_game_state, update_score, \
    update_user_campaign_status, delete_game_state, update_current_game_state


async def message_guess(message: types.Message, session_maker: sessionmaker):
    guess = message.text.lower()
    words = guess.split()
    if len(words) > 2:
        return await message.answer("В сообщении может быть максимум 2 слова.\n"
                                    "Возможные ответы: [Фамилия] или [Имя], или [Фамилия][пробел][Имя] персонажа.")
    answer = await get_name(message.from_user.id, session_maker)
    answer = answer.lower()
    answers = answer.split()
    if (len(words) == 2 and words[0] == answers[0] and words[1] == answers[1]) or (len(words) == 2 and words[1] == answers[0] and words[0] == answers[1]) or (guess == answers[0]) or (guess == answers[1]):
        game = await get_current_game_state(message.from_user.id, session_maker)
        points = 125 - game.minus_points
        await update_score(message.from_user.id, points, session_maker)
        await update_user_campaign_status(message.from_user.id, session_maker)
        await delete_game_state(message.from_user.id, game.type_of_game, session_maker)
        await message.answer(text=f"Победа!\nОчков за уровень: {points}",
                             reply_markup=await get_game_keyboard(message.from_user.id, session_maker))
    elif answer == "":
        return await message.answer("В сообщении может быть максимум 2 слова.\n"
                                    "Возможные ответы: [Фамилия] или [Имя], или [Фамилия][пробел][Имя] персонажа.")
    elif "/hax" in guess:
        state = await get_current_game_state(message.from_user.id, session_maker)
        await update_current_game_state(state.addMinus(-2), session_maker)
        ans = await output_game_state(message.from_user.id, session_maker)
        await message.answer(text="Читы сработали!\n - -2 балла!\n\n" + ans[0],
                             reply_markup=await generate_round_keyboard(message.from_user.id, session_maker))
    elif "бо" == guess:
        await message.answer_photo(photo=URLInputFile("https://sun9-13.userapi.com/impg/gajo20WIwQblT2tTVnBLPyAJBtFjdQ2QmXd21g/-zYZ4exYFtY.jpg?size=890x980&quality=95&sign=da9e811d067077da014d49981834a1fe&type=album"),caption="Есть такой")
    elif "велоспорт" == guess:
        await message.answer_photo(photo=URLInputFile("https://sun9-40.userapi.com/impg/z4YNLsZ9YrQ7NfBaI6BAO8k7W0CG6GO-V0d8Jw/2yI45ejFLnw.jpg?size=807x807&quality=95&sign=0aac49467f88d3090c94460d96d87311&c_uniq_tag=UzP0zIBRYaZZrcosE38eTEnLv9wmP0ieSy357ctoMAk&type=album"),caption="Есть такой")
    else:
        state = await get_current_game_state(message.from_user.id, session_maker)
        await update_current_game_state(state.addMinus(2), session_maker)
        ans = await output_game_state(message.from_user.id, session_maker)
        await message.answer(text="Неверный ответ!\n -2 баллa!\n\n"+ans[0],
                             reply_markup=await generate_round_keyboard(message.from_user.id, session_maker))
