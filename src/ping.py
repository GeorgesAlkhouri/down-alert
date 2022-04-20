import shlex
import subprocess
import time

from log import logger


def is_reachable(url: str, timeout: float = 5, retries: int = 5) -> bool:

    assert retries > 0, "Retries has to be > 0."

    command_line = f"ping -c 1 {url}"
    args = shlex.split(command_line)

    for _try in range(1, retries + 1):
        try:
            subprocess.check_call(
                args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout
            )
        except subprocess.CalledProcessError as _e:
            logger.error(_e)
            logger.info(f"Could not reach {url}. {retries - (_try)} more tries.")
            if _try < retries:
                time.sleep(timeout)
                continue
            return False
        except subprocess.TimeoutExpired as _e:
            logger.error(_e)
            logger.info(f"Could not reach {url}. {retries - (_try)} more tries.")
            if _try < retries:
                time.sleep(timeout)
                continue
            return False

        return True

    return True
