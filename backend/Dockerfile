# 
FROM python:3.9

# 
WORKDIR /usr/src/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



# 
COPY ./requirements.txt /backend/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

# 
COPY ./core /backend/core

# 
CMD ["uvicorn", "backend.core.config:app", "--host", "0.0.0.0", "--port", "80"]