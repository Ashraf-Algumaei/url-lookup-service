FROM tiangolo/uvicorn-gunicorn:python3.8 AS builder

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app /app

# Runs the tests 
FROM tiangolo/uvicorn-gunicorn:python3.8 AS tests
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY --from=builder /app /app
COPY tests tests
RUN pip install pytest pytest-mock
WORKDIR /app
ARG COSMOS_DB_MASTER_KEY=$COSMOS_DB_MASTER_KEY
ENV COSMOS_DB_MASTER_KEY $COSMOS_DB_MASTER_KEY
ARG APP_INSIGHTS_CONNECTION_STRING=$APP_INSIGHTS_CONNECTION_STRING
ENV APP_INSIGHTS_CONNECTION_STRING $APP_INSIGHTS_CONNECTION_STRING
RUN pytest tests/unit