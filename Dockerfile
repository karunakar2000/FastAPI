FROM python:3.11-slim

WORKDIR /app

ENV AWS_REGION=us-east-1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9000

ENTRYPOINT ["uvicorn", "main:app","--host", "0.0.0.0"]
CMD ["--port", "9000"]