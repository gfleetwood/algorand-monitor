FROM python:3.9.5

RUN apt-get update && apt-get install -y \
    libcurl4-gnutls-dev \
    libssl-dev \
    libxml2-dev \
    unixodbc-dev \
    odbc-postgresql
    
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl gnupg && \
    curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | apt-key add - && \
    echo "deb https://packages.doppler.com/public/cli/deb/debian any-version main" | tee /etc/apt/sources.list.d/doppler-cli.list && \
    apt-get update && \
    apt-get -y install doppler
             
WORKDIR /home/pipeline
COPY . .

RUN crontab scheduler
RUN python3 -m  venv .venv
RUN source .venv/bin/activate
RUN pip3 install -r requirements.txt
