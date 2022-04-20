from dataclasses import asdict

from alert import mail_alert
from config import Config
from log import logger
from ping import is_reachable


def down_alert(config: Config) -> bool:
    """Check if a server is reachable and alert via
    mail if not.
    Return bool whether an alert could be sent or
    not.
    """

    url = config.server_url
    try:
        reachable = is_reachable(url)
    except BaseException as _e:
        logger.error(f"Something went wrong. Could not check if {url} is reachable.")
        logger.exception(_e)
        return False

    if not reachable:
        logger.info(f"{url} is down!")
        return mail_alert(**asdict(config))

    logger.debug(f"{url} is up!")
    return False
