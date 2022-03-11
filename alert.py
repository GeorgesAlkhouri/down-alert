import smtplib, ssl, socket
from datetime import datetime


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
):
    socket.setdefaulttimeout(socket_timeout)
    context = ssl.create_default_context()
    message = create_message(**kwargs)
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(user, password)
            server.sendmail(from_mail, to_mail, message)
    except BaseException as _e:
        print("Could not establish server connection. Maybe check Firewall settings.")
        print("Reason:", _e)
