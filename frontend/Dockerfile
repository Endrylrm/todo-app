FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src .

EXPOSE 3000

CMD [ "python", "todo_gui/main.py" ]