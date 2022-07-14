FROM python:3.9-slim

RUN pip install tomodachi

COPY app /app
WORKDIR /app

ENV PYTHONUNBUFFERED=1

CMD ["tomodachi", "run", "service.py", "--production"]
