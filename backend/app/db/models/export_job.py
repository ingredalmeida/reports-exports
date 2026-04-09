from app.db.models.base_model import BaseModel

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

class ExportJob(BaseModel):
    __tablename__ = "export_jobs"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    type: Mapped[str] = mapped_column(String(30), nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False)
    file_path: Mapped[str | None] = mapped_column(String(225), nullable=True)
    error_message: Mapped[str | None] = mapped_column(String(225), nullable=True)