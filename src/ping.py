import time
import subprocess
import shlex
from log import logger

def is_reachable(url: str, timeout: float = 5, retries: int = 5) -> bool:

  assert retries > 0, "Retries has to be > 0."

  command_line = f"ping -c 1 {url}"
  args = shlex.split(command_line)

  for _try in range(retries):
    try:
      subprocess.check_call(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE, timeout=timeout)
    except subprocess.CalledProcessError:
      if _try < retries:
        logger.info(f"Could not reach {url}. {retries - (_try + 1)} more tries.")
        time.sleep(timeout)
        continue
      return False
    except subprocess.TimeoutExpired:
      logger.info(f"Could not reach {url}. {retries - (_try + 1)} more tries.")
      if _try < retries:
        time.sleep(timeout)
        continue
      return False
    
    return True
