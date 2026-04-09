from app.db.models.base_model import BaseModel

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(BaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)