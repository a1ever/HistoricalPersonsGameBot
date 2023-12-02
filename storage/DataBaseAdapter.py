from storage.FactState import Fact


async def get_personal_info(user_id: int):
    return f"Ты хорош, {user_id}, а статистика в бд)"


async def get_top_info(user_id: int):
    return f"Ты хорош, {user_id}, а статистика в бд)"

async def get_surrender(user_id: int):
    return f"Слабый"

async def get_current_fact_state(user_id: int):
    return Fact