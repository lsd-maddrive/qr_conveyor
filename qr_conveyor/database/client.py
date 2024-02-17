import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, sessionmaker


class DatabaseClient:
    def __init__(self):
        # Создаем приватный объект логгера
        self._logger = logging.getLogger(__name__)

        # Загружаем переменные окружения из файла .env
        load_dotenv()

        # Проверяем наличие переменной окружения DB_DPATH
        db_dpath = os.getenv("DB_DPATH")
        if db_dpath is None:
            raise ValueError("Переменная окружения DB_DPATH не определена в файле .env")

        # Проверяем, существует ли папка для БД, и создаем ее, если необходимо
        if not os.path.exists(db_dpath):
            os.makedirs(db_dpath)

        # Создаем переменную с путем до файла БД
        self.db_path = os.path.join(db_dpath, "data.db")

        # Создаем объект движка SQLAlchemy
        self.engine = create_engine("sqlite:///" + self.db_path)

        # Создаем объект сессии
        self._session = sessionmaker(bind=self.engine)
