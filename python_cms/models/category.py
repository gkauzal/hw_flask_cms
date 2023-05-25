from python_cms.db import BaseModel, db
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import String, Integer


class CategoryModel(BaseModel):
  __tablename__ = "categories"
  id = mapped_column(Integer, primary_key=True, autoincrement=True)
  name = mapped_column(String(80), nullable=False)

  posts = relationship("PostModel", back_populates="categories")

  def __init__(self, name):
    self.name = name

  @classmethod
  def get(cls, id):
    return cls.query.filter_by(id=id).first()

  @classmethod
  def get_all(cls):
    return cls.query.all()

  def save(self):
    db.session.add(self)
    db.session.commit()