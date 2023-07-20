FROM python:3.10.4
WORKDIR /app
ADD requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
ADD . /app
CMD ["python", "./main.py"]
