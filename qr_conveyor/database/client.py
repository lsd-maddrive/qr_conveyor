import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, sessionmaker


class DatabaseClient:
    def __init__(self):
        # Создаем приватный объект логгера
        self._logger = logging.getLogger(__name__)

        # Загружаем переменные окружения из файла .env
        load_dotenv(override=True)

        # Проверяем наличие переменной окружения DB_DPATH
        db_dpath = os.getenv("DB_DPATH")
        if db_dpath is None:
            raise ValueError("Переменная окружения DB_DPATH не определена в файле .env")

        # Переписываем проверку существования папки через pathlib
        db_path = Path(db_dpath)
        if not db_path.exists():
            db_path.mkdir(parents=True)

        # Создаем переменную с путем до файла БД
        self.db_path = db_path / "data.db"

        # Создаем объект движка SQLAlchemy через f-string
        self.engine = create_engine(f"sqlite:///{self.db_path}")

        # Создаем объект сессии
        self._session = sessionmaker(bind=self.engine)
