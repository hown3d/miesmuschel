FROM python:3.10

RUN apt-get update && apt-get install -y ffmpeg portaudio19-dev

WORKDIR /speecher

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt

# Run the application:
COPY *.py .

CMD ["python","speecher.py"]