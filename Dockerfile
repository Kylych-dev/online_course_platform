FROM python:3.10

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

WORKDIR /backend

COPY requirements.txt .


RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /backend

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]