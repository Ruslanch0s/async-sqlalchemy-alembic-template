from pydantic import BaseSettings


class DataBase(BaseSettings):
    user: str
    password: str
    host: str
    port: int
    name: str
    url: str

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Settings(BaseSettings):
    db: DataBase


cfg = Settings(db={'user': 'postgres', 'password': 'bezeq123', 'host': 'localhost', 'port': 5432, 'name': 'postgres'})
