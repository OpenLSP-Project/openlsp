"""
OpenLSP Core Message Module

Version: 0.1

Basic message creation for OpenLSP.
"""


import json
import uuid
from datetime import datetime


def create_message(source, target, content):
    """
    Create a basic OpenLSP message.
    """

    message = {
        "protocol": "OpenLSP",
        "version": "0.2",
        "message_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "target": target,
        "content": content
    }

    return message


def serialize_message(message):
    """
    Convert OpenLSP message into JSON format.
    """

    return json.dumps(
        message,
        ensure_ascii=False,
        indent=2
    )
