import os
from dataclasses import dataclass
from log import logger


@dataclass
class Config:
    server_url: str
    smtp_server: str
    smtp_port: int
    from_mail: str
    to_mail: str
    user: str
    password: str
    interval: int = 300
    interval_wait_after_send: int = 10_800
    use_wget: bool = False


def create_config(prefix="DOWN_ALERT") -> Config:
    config_dict = {}
    for key, _type in Config.__annotations__.items():
        value = os.getenv(f"{prefix}_{key.upper()}")
        if value:
            logger.debug(f"Found: {key}={value}")
            if _type == bool:
                config_dict[key] = bool(eval(value))
            else:
                config_dict[key] = _type(value)
    config = Config(**config_dict)
    return config
