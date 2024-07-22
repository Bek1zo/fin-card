"""Debug setting."""
from app.tools.setting import BaseConfig


class DevConfig(BaseConfig):
    """Development configuration."""

    DB_URI = "postgresql+psycopg2://postgres:12345678@127.0.0.1:5432/fin-card"

    SWAGGER = {
        "swagger": "2.0",
        "info": {
            "title": "Учет карт денежного довольствия",
            "description": "Модуль учета денежного довольствия",
            "version": "1.0.0",
        },
        "schemes": [
            "http"
        ]
    }