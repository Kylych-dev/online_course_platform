from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

# задачи для парсинга и сохранения репозиториев
@app.task
def parse_and_save_repositories():
    pass
