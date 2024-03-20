# Test project

Simple API

## Clone and Run project

```git clone git@github.com:allenkg/test.git```

create virtual env 
python3 -m venv venv

Run docker commands

```
docker-compose build
docker-compose up -d
docker exec -it <container_name> bash -c "python manage.py migrate"
```

Enter the web container
```
docker ps
docker exec -it <container_name> bash
```

Create superuser and populate some data to DB
``` 
python manage.py createsuperuser
python manage.py populate_products
```

Run Test
``` pytest ```

### Check API Doc to manual API requests


