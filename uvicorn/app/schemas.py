from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    password: str


class UserCreate(UserBase):
    pass


class User(UserBase):

    id: int
    username: str

    class Config:
        from_attributes = True

