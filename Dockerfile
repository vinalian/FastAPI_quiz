FROM python:3.11
WORKDIR .

RUN python3 -m venv venv
SHELL ["/bin/bash", "-c"]
RUN source venv/bin/activate

COPY req.txt .
RUN pip install --upgrade pip && pip install -r req.txt

COPY docker .
