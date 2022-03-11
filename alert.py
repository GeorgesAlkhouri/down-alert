import smtplib, ssl, socket


def message() -> str:
    return f"""
Subject: Server not reachable

This message is sent from Python.
   """


def mail_alert(
    user: str,
    password: str,
    from_mail: str,
    to_mail: str,
    smpt_server: str,
    smtp_port: int,
    socket_timeout: float = 5,
):

    socket.setdefaulttimeout(socket_timeout)
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
    except BaseException as _e:
        print("Could not establish server connection. Maybe check Firewall settings.")
        return

    try:
        server.starttls(context=context)
        server.login(
            "cloud.couri@gmail.com",
            "tighten-granular-uranium-hunk-comma-married-unpaired",
        )
        server.sendmail("cloud.couri@gmail.com", "ofungus@gmail.com", message())
    except BaseException as _e:
        print(_e)
    finally:
        server.quit()
