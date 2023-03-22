from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')
#FIXME move this config to database, `/` is vhost in localhost//


@app.task
def add(x, y):
    return x + y
