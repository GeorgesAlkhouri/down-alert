import os
import time

from app import down_alert
from config import create_config
from log import logger

if __name__ == "__main__":

    log_level = os.environ.get("DOWN_ALERT_LOG_LEVEL", "INFO").upper()
    logger.setLevel(log_level)

    config = create_config()
    logger.info(f"Start pinging url {config.server_url}")
    while True:

        alert_sent = down_alert(config)

        if alert_sent:
            interval = config.interval_wait_after_send
            logger.info(
                f"Alert was sent. Next check if reachable will be in {interval}s."
            )
        else:
            interval = config.interval

        logger.debug("Waiting...")
        time.sleep(interval)
