# Alembic

- Add new models to __init__ !

- Run from root dir!

### Make migrations
    alembic revision --autogenerate -m "migration name"
### Migrate
    alembic upgrade head
