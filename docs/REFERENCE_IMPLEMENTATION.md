# OpenLSP Reference Implementation

## Overview

The OpenLSP Reference Implementation demonstrates the basic behavior of the Open Language Service Protocol.

The reference implementation is not a production SDK.

It is designed to help developers understand:

- OpenLSP message creation
- Message exchange flow
- Session concepts
- Protocol behavior

---

# Current Reference Example

The current example implementation is:

```text
examples/ping_demo.py
The demo provides a minimal OpenLSP communication model.

Message Flow
The reference flow:

Create Message

      ↓

OpenLSP Message

      ↓

Receive Message

      ↓

Process Content
Core Functions
create_message()
Example function:

create_message(source, target, text)
Purpose:

Creates an OpenLSP message containing:

Source language

Target language

Message content

receive_message()
Example function:

receive_message(message)
Purpose:

Receives and processes an OpenLSP message.

Implementation Principles
Future OpenLSP implementations should maintain:

Protocol compatibility

Privacy-first communication

Temporary sessions

Platform independence

Future Development
Future reference implementations may include:

Device discovery

Transport adapters

Session management

Local AI integration

SDK development

Relationship to Protocol
The reference implementation follows:

docs/PROTOCOL.md
The protocol defines the rules.

The reference implementation demonstrates possible usage.
