from pydantic import BaseSettings

from db.database import AsyncDatabaseSession


class DataBase(BaseSettings):
    user: str
    password: str
    host: str
    port: int
    name: str
    async_url: str
    sync_url: str
    # async_session: AsyncDatabaseSession

    @property
    def async_url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    @property
    def sync_url(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    @property
    def async_session(self):
        return AsyncDatabaseSession(self.async_url)


class Settings(BaseSettings):
    db: DataBase


cfg = Settings(db={'user': 'postgres', 'password': 'bezeq123', 'host': 'localhost', 'port': 5432, 'name': 'postgres'})
