from src.models import UserOrm
from src.repositories.base import BaseRepository
from src.schemas.user import CreateUserSchema


class UserRepository(BaseRepository):
    async def create_user(self, create_user: CreateUserSchema):
        async with self._get_session() as session:
            db_user = UserOrm.from_user(create_user)
            session.add(db_user)

            await session.flush()
            await session.refresh(db_user)

            user_response = db_user.to_user()

            return user_response
