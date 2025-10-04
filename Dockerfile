FROM python:3.11-slim

WORKDIR /

RUN apt-get update -qq \
      && apt-get install -y --no-install-recommends \
      build-essential \
      python3-dev \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "api/index.py"]
