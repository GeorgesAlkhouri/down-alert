import smtplib, ssl, socket
from datetime import datetime

from log import logger


def create_message(server_url: str, **kwargs) -> str:
    return """\
Subject: Server ({server_url}) not reachable!

On {date}, the server not responded to ping.
   """.format(
        server_url=server_url, date=str(datetime.now().ctime())
    )


def mail_alert(
    user: str,
    password: str,
    from_mail: str,
    to_mail: str,
    smtp_server: str,
    smtp_port: str,
    socket_timeout: float = 5,
    **kwargs,
) -> bool:
    socket.setdefaulttimeout(socket_timeout)
    context = ssl.create_default_context()
    message = create_message(**kwargs)
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.ehlo()
            server.login(user, password)
            errors = server.sendmail(from_mail, to_mail, message)
    except BaseException as _e:
        logger.error(
            "Could not establish server connection. Maybe check Firewall settings."
        )
        raise _e

    # True if mail could be sent to receiver
    return not errors
