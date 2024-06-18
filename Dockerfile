ARG PYTHON_VERSION=3.12.3

FROM python:${PYTHON_VERSION}

WORKDIR /app

COPY . /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 7777

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7777"]
