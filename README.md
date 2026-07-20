Тестовое задание: Python backend за nginx reverse proxy в Docker.

## Как запустить

```
git clone [https://github.com/PlayerJr/Stackbridge_Test].git
cd effective_mobile_test
docker compose up -d
```

## Как проверить

```
curl http://localhost
```

Ожидаемый ответ:

```
Hello from Effective Mobile!
```

## Как работает

```
Client → nginx:80 → backend:8080
```

nginx принимает запросы на порт 80 и проксирует их на Python HTTP-сервер внутри docker-сети `internal`. Backend наружу не публикуется, доступ к нему только у nginx.

## Стек

- Python 3.12-slim
- nginx 1.25-alpine
- Docker Compose

## Troubleshooting

**`curl http://localhost` не отвечает**
Проверьте, что оба контейнера запущены и backend прошёл healthcheck:
```
docker compose ps
```
Если `em_backend` не в статусе `healthy`, посмотрите логи:
```
docker compose logs backend
```

**Порт 80 занят**
Освободите порт или измените проброс в `docker-compose.yml` на `"8080:80"` и обращайтесь на `http://localhost:8080`.

**Изменения в nginx.conf не применяются**
Конфиг копируется в образ на этапе сборки, а не через volume, поэтому нужен пересбор:
```
docker compose up -d --build
```
