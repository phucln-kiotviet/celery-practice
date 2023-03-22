# Celery practice

- My first practice about celery from this official [getting started](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html)



## RabbitMQ

- Docker:
```
docker run -d --name rabbitmq -p 5672:5672 rabbitmq:3.9.29-management
```

## Run first Celery worker server

- Command:
```
celery -A tasks worker --loglevel=INFO
```