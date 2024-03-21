FROM --platform=linux/amd64 python:3.10.13-slim

#copy all data to app
COPY . /app

WORKDIR /app

RUN python3 -m venv /opt/venv


RUN /opt/venv/bin/pip install --upgrade pip && /opt/venv/bin/pip install -r requirements.txt

RUN chmod +x entrypoint.sh
RUN chmod +x collectstatic.sh

CMD ["/app/entrypoint.sh"]