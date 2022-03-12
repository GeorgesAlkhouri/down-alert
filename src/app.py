from typing import Dict
from alert import mail_alert
from config import read_secrets

from ping import is_reachable
from log import logger


def down_alert(config: Dict) -> bool:
    """Check if a server is reachable and alert via
    mail if not.
    Return bool whether an alert could be sent or
    not.
    """

    url = config["server_url"]
    try:
        reachable = is_reachable(url)
    except BaseException as _e:
        logger.error(f"Something went wrong. Could not check if {url} is reachable.")
        logger.exception(_e)
        return False

    if not reachable:
        logger.info(f"{url} is down!")
        return mail_alert(*read_secrets(config["env_path"]), **config)

    logger.info(f"{url} is up!")
    return False
