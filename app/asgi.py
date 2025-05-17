from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from litestar import Litestar


def create_app() -> Litestar:
    from litestar import Litestar
    from app.components.core import BuilderApp
    
    return Litestar(plugins=[BuilderApp()])
