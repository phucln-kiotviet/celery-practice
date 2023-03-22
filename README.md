# Celery practice

- My first practice about celery from this official [getting started](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html)

## Another solution

- Check this with [socketserver](https://stackoverflow.com/questions/35341959/best-practice-for-communication-between-server-and-background-processes) in python

## RabbitMQ

- Docker:
```
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9.29-management
```

## Run first Celery worker server

- Command:
```
celery -A tasks worker --loglevel=INFO
```