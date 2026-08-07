"""
OpenLSP Validator Exception Tests

Tests exception based validation.
"""


import pytest

from openlsp_core.message import create_message
from openlsp_core.validator import validate_message_or_raise
from openlsp_core.exceptions import InvalidMessageError


def test_valid_message_no_exception():

    message = create_message(
        "client",
        "server",
        "Hello OpenLSP"
    )

    assert validate_message_or_raise(message) is True


def test_invalid_message_raises_exception():

    message = create_message(
        "client",
        "server",
        "Hello OpenLSP"
    )

    message["protocol"] = "InvalidProtocol"

    with pytest.raises(InvalidMessageError):
        validate_message_or_raise(message)
