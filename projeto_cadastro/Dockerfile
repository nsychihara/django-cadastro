FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/* 

RUN pip install --upgrade pip && pip install django psycopg2-binary
COPY . . 

EXPOSE 8000 

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]