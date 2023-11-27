FROM python:3.10.6-slim
COPY icecream icecream/
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn icecream.fast:app --host 0.0.0.0 --port $PORT
