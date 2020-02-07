# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:3

# Copy the Python Script to blink LED
COPY main.py ./
COPY requirements.txt ./

# Intall the rpi.gpio python module
RUN pip install -r requirements.txt

# Trigger Python script
CMD ["python", "./main.py"]
