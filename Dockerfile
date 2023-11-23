FROM --platform=linux/arm64 python:3.10.10-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .
RUN apk update && apk add chromium chromium-chromedriver

RUN apk add --no-cache --virtual build-dependencies libpq-dev build-base
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +w .
EXPOSE 8000
ENTRYPOINT ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload" ]
