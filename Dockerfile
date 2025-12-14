FROM python:3.11-slim
LABEL author="@KARUNAKAR" email="k7rt2020@gmail.com"
WORKDIR /app
ENV AWS_REGION=us-east-1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app","--host", "0.0.0.0"]
CMD ["--port", "8000"]