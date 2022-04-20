import os
from dataclasses import dataclass


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


def create_config(prefix="DOWN_ALERT") -> Config:
    config_dict = {}
    for key, _type in Config.__annotations__.items():
        value = os.getenv(f"{prefix}_{key.upper()}")
        if value:
            config_dict[key] = _type(value)
    return Config(**config_dict)
