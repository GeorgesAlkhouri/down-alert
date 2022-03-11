
import subprocess
import shlex


def is_reachable(url: str, timeout: float = 5) -> bool:

  command_line = f"ping -c 1 {url}"
  args = shlex.split(command_line)
  try:
      subprocess.check_call(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE, timeout=timeout)
  except subprocess.CalledProcessError:
      return False
  except subprocess.TimeoutExpired:
      return False

  return True
    
