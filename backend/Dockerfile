FROM python:3.13-slim-bookworm

# host.docker.internal -> localhost
# curl -X POST -d '{"message": "Hello world"}'  -H "Content-Type: application/json" http://host.docker.internal:8080/api/chats/
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Create python virtual environment
# isolate our python app and installs from system-level python
RUN python -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH


WORKDIR /app

# COPY local_folder/file container_destination
COPY requirements.txt /tmp/requirements.txt

# RUN within_container_while_building
RUN pip install -r /tmp/requirements.txt

COPY ./src .

CMD ["python", "-m", "http.server", "8000"]