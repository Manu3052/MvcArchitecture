FROM python:3

WORKDIR /MvcArchitecture

COPY . .
COPY requirements.txt /MvcArchitecture

RUN pip install -r requirements.txt


CMD ["uvicorn", "server:app", "--reload"]