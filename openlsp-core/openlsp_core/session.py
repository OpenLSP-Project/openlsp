"""
OpenLSP Core Session Module

Version: 0.1

Basic session management for OpenLSP.
"""


import uuid
from datetime import datetime


class Session:

    def __init__(self, source, target):
        self.session_id = str(uuid.uuid4())
        self.source = source
        self.target = target
        self.status = "CREATED"
        self.created_at = datetime.utcnow().isoformat()

    def start(self):
        self.status = "ACTIVE"

    def close(self):
        self.status = "CLOSED"
