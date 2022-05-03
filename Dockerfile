FROM python:3.8-slim-bullseye

# Set working directory.
WORKDIR /src

# Copy dependencies.
COPY requirements.txt /src

# Install dependencies.
RUN pip install -r requirements.txt

# Copy project.
COPY . /src/

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
