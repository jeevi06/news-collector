# app/models.py
from sqlalchemy import create_engine, Column, String, DateTime, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import timezone,datetime

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String(255),nullable=False)
    content = Column(Text,nullable=False)
    pub_date = Column(DateTime(timezone=timezone.utc), default=datetime.utcnow)
    source_url = Column(String(255),nullable=False,unique=True)
    category = Column(String(50))  # Adjust the length based on your categories

# MySQL connection string
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/newsarticle"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


