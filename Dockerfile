FROM python:3.9
RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY app /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
