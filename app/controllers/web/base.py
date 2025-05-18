from litestar import (
    Controller,
    get,
)
from litestar.response import Template

from app.tools.xrequest import XRequest


class BaseController(Controller):
    path = "/"

    @get("/")
    async def index(self, request: XRequest) -> Template:
        return request.template("index.html.j2")
