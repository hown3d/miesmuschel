FROM python:3.10-slim as compile

RUN apt-get update && apt-get install -y ffmpeg portaudio19-dev espeak
WORKDIR /speecher

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt
RUN rm -r /root/.cache

# Run the application:
COPY src src
COPY pyproject.toml .
RUN pip install .

FROM python:3.10-slim
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg espeak
COPY --from=compile /opt/venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
CMD ["speecher"]