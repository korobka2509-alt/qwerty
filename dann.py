class User(Base):
    tablename = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    tokens = relationship("Token", back_populates="user")
    articles = relationship("Article", back_populates="author")


class Token(Base):
    tablename = "tokens"

    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tokens")


class Category(Base):
    tablename = "categories"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    articles = relationship("Article", back_populates="category")


class Article(Base):
    tablename = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    is_approved = Column(Boolean, default=False)

    author_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    author = relationship("User", back_populates="articles")
    category = relationship("Category", back_populates="articles")
