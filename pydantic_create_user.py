from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError



class UserSchema(BaseModel):
    """Данные пользователя"""
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """Cоздание пользователя"""
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """Ответ на запрос о создании пользователя"""
    user: UserSchema