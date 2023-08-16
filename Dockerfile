FROM python:3.9.17

WORKDIR /code

COPY ./ /code

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]