import os
import time

from app import down_alert
from config import create_config
from log import logger


def main():
    log_level = os.environ.get("DOWN_ALERT_LOG_LEVEL", "INFO").upper()
    logger.setLevel(log_level)

    config = create_config()
    test_cmd = "ping" if not config.use_wget else "wget"
    logger.info(f"Start testing {config.server_url} with {test_cmd}.")
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


if __name__ == "__main__":
    main()
