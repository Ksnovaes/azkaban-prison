ARG PYTHON_VERSION=3.12.3

FROM python:${PYTHON_VERSION}

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--port", "8000"]
