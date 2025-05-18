from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Type

from environs import Env

PROJECT_DIR = Path(__file__).parent.parent.parent
APP_DIR = PROJECT_DIR / "app"


_env = Env()


def env(type: Type | str, name: str, default: Any = ..., **kwargs):
    return field(
        default_factory=lambda: getattr(
            _env, type if isinstance(type, str) else type.__name__
        )(name, default, **kwargs),
    )


@dataclass
class AppSettings:
    DEBUG: bool = env(bool, "DEBUG", False)
    STATIC_DIR: Path = PROJECT_DIR / "static"
    TEMPLATES_DIR = APP_DIR / "templates"


@dataclass
class DatabaseSettings:
    url: str = env(str, "DATABASE_URL", "sqlite+aiosqlite:///db.sqlite3")
    echo: bool = env(bool, "ECHO", False)
    MIGRATION_DIR: str = str(APP_DIR / "database/migrations")
    MIGRATION_CONFIG: str = str(APP_DIR / "database/migrations/alembic.ini")


@dataclass
class Settings:
    app: AppSettings = field(default_factory=AppSettings)
    db: DatabaseSettings = field(default_factory=DatabaseSettings)


@lru_cache(maxsize=1, typed=True)
def get_settings() -> Settings:
    return Settings()
