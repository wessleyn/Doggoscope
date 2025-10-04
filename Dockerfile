FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update -qq \
      && apt-get install -y --no-install-recommends \
      build-essential \
      python3-dev \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=api/index.py
CMD ["flask", "run", "--host=0.0.0.0"]
