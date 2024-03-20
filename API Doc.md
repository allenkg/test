# API Documentation

### Register User

```http
POST http://localhost:8000/v1/users/register/
Content-Type: application/json

{
  "email": "test@email.com",
  "name": "tester",
  "password": "12345678A@",
  "password_confirmation": "12345678A@"
}
```
response
``` 
{
  "email": "test@email.com"
}
```

### User Login

```http
POST http://localhost:8000/v1/users/login/
Content-Type: application/json

{
  "email": "test@email.com",
  "password": "12345678A@"
}
```

response
``` 
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwOTU3NTk5LCJpYXQiOjE3MTA5NTcyOTksImp0aSI6ImIyODQyMmQxNTQwNjQzZmQ5M2UxNGM3MzFkM2ViZmU2IiwidXNlcl9pZCI6Mn0.-MMKap4SjFF_sA7z6_wpmL16FWRcEH-rv7FtCiyBWZ4"
}
```

### Create Product Category
```
POST http://localhost:8000/v1/products/categories/
Content-Type: application/json
Authorization: Bearer <your_token>

{
  "name": "Parts",
  "description": "Description for Parts"
}
```

response
``` 
{
  "id": 7,
  "name": "Parts",
  "description": "Description for Parts"
}
```

### Delete
```
DELETE http://localhost:8000/v1/products/categories/43/
Content-Type: application/json
Authorization: Bearer <your_token>
```

### Fetch Product
```
GET http://localhost:8000/v1/products/
Content-Type: application/json

```

### Product Detail
``` 
GET http://localhost:8000/v1/products/7/
Content-Type: application/json
Authorization: Bearer <your_token>

```
response
``` 
{
  "id": 7,
  "name": "Iphone 7",
  "description": "Description of Iphone7",
  "qty": 30,
  "history": [
    {
      "id": 1,
      "product_data": {
        "new_qty": 50,
        "old_qty": 35
      },
      "product": 7,
      "created_at": "2024-03-20T17:25:23.004005Z"
    },
    {
      "id": 2,
      "product_data": {
        "new_qty": 80,
        "old_qty": 50
      },
      "product": 7,
      "created_at": "2024-03-20T17:25:28.147133Z"
    },
    {
      "id": 3,
      "product_data": {
        "new_qty": 100,
        "old_qty": 80
      },
      "product": 7,
      "created_at": "2024-03-20T17:25:31.976508Z"
    },
    {
      "id": 4,
      "product_data": {
        "new_qty": 30,
        "old_qty": 100
      },
      "product": 7,
      "created_at": "2024-03-20T17:25:35.487879Z"
    }
  ]
}
```

### Change Product qty
``` 
PATCH http://localhost:8000/v1/products/7/
Content-Type: application/json
Authorization: Bearer <your_token>

{
  "qty": 30
}

```

response
``` 
{
  "id": 7,
  "name": "Iphone 7",
  "description": "Description of Iphone7",
  "qty": 300
}
```