# Down Alert
Small Python application. Pings a service URL and sends a TLS encrypted mail if the service does not respond.

## Usage

Clone the repository to your machine and copy the docker-compose.yml.example file.


```bash
git clone git@github.com:GeorgesAlkhouri/down-alert.git

cd down-alert
cp docker-compose.yml.example docker-compose.yml
# adjust docker-compose.yml file to your needs
# and deploy the service in the background with Docker.
docker compose up -d
```


## Config

Configure the app by setting the following env variables with docker compose.

```
# check every 5 minutes
DOWN_ALERT_INTERVAL: 300
# wait 3 hours
# after an alert could be sent successfully
DOWN_ALERT_SMTP_SERVER: ...
DOWN_ALERT_SMTP_PORT: ...
DOWN_ALERT_FROM_MAIL: ...
DOWN_ALERT_TO_MAIL: ...
DOWN_ALERT_USER: ...
DOWN_ALERT_PASSWORD: ...
```

## Docker Compose Example

```yaml
x-down-alert-common:
  &down-alert-common
  image: python:3.10-alpine
  environment:
    &down-alert-common-env
    TZ: Europe/Berlin
    # check every 5 minutes
    DOWN_ALERT_INTERVAL: 300
    # wait 3 hours
    # after an alert could be sent successfully
    DOWN_ALERT_INTERVAL_WAIT_AFTER_SEND: 10800
    DOWN_ALERT_SMTP_SERVER: ...
    DOWN_ALERT_SMTP_PORT: ...
    DOWN_ALERT_FROM_MAIL: ...
    DOWN_ALERT_TO_MAIL: ...
    DOWN_ALERT_USER: ...
    DOWN_ALERT_PASSWORD: ...
  volumes:
      - ./src/:/app/:ro
  command: ["python", "/app/__main__.py"]
  healthcheck:
    test: ["CMD", "pgrep", "-x", "python"]
    interval: 30s
    retries: 0

services:

  sample-1-service:
    <<: *down-alert-common
    environment:
      <<: *down-alert-common-env
      DOWN_ALERT_LOG_LEVEL: DEBUG
      DOWN_ALERT_SERVER_URL: sample-1.service.de

  sample-2-service:
    <<: *down-alert-common
    environment:
      <<: *down-alert-common-env
      TZ: Europe/London
      DOWN_ALERT_INTERVAL: 3600
      DOWN_ALERT_SERVER_URL: sample-2.service.com
```
