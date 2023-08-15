FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY ../.. /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000

ENV MODULE_NAME="src.api.main"

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]