# Planetarium API

This API provides several endpoints to manage planetarium service


## Features

- JWT Authentication
- Admin panel
- Swagger documentation
- Pagination
- Managing reservations and tickets
- Managing different endpoints

Credentials:
- `email`: **admin@pln.com**
- `password`: **12345**

## Installation

1. Clone repository

```bash
git clone https://github.com/roffi37/planetarium-api
```
2. Set parameters in .env
3. Run docker compose
```bash
docker-compose up
```
4. Check images
```bash
docker ps
```
5. Connect to interactive terminal
```bash
docker exec -it <containerid> bash
```
6. Load data
```bash
python manage.py loaddata planetarium_db
```

## Installation with Docker
1. Pull repository
```bash
docker push roffi37/planetarium-api:latest
```
2. Run compose
```bash
docker-compose up
```
3. Check images
```bash
docker ps
```
4. Connect to interactive terminal
```bash
docker exec -it <containerid> bash
```
5. Load data
```bash
python manage.py loaddata planetarium_db
```
