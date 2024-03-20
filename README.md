# Проект Test

Простейшая API не включает в себя пермишены, индексацию таблиц

## Запуск проекта

Для запуска проекта выполните следующие шаги:

```bash
docker-compose build && \
docker-compose up -d && \
docker exec -it test_full_dev_web_1 bash -c "python manage.py migrate
python manage.py createsuperuser && \
python manage.py populate_products && \
pytest"
```

### Для самостоятельного тестирования


