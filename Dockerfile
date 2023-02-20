FROM python:3.11-alpine3.17

ENV PYTHONUNBUFFERED=1

RUN apk add gcc g++ cmake make mupdf-dev freetype-dev libpq-dev

WORKDIR /app

COPY ["requirements.txt", "."]

RUN pip install -r requirements.txt

COPY [".", "."]

EXPOSE 8000

CMD [ "python3", "main.py" ]