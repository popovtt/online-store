from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str | None = None
    disabled: bool = False
    hashed_password: str = None


class CreateUserSchema(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    disabled: bool = False
    password: str = None


class UpdateUserSchema(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    hashed_password: str


class UserOutSchema(CreateUserSchema):
    username: str
    email: EmailStr
    full_name: str | None = None
    disabled: bool = False
