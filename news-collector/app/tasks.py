# app/tasks.py
from celery import Celery
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Celery(
    'tasks',
    broker='sqla+mysql://root:root@localhost/newsarticle?charset=utf8mb4',  
    backend='db+mysql://root:root@localhost/newsarticle?charset=utf8mb4',
    broker_connection_retry_on_startup=True,
)

# SQLAlchemy configuration
engine = create_engine('mysql://root:root@localhost/newsarticle?charset=utf8mb4')
Session = sessionmaker(bind=engine)

# Additional configuration if needed
app.conf.update(
    result_backend='db+mysql://root:root@localhost/newsarticle?charset=utf8mb4',
    result_serializer='json',
)
