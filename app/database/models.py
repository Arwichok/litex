from advanced_alchemy.base import UUIDv7AuditBase

from sqlalchemy.orm import Mapped, mapped_column



class User(UUIDv7AuditBase):
    
    name: Mapped[str] = mapped_column(nullable=False)
