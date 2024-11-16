FROM python:3.10-slim

EXPOSE 3000

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]