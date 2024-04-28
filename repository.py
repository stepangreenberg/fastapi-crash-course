from typing import List

from database import new_session, TasksOrm
from sqlalchemy import select

from schemas import STask


class TaskRepository:
    from schemas import STaskAdd

    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TasksOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TasksOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return tasks_schemas
