FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip3 install --upgrade pip
RUN pip3 install pipenv && pipenv sync --system

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

WORKDIR /src
COPY app ./

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]