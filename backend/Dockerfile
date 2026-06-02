FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src .

EXPOSE 8000

CMD [ "fastapi", "run", "/app/todo_api/main.py", "--port", "8000" ]