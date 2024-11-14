from pydantic import Field, BaseModel


class User(BaseModel):
    username: str = Field(...)
    phone_number: str = Field()


class UserInDb(User):
    hashed_password: str = Field(...)


class TokenModel(BaseModel):
    token: str = Field(...)