"""
OpenLSP Core Validator Module
from .exceptions import InvalidMessageError
Version: 0.4-alpha

Basic validation for OpenLSP messages.
"""

from .exceptions import InvalidMessageError

REQUIRED_FIELDS = [
    "protocol",
    "version",
    "source",
    "target",
    "content"
]


def validate_message(message):
    """
    Validate an OpenLSP message.

    Returns:
        True if valid.
        False if invalid.
    """

    if not isinstance(message, dict):
        return False

    for field in REQUIRED_FIELDS:
        if field not in message:
            return False

    if message["protocol"] != "OpenLSP":
        return False

    if message["version"] != "0.2":
        return False

    return True

def validate_message_or_raise(message):
    """
    Validate an OpenLSP message.

    Raises:
        InvalidMessageError
        when the message is invalid.
    """

    if not isinstance(message, dict):
        raise InvalidMessageError(
            "Message must be a dictionary"
        )

    for field in REQUIRED_FIELDS:
        if field not in message:
            raise InvalidMessageError(
                f"Missing required field: {field}"
            )

    if message["protocol"] != "OpenLSP":
        raise InvalidMessageError(
            "Invalid protocol"
        )

    if message["version"] != "0.2":
        raise InvalidMessageError(
            "Unsupported version"
        )

    return True
