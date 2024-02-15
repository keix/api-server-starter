# Minimal API Server.

This can be used as a template for new projects, but the configuration is minimal.

## Program behavior.

- Nginx is listening on localhost:80
- Forwards requests to Uvicorn, which is listening on localhost:8080
- This application utilizes SQLite as its database system

## Installation guide.

The installation guide outlines steps to clone the project, build it using Docker, and start the application.

```
 $ git clone git@github.com:keix/api-server-starter.git
 $ cd api-server-starter
 $ docker compose up --build
```

## Usage.

To create a user, use this command:

```
 $ curl -X POST http://localhost/users/ -H "Content-Type: application/json" \
                        -d '{"email": "keix@example.com", "password": "HelloWorld"}'
```

To retrieve the list of users, use this command:

```
 $ curl http://localhost/users/
```

## API Specification.

FastAPI automatically generates API documentation upon running.

http://localhost/redoc

