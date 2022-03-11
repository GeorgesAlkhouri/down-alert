from app import down_alert


if __name__ == "__main__":
    config = {"url": "194.163.179.102", "smtp_server": "smtp"}
    down_alert(config)
