FROM python:3.10-alpine3.18

ENV API_DEBUG=false
ENV TZ="America/Sao_Paulo"

RUN date

WORKDIR /opt/app

COPY . .

RUN python3 -m pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]