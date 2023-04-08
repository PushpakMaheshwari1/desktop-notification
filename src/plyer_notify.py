from plyer import notification


def notify(title: str, message: str, app_icon: str = None, timeout: int = 10):
    notification.notify(
        title=title,
        message=message,
        app_icon=app_icon,
        timeout=timeout,
    )
    return True
