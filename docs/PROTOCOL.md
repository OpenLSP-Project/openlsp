# OpenLSP Protocol Specification

## Open Language Service Protocol

**Version:** 0.2-alpha

**Status:** Draft

**Last Updated:** August 2026

---

# Revision History

| Version | Status | Description |
|----------|--------|-------------|
| 0.1-alpha | Draft | Initial protocol framework |
| 0.2-alpha | Draft | Introduced protocol philosophy and protocol scope |

---

# 1. Introduction

OpenLSP (Open Language Service Protocol) is an open protocol for temporary cross-language communication between nearby devices.

Unlike translation applications, OpenLSP does not define how translation is performed.

Instead, OpenLSP defines how devices discover each other, establish temporary language sessions, exchange messages, and terminate communication securely.

Translation engines, AI models, speech recognition systems, user interfaces, and commercial products are outside the scope of this specification.

The goal of OpenLSP is to become an open interoperability standard for multilingual communication.

---

# 2. Design Philosophy

OpenLSP is built upon the following design principles.

## 2.1 Connection Before Translation

The primary responsibility of OpenLSP is to establish communication.

Translation is considered an implementation detail handled by participating devices.

---

## 2.2 Temporary by Default

Every communication session is temporary.

OpenLSP does not create permanent relationships between users.

A completed session should leave no persistent connection unless both parties explicitly choose another communication channel outside OpenLSP.

---

## 2.3 Original Text First

OpenLSP transports original language content.

Translation should be performed by the receiving device whenever possible.

This approach minimizes unnecessary data transfer while allowing different translation technologies to coexist.

---

## 2.4 Privacy First

OpenLSP is designed to minimize unnecessary data collection.

The protocol does not require:

- User accounts
- Phone numbers
- Email addresses
- Social identities
- Mandatory cloud storage

Implementations may provide additional services, but they are outside the protocol specification.

---

## 2.5 Open Standard

OpenLSP is an open protocol.

Any developer, organization, hardware manufacturer, or software vendor may implement OpenLSP.

No single commercial entity should control the protocol specification.

---

# 3. Protocol Scope

This specification defines:

- Device discovery
- Temporary session establishment
- Session lifecycle
- Capability negotiation
- Message exchange
- Session termination

This specification does **not** define:

- Machine translation quality
- Speech recognition algorithms
- AI model implementation
- User interface design
- Business models
- Commercial products

---

# 4. Protocol Status

OpenLSP Version 0.2-alpha is an early engineering draft.

The specification is under active development.

Protocol fields, message formats, and transport mechanisms may change before Version 1.0.

Community discussion, feedback, and reference implementations are encouraged.

---

*End of Part 1*

---

# 5. Terminology

This section defines the core terms used throughout the OpenLSP specification.

Clear terminology is required to ensure consistent implementations across different platforms.

---

## 5.1 Device

A Device is any physical or virtual computing entity capable of implementing OpenLSP.

Examples include:

- Smartphones
- Wireless earbuds
- AR glasses
- Translation terminals
- Embedded systems

A Device is not equivalent to a user identity.

One user may operate multiple Devices.

---

## 5.2 Endpoint

An Endpoint is a communication participant within an OpenLSP session.

An Endpoint represents the active communication capability of a Device.

An Endpoint may provide:

- Language input
- Language output
- Translation capability
- Audio processing
- Display capability

---

## 5.3 Session

A Session is a temporary communication relationship established between OpenLSP Endpoints.

A Session has:

- A beginning
- An active state
- An ending condition

A Session does not create:

- Permanent identity
- Friendship relationship
- Contact information
- Social connection

---

## 5.4 Capability

A Capability describes functions supported by an OpenLSP Endpoint.

Examples:

```
text
voice
tts
subtitle
image
ai-agent
```

Capabilities allow devices with different hardware and software abilities to communicate effectively.

---

## 5.5 Message

A Message is a structured unit of information exchanged between OpenLSP Endpoints.

Messages may represent:

- Discovery information
- Session requests
- Session responses
- Language content
- Session termination

---

# 6. Architecture

OpenLSP follows a layered architecture model.

```
User Layer

↓

Application Layer

↓

OpenLSP Protocol Layer

↓

Transport Layer

↓

Device Capability Layer
```

---

## 6.1 User Layer

The User Layer provides human interaction.

Examples:

- Mobile applications
- Wearable interfaces
- Translation devices

The User Layer is responsible for presenting communication experiences.

---

## 6.2 Application Layer

The Application Layer manages OpenLSP implementations.

Responsibilities include:

- Session control
- User interaction
- Local service integration

---

## 6.3 Protocol Layer

The OpenLSP Protocol Layer defines:

- Discovery
- Handshake
- Session management
- Message exchange

This layer provides interoperability between different implementations.

---

## 6.4 Transport Layer

The Transport Layer provides device-to-device communication.

Possible transports include:

- Bluetooth
- NFC
- Wi-Fi Direct
- Local network

OpenLSP does not require a single transport technology.

---

## 6.5 Device Capability Layer

The Device Capability Layer provides local processing functions.

Examples:

- Automatic speech recognition (ASR)
- Translation models
- Text-to-speech (TTS)
- Display systems

OpenLSP does not require any specific AI model.

---

*End of Part 2*
