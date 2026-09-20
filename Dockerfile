FROM python:3.9-slim
WORKDIR /app
COPY welcomeraj.py .
CMD ["python", "welcomeraj.py"]
