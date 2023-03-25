from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

engine = create_async_engine(
    "postgresql+asyncpg://postgres:123456@localhost:5432/quart",
    echo=True,
)

Session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
session = Session()


from dataclasses import dataclass
#
@dataclass
class User_test:
    id: int
    username : str
    email: str
    full_name : str




class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    username = Column(String(45), nullable=False)
    email = Column(String(80), nullable=False)
    full_name = Column(String(80), nullable=True)


    posts = relationship("Post", backref="author")

    def format(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,

        }

    def __repr__(self):
        return f"<User {self.username}>"


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    content = Column(Text(), nullable=False)
    user_id = Column(Integer(), ForeignKey("users.id"))

    def __repr__(self):
        return f"<User {self.title}>"


class Test(Base):
    __tablename__ = "test"
    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
