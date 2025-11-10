FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y git git-lfs
RUN git lfs install && git clone https://huggingface.co/seara/rubert-tiny2-russian-sentiment

CMD ["python", "main.py"]
