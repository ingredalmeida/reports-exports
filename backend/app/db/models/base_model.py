from app.db.base import Base
from app.db.mixins import IdMixin, TimestampMixin

class BaseModel(Base, IdMixin, TimestampMixin):
    __abstract__ = True