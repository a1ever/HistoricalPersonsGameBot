import random

from sqlalchemy import select, insert, func, update, delete
from sqlalchemy.orm import sessionmaker

from storage.Models.game_state_model import GameStateModel
from storage.db import General, Fact, Quote, GameState, User


# s = (select()
#      .select_from(General
#                   .join(Fact, General.level_id == Fact.level_id)
#                   .join(Quote, General.level_id == Quote.level_id))
#      )


async def get_personal_info(user_id: int, session_maker: sessionmaker) -> str:
    async with session_maker() as session:
        async with session.begin():
            random_points = await session.scalar(select(User.random_problems_score).where(User.uuid == user_id))
            campaign_points = await session.scalar(select(User.campaign_score).where(User.uuid == user_id))
            campaign_lv = await session.scalar(select(User.campaign_status).where(User.uuid == user_id))
            return f"Ваш текущий уровень в кампании: {campaign_lv}\nЗа предыдущие уровни вы получили - {campaign_points}\nЗа случайные уровни вы набрали - {random_points}"


async def get_top_info(user_id: int, session_maker: sessionmaker) -> str:
    return f"Секрет"


async def create_new_user(user_id: int, name: str, session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            print(11213)
            res = (await session.scalar(select(func.count()).select_from(User).where(User.uuid == user_id)))
            if res == 0:
                await session.execute(insert(User).values(uuid=user_id, username=name))


async def update_user_in_campaign(user_id: int, status: bool, session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(update(User).where(User.uuid == user_id).values(is_in_campaign=status))


async def update_user_campaign_status(user_id: int, session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            level_amount = (await session.scalar(select(func.count()).select_from(General)))
            current_level = await session.scalar(select(User.campaign_status).where(User.uuid == user_id))
            if current_level < level_amount:
                await session.execute(update(User).where(User.uuid == user_id).values(
                    campaign_status=current_level + 1))
            else:
                await session.execute(update(User).where(User.uuid == user_id).values(
                    campaign_status=1))


async def update_score(user_id: int, score: int, session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            if await session.scalar(select(User.is_in_campaign).where(User.uuid == user_id)):
                await session.execute(update(User).where(User.uuid == user_id)
                                      .values(campaign_score=score + await session.scalar(
                    select(User.campaign_score).where(User.uuid == user_id))))
            else:
                await session.execute(update(User).where(User.uuid == user_id)
                                      .values(random_problems_score=score + await session.scalar(
                    select(User.random_problems_score).where(User.uuid == user_id))))


async def update_current_game_state(game: GameStateModel, session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            return await session.execute(update(GameState).where(game.uuid == GameState.uuid).where(
                game.type_of_game == GameState.type_of_game).values(
                uuid=game.uuid,
                type_of_game=game.type_of_game,
                level_id=game.level_id,
                fact_amount=game.fact_amount,
                age_fact_amount=game.age_fact_amount,
                displayed_country=game.displayed_country,
                displayed_photo=game.displayed_photo,
                displayed_activity=game.displayed_activity,
                quote_amount=game.quote_amount,
                minus_points=game.minus_points,
            ))


async def create_null_game_state(user_id: int, session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            is_in_campaign = (
                await session.scalar(select(User.is_in_campaign).where(User.uuid == user_id)))
            ans = await session.scalar(
                select(GameState).where(user_id == GameState.uuid).where(is_in_campaign == GameState.type_of_game))
            print(1122)
            print(ans)
            if ans is None:
                if is_in_campaign:
                    user = (await session.scalar(select(User).where(user_id == User.uuid)))
                    user: User
                    await session.execute(
                        insert(GameState).values(uuid=user_id, type_of_game=True, level_id=user.campaign_status))
                else:
                    level_amount = (await session.scalar(select(func.count()).select_from(General)))
                    await session.execute(
                        insert(GameState).values(uuid=user_id, type_of_game=False,
                                                 level_id=random.randint(1, level_amount + 1)))


async def get_surrender(user_id: int, session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            type_of_game = await get_campaign_status(user_id, session_maker)
            level = (await session.scalar(
                select(GameState.level_id).where(user_id == GameState.uuid).where(
                    GameState.type_of_game == type_of_game)))
            if type_of_game:
                await update_user_campaign_status(user_id, session_maker)
            ans = await session.scalar(select(General.full_name).where(General.level_id == level))
            await session.execute(
                delete(GameState).where(user_id == GameState.uuid).where(GameState.type_of_game == type_of_game))

    return f"Очков за данный уровень 0. Персонажем был {ans}"


async def delete_game_state(user_id: int, type_of_game: bool, session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(
                delete(GameState).where(user_id == GameState.uuid).where(GameState.type_of_game == type_of_game))


async def get_name(user_id: int, session_maker: sessionmaker) -> str:
    async with session_maker() as session:
        async with session.begin():
            type_of_game = await get_campaign_status(user_id, session_maker)
            level = (await session.scalar(
                select(GameState.level_id).where(user_id == GameState.uuid).where(
                    GameState.type_of_game == type_of_game)))
            if level is None:
                return ""
            return await session.scalar(select(General.full_name).where(General.level_id == level))


async def get_current_game_state(user_id: int, session_maker: sessionmaker) -> GameStateModel:
    async with session_maker() as session:
        async with session.begin():
            type_of_game = await get_campaign_status(user_id, session_maker)
            game_state = (await session.scalar(
                select(GameState).where(user_id == GameState.uuid).where(GameState.type_of_game == type_of_game)))
            model = GameStateModel()
            model.uuid = game_state.uuid
            model.level_id = game_state.level_id
            model.type_of_game = game_state.type_of_game
            model.fact_amount = game_state.fact_amount
            model.age_fact_amount = game_state.age_fact_amount
            model.displayed_photo = game_state.displayed_photo
            model.displayed_country = game_state.displayed_country
            model.displayed_activity = game_state.displayed_activity
            model.quote_amount = game_state.quote_amount
            model.minus_points = game_state.minus_points

            return model


async def get_campaign_status(user_id: int, session_maker: sessionmaker) -> bool:
    async with session_maker() as session:
        async with session.begin():
            return await session.scalar(select(User.is_in_campaign).where(User.uuid == user_id))


async def output_game_state(user_id: int, session_maker: sessionmaker, previous_msg="") -> [str, str]:
    async with session_maker() as session:
        async with session.begin():
            type_of_game = await get_campaign_status(user_id, session_maker)
            game_state = (await session.scalar(
                select(GameState).where(user_id == GameState.uuid).where(GameState.type_of_game == type_of_game)))
            ans = ("Случайный\n", "Кампания\n")[type_of_game]
            if type_of_game:
                ans += f"Уровень {game_state.level_id} "
            ans += f"Очков: {120 - game_state.minus_points}\n"
            general = (await session.scalar(select(General).where(General.level_id == game_state.level_id)))
            facts = (await session.scalar(select(Fact).where(Fact.level_id == game_state.level_id)))
            facts: Fact
            quotes = (await session.scalar(select(Quote).where(Quote.level_id == game_state.level_id)))
            quotes: Quote
            ans += facts.get_facts(game_state.fact_amount)
            ans += quotes.get_quotes(game_state.quote_amount)
            ans += general.get_age_fact(game_state.age_fact_amount)
            if game_state.displayed_activity:
                ans += "Активность:" + general.activity + "\n"
            if game_state.displayed_country:
                ans += "Страна:" + general.country + "\n"
            if not game_state.displayed_photo:
                link = "https://cdn.fishki.net/upload/post/2021/08/30/3909511/1f21cb369a625b5f1ff2040161ed2d6d.jpg"
            else:
                general = (
                    await session.scalar(select(General).where(General.level_id == game_state.level_id)))
                link = general.link_to_photo
            return [ans, link]
