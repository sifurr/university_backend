FROM python:3.13-slim

WORKDIR /app 

# system dependency
RUN apt update && apt install -y build-essential

# copy requirements first (cache optimization)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#copy project
COPY . .

# run app
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]


