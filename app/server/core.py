from __future__ import annotations


from typing import TYPE_CHECKING

from litestar.plugins import InitPluginProtocol

if TYPE_CHECKING:
    from litestar.config.app import AppConfig


class ApplicationCore(InitPluginProtocol):
    def on_app_init(self, app_config: AppConfig) -> AppConfig:
        from app.config import app as config
        from app.server import plugins
        from app.config.base import get_settings
        from app.controllers.web.base import BaseController
        from app.tools.xrequest import XRequest
        from app.database import models as m
        from litestar.static_files import create_static_files_router

        settings = get_settings()

        app_config.debug = settings.app.DEBUG
        app_config.request_class = XRequest
        app_config.template_config = config.template
        app_config.compression_config = config.compression
        app_config.plugins.extend(
            [plugins.alchemy, plugins.reload, plugins.htmx]
        )
        app_config.route_handlers.extend(
            [
                create_static_files_router(
                    path="/static", directories=[settings.app.STATIC_DIR]
                ),
                BaseController,
            ]
        )
        app_config.signature_namespace.update({"m": m})

        return app_config
