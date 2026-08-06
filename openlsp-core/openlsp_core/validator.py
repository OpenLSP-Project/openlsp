"""
OpenLSP Core Validator Module

Version: 0.4-alpha

Basic validation for OpenLSP messages.
"""


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
