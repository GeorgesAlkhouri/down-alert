from app import down_alert
import os
import argparse
import time
from log import logger
from config import read_config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ping an URL and send an alert mail if service is down."
    )
    parser.add_argument(
        "env",
        type=str,
        help=".env file containing config data.",
    )
    args = parser.parse_args()

    assert os.path.isfile(args.env), f"{args.env} is not a file."
    config = read_config(args.env)
    while True:

        alert_sent = down_alert(config)

        if alert_sent:
            interval = config["interval_wait_after_send"]
            logger.info(
                f"Alert was sent. Next check if reachable will be in {interval}s."
            )
        else:
            interval = config["interval"]

        logger.info("Waiting...")
        time.sleep(interval)
