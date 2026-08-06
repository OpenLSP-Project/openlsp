"""
OpenLSP Message Tests

Basic validation for OpenLSP message creation.
"""


import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

from openlsp_core.message import create_message


def test_create_message():

    message = create_message(
        "zh-CN",
        "en-US",
        "你好"
    )

    assert message["protocol"] == "OpenLSP"
    assert message["version"] == "0.2"
    assert message["source"] == "zh-CN"
    assert message["target"] == "en-US"
    assert message["content"] == "你好"
