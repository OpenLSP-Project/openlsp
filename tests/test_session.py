"""
OpenLSP Session Tests

Basic validation for OpenLSP session lifecycle.
"""


import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

from openlsp_core.session import Session


def test_session_lifecycle():

    session = Session(
        "zh-CN",
        "en-US"
    )

    assert session.status == "CREATED"

    session.start()

    assert session.status == "ACTIVE"

    session.close()

    assert session.status == "CLOSED"
