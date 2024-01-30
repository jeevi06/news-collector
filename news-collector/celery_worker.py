# celery_worker.py
from app.tasks import app

if __name__ == '__main__':
    app.worker_main(['-l', 'info'])