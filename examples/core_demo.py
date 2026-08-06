"""
OpenLSP Core Demo v0.1

Demonstrates usage of OpenLSP Core components.
"""


import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

from openlsp_core.message import create_message, serialize_message
from openlsp_core.session import Session


def main():

    session = Session(
        "zh-CN",
        "en-US"
    )

    session.start()

    message = create_message(
        session.source,
        session.target,
        "你好，OpenLSP"
    )

    print("Session Status:")
    print(session.status)

    print()

    print("OpenLSP Message:")

    print(
        serialize_message(message)
    )

    session.close()

    print()

    print("Session Closed:")
    print(session.status)


if __name__ == "__main__":
    main()
