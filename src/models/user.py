from pydantic import EmailStr
from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models import Base
from src.schemas.user import CreateUserSchema, UserBaseSchema, UserOutSchema


class UserOrm(Base):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[EmailStr] = mapped_column(String, unique=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=True)
    disabled: Mapped[bool] = mapped_column(Boolean, nullable=True)
    hashed_password: Mapped[str] = mapped_column(String(50))

    def to_user(self) -> UserBaseSchema:
        return UserBaseSchema.model_validate(self)

    def to_public_user(self) -> UserOutSchema:
        return UserOutSchema.model_validate(self)

    @classmethod
    def from_user(cls, user: CreateUserSchema) -> "UserOrm":
        return UserOrm(
            **user.model_dump(),
        )
