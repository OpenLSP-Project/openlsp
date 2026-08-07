"""
OpenLSP Validator Tests

Tests for message validation.
"""


from openlsp_core.message import create_message
from openlsp_core.validator import validate_message


def test_valid_message():

    message = create_message(
        "client",
        "server",
        "Hello OpenLSP"
    )

    assert validate_message(message) is True


def test_invalid_protocol():

    message = create_message(
        "client",
        "server",
        "Hello OpenLSP"
    )

    message["protocol"] = "InvalidProtocol"

    assert validate_message(message) is False
