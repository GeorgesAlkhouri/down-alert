from typing import Dict
from alert import mail_alert
from config import read_secrets

from ping import is_reachable
from log import logger


def down_alert(config: Dict):

    url = config["server_url"]
    try:
        reachable = is_reachable(url)
    except BaseException as _e:
        logger.error(f"Something went wrong. Could not check if {url} is reachable.")
        logger.exception(_e)
        return

    if not reachable:
        logger.info(f"{url} is down!")
        mail_alert(*read_secrets(config["env_path"]), **config)
        return

    logger.info(f"{url} is up!")
