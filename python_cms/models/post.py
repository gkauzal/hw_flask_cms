from sqlalchemy import String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import mapped_column, relationship
from python_cms.db import BaseModel, db
from python_cms.models.category import CategoryModel


class PostModel(BaseModel):
  id = mapped_column(Integer, primary_key=True, autoincrement=True)
  title = mapped_column(String(80), nullable=False)
  teaser_image = mapped_column(String(80), nullable=False)
  body = mapped_column(String(8000), nullable=False)
  author_id = mapped_column(String(80), ForeignKey("users.id"), nullable=False)
  promoted = mapped_column(Boolean(), nullable=False)
  category_id = mapped_column(Integer,
                              ForeignKey("categories.id"),
                              nullable=False)

  author = relationship("UserModel", back_populates="posts")
  categories = relationship("CategoryModel", back_populates="posts")

  def __init__(self, title, body, user_id, teaser_image, promoted,
               category_id):
    self.title = title
    self.body = body
    self.author_id = user_id
    self.teaser_image = teaser_image
    self.promoted = promoted
    self.category_id = category_id

  @classmethod
  def get(cls, post_id):
    return cls.query.filter_by(id=post_id).first()

  @classmethod
  def get_all(cls):
    return cls.query.all()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()