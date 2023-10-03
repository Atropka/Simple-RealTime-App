# Simple-RealTime-App

Это простое приложение с изменением данных в реальном времени с использованием websocket, redis

_____
### Запуск приложения
1)	daphne jokes_project.asgi:application

2)	запустить redis-sever
3)	celery -A jokes_project beat -l INFO
4)	celery -A jokes_project worker -l info -P eventlet
5)	Приложение должно корректно работать
