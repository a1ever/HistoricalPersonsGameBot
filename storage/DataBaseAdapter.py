from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from storage.FactState import Fact
from storage.db import General, Fact, Quote, GameState


# s = (select()
#      .select_from(General
#                   .join(Fact, General.level_id == Fact.level_id)
#                   .join(Quote, General.level_id == Quote.level_id))
#      )


async def get_personal_info(user_id: int):
    return f"Ты хорош, {user_id}, а статистика в бд)"


async def get_top_info(user_id: int) -> object:
    return f"Ты хорош, {user_id}, а статистика в бд)"


async def get_surrender(user_id: int, session_maker: sessionmaker):
    async with session_maker() as session:
        async with session.begin():
            await session.execute(select(GameState).where(user_id == GameState.uuid).delete())

    return f"Слабый"


async def get_current_fact_state(user_id: int):
    return Fact
