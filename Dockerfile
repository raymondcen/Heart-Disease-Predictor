FROM python:3.13-slim
WORKDIR /app
COPY . /app
RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python3", "application.py"]