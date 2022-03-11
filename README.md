# Down Alert
Small Python application. Pings a service URL and sends a TLS encrypted mail if the service does not respond.

## Usage

Clone the repository to your machine and create the config.ini file.


```bash
git clone git@github.com:GeorgesAlkhouri/down-alert.git

cd down-alert
cp config.example.ini config.ini
# adjust config.ini file
# and deploy the service in the background with Docker.
docker compose up -d
```


## Config

```ini
[GENERAL]
# every 3 hours
interval=10800
server_url= the server or the service you try to reach
smtp_server=
smtp_port=
from_mail= sender mail
to_mail= receiver mail

[SECRETS]
user=
password=
```
