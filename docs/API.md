# OpenLSP Core API

Version: v0.4-alpha (Draft)

---

# Overview

This document describes the public API provided by the OpenLSP Core reference implementation.

The goal of this API is to provide a simple and stable programming interface for OpenLSP applications.

---

# Message API

## create_message()

Create a new OpenLSP message.

### Parameters

| Name | Description |
|------|-------------|
| source | Message sender |
| target | Message receiver |
| content | Message content |

### Returns

A Python dictionary representing an OpenLSP message.

---

## serialize_message()

Convert an OpenLSP message into JSON format.

### Parameters

| Name | Description |
|------|-------------|
| message | OpenLSP message object |

### Returns

JSON string.

---

# Session API

## Session()

Create a communication session.

### Methods

- start()
- close()

### Properties

- session_id
- source
- target
- status
- created_at

---

# Planned API

The following APIs are planned for future releases.

## Validator

```python
validate_message(message)
```

Validate an OpenLSP message.

---

## Transport

```python
Transport.send(message)

Transport.receive()
```

Abstract communication interface.

---

## Exceptions

```python
OpenLSPError

InvalidMessageError

InvalidSessionError
```

Unified exception system.

---

# Stability

Current status:

Draft (v0.4-alpha)

API definitions may evolve before the first stable release.
