from datetime import datetime, timezone

TIMESTAMP_WITH_TIMEZONE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"


class GeneralObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def get_utc_now():
    """Returns current utc time with timezone"""
    return datetime.now(timezone.utc)
    # Deprecated code
    # return datetime.utcnow()
