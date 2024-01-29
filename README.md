# MvcArchitecture

Hello there

This code is a simple system of token validation using a MVC (model, view, controller) architecture, on this code was applied some concepts like:

<ul>
    <li>Test driven code (unity tests and integration)</li>
    <li>Documentation with mkdocs</li>
    <li>Api Rest</li>
    <li>Schemas for request and response</li>
    <li>Object-oriented programming</li>
</ul>

Beyond that, the technologies used are:

<ul>
    <li>SqlAlchemy</li>
    <li>Pydantic</li>
    <li>Python</li>
    <li>Pytest</li>
    <li>Alembic</li>
    <li>Black</li>
    <li>Flake8</li>
    <li>Fast Api</li>
    <li>Sqlite</li>
</ul>

## How to use the application

### Configuring Environment Variables

For configuring the environment run the following commands

Windows:

```
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
```

Linux:

```
    python -m venv venv
    venv/bin/activate
    pip install -r requirements.txt
```

### Creating the database and migrating

This project was created using sqlite, but you can change and use any database, in order to create the sqlite using the models available you must use the following code:

```
    python
    from src.infra.config.db_connection import *
    from src.infra.models.users import *
    db_conn = DataBaseConnectionHandler()
    engine = db_conn.get_engine()
    Base.metadata.create_all(engine)
    exit()
```

### Migrating the changes in the models with alembic

```
    alembic upgrade head
```

### Documentation with Mkdocs

To run the documentation with mkdocs you must use following command

```
    mkdocs serve
```

### Run the project

For running the project you must run:

```
    uvicorn server:app --reload --port 8080
```

### Docker

This project has support to docker, so if you want to run use:

Build:

```
    docker build -t mvc-python
```

Run:

```
    docker run -it mvc-python
```
