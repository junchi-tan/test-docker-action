FROM python:3-slim

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ../../.. .

CMD ["python", "/fetch_file_path.py"]