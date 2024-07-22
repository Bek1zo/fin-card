"""Debug setting."""

from app.tools.setting import BaseConfig


class ProdConfig(BaseConfig):
    """Production configuration."""

    DB_URI = "postgresql+psycopg2://{}@site.ru/fincard?gssencmode=disable"

