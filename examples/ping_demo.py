"""
OpenLSP Ping Demo v0.1

A minimal example showing
OpenLSP message creation and receiving.
"""


import json
import uuid
from datetime import datetime


def create_message(source, target, text):
    return {
        "protocol": "OpenLSP",
        "version": "0.1",
        "session": {
            "id": str(uuid.uuid4()),
            "type": "temporary",
            "created": datetime.utcnow().isoformat()
        },
        "language": {
            "source": source,
            "target": target
        },
        "payload": {
            "type": "text",
            "content": text
        }
    }


def receive_message(message):
    print("OpenLSP Message Received")
    print("------------------------")
    print("Language:")
    print(
        message["language"]["source"],
        "->",
        message["language"]["target"]
    )

    print("Content:")
    print(message["payload"]["content"])


if __name__ == "__main__":

    message = create_message(
        "zh-CN",
        "en-US",
        "你好，OpenLSP"
    )

    print("Sending OpenLSP Message")
    print("-----------------------")

    print(json.dumps(
        message,
        ensure_ascii=False,
        indent=2
    ))

    print()

    receive_message(message)
