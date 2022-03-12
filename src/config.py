from configparser import ConfigParser
from typing import Dict, Tuple


def read_config(env_path: str) -> Dict:
    env_file = ConfigParser()
    env_file.read(env_path)
    config = dict(env_file["GENERAL"])
    config["env_path"] = env_path
    config["interval"] = env_file["GENERAL"].getint("interval")
    config["interval_wait_after_send"] = env_file["GENERAL"].getint(
        "interval_wait_after_send"
    )
    return config


def read_secrets(env_path: str) -> Tuple[str, str]:
    env_file = ConfigParser()
    env_file.read(env_path)
    return env_file["SECRETS"]["user"], env_file["SECRETS"]["password"]
