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

---

# 7. Discovery

Discovery is the first stage of an OpenLSP communication process.

The purpose of Discovery is to allow nearby devices to identify available OpenLSP capabilities.

Discovery does not establish a communication session.

Discovery only announces:

- Protocol support
- Protocol version
- Available language information
- Basic capability information

---

## 7.1 Discovery Message

Example:

```json
{
  "protocol": "OpenLSP",
  "version": "0.2",
  "type": "DISCOVER",
  "language": {
    "primary": "zh-CN"
  },
  "capabilities": [
    "text",
    "voice",
    "tts"
  ]
}
```

---

## 7.2 Discovery Privacy

Discovery messages SHOULD NOT contain permanent user identity information.

Discovery SHOULD NOT require:

- User accounts
- Phone numbers
- Email addresses
- Social profiles

The purpose of Discovery is capability awareness, not user identification.

---

# 8. Handshake

After Discovery, two devices may begin a handshake process.

The purpose of the handshake is to:

- Confirm OpenLSP compatibility
- Exchange communication parameters
- Prepare a temporary session

The handshake process consists of:

```
HELLO

↓

HELLO_ACK

↓

SESSION_CREATE
```

---

# 8.1 HELLO Message

A device sends a HELLO message when requesting communication.

Example:

```json
{
  "type": "HELLO",
  "protocol": "OpenLSP",
  "version": "0.2",
  "language": {
    "source": "zh-CN",
    "target": "en-US"
  }
}
```

---

# 8.2 HELLO_ACK Message

The receiving device responds with acceptance or rejection.

Accepted example:

```json
{
  "type": "HELLO_ACK",
  "accepted": true
}
```

Rejected example:

```json
{
  "type": "HELLO_ACK",
  "accepted": false
}
```

A rejected handshake SHALL terminate the connection attempt.

---

# 9. Session Creation

After successful handshake, devices create a temporary OpenLSP Session.

Example:

```json
{
  "type": "SESSION_CREATE",
  "session": {
    "id": "UUID",
    "duration": 1800
  }
}
```

---

## 9.1 Session Properties

An OpenLSP Session has the following properties:

- Temporary
- Independent
- Expirable
- Locally managed

A Session does not represent:

- A user account
- A social relationship
- A permanent connection

---

## 9.2 Session Lifetime

A Session MAY expire when:

- The negotiated duration ends
- A device disconnects
- A user manually terminates communication

---

# 10. Session Termination

Either Endpoint may terminate an active session.

Example:

```json
{
  "type": "SESSION_CLOSE",
  "reason": "completed"
}
```

After termination:

- Session state SHOULD be removed
- Temporary session data SHOULD be discarded
- Future communication requires a new Session

---

# 11. Session State Model

An OpenLSP Session follows this lifecycle:

```
CREATED

↓

ACTIVE

↓

CLOSED
```

A closed Session cannot be resumed.

A new interaction requires creation of a new Session.

---

*End of Part 3*

---

# 12. Message Model

The Message Model defines the structure of information exchanged between OpenLSP Endpoints.

All OpenLSP communication is based on structured messages.

A Message contains:

- Message type
- Session information
- Language information
- Payload data

---

# 12.1 General Message Structure

A standard OpenLSP message follows this structure:

```json
{
  "type": "MESSAGE",
  "version": "0.2",
  "session": {
    "id": "UUID"
  },
  "language": {
    "source": "zh-CN",
    "target": "en-US"
  },
  "payload": {
    "type": "text",
    "content": "你好"
  }
}
```

---

# 12.2 Message Type

The `type` field identifies the purpose of a message.

OpenLSP v0.2 defines the following message types:

| Type | Purpose |
|------|---------|
| DISCOVER | Device capability announcement |
| HELLO | Request to start communication |
| HELLO_ACK | Accept or reject request |
| SESSION_CREATE | Create temporary session |
| MESSAGE | Exchange language content |
| SESSION_CLOSE | Terminate session |

Future versions may introduce additional message types.

---

# 13. Payload Model

The Payload Model defines the actual communication content carried by a MESSAGE.

The payload contains:

- Content type
- Content data

---

## 13.1 Text Payload

Example:

```json
{
  "payload": {
    "type": "text",
    "content": "你好"
  }
}
```

Text payload is the default communication format.

---

## 13.2 Voice Payload

Future implementations may support direct voice transport.

Example:

```json
{
  "payload": {
    "type": "voice",
    "format": "audio"
  }
}
```

Voice transmission is an extension capability.

---

## 13.3 Display Payload

Devices with visual output may support subtitle or display information.

Example:

```json
{
  "payload": {
    "type": "subtitle",
    "content": "Hello"
  }
}
```

---

# 14. Language Model

OpenLSP messages may contain language information.

The language model describes communication direction.

Example:

```json
{
  "language": {
    "source": "zh-CN",
    "target": "en-US"
  }
}
```

---

## 14.1 Source Language

`source` identifies the original language of the content.

Example:

```
zh-CN
```

means:

Chinese language content from Mainland China.

---

## 14.2 Target Language

`target` identifies the preferred output language.

Example:

```
en-US
```

means:

English language output for United States locale.

---

# 15. Message Processing Principle

OpenLSP follows the principle:

```
Send Original Content

↓

Receive Message

↓

Local Processing

↓

Output Result
```

The receiving Endpoint decides:

- Translation method
- AI model
- Speech output
- Display method

OpenLSP does not require a specific translation implementation.

---

*End of Part 4*
---

# 16. Security Model

Security is a fundamental design principle of OpenLSP.

OpenLSP is designed to enable communication between unknown devices while minimizing unnecessary data exposure.

The protocol prioritizes:

- Privacy
- Encryption
- Temporary communication
- User control

---

# 16.1 Privacy First Principle

OpenLSP does not require permanent user identity.

Implementations SHOULD NOT require:

- User accounts
- Personal profiles
- Social relationships
- Permanent identifiers

Communication should be based on temporary sessions rather than user identity.

---

# 16.2 Encrypted Communication

OpenLSP communication SHOULD use encryption mechanisms appropriate for the selected transport layer.

Implementations SHOULD protect:

- Session information
- Message content
- Capability information

The protocol does not mandate a single encryption algorithm.

Future versions may define recommended security profiles.

---

# 16.3 Local Processing Preference

OpenLSP prefers local processing whenever possible.

Examples:

- Local speech recognition
- Local translation models
- Local text-to-speech

Cloud-based services MAY be used by implementations, but they are outside the core protocol requirements.

---

# 17. Session Security

OpenLSP Sessions are temporary communication states.

A Session SHOULD have:

- A unique identifier
- A limited lifetime
- A defined termination process

---

## 17.1 Session Lifecycle Security

A secure Session follows this model:

```
CREATE

↓

ACTIVE

↓

EXPIRE

↓

DELETE
```

After Session termination, temporary session information SHOULD be removed.

---

## 17.2 Temporary Identity

OpenLSP uses temporary communication identifiers.

A Session identifier:

- Identifies a communication session
- Does not identify a person
- Does not create a permanent relationship

---

# 18. Data Protection

OpenLSP minimizes unnecessary data collection.

The core protocol does not require:

- Cloud message storage
- Communication history storage
- User behavior tracking
- Advertising profiles

Implementations providing additional services must clearly separate those services from the OpenLSP protocol layer.

---

# 19. Compliance Requirements

An implementation claiming OpenLSP compatibility SHOULD support:

- OpenLSP message structure
- Session lifecycle
- Capability negotiation
- Required protocol behaviors

---

## 19.1 Compatibility Principles

Compatible implementations SHOULD:

- Preserve protocol field meanings
- Maintain interoperability
- Respect privacy principles
- Avoid unnecessary protocol restrictions

---

## 19.2 Non-Compatible Behavior

Implementations SHOULD NOT:

- Modify core message meanings
- Require a single commercial service
- Force permanent user identity
- Prevent other compatible implementations

---

*End of Part 5*
---

# 20. Capability Model

Capability describes the functions and limitations supported by an OpenLSP Endpoint.

Capability information allows different devices to determine compatible communication methods.

A Capability may describe:

- Input methods
- Output methods
- Language support
- Processing abilities

---

# 20.1 Capability Structure

A Capability description may contain:

```json
{
  "capabilities": [
    "text",
    "voice",
    "tts"
  ]
}
```

Each Capability represents a supported function.

---

# 20.2 Capability Types

OpenLSP defines the following basic capability categories.

## Text Capability

Supports text-based language communication.

Example:

```
text
```

---

## Voice Capability

Supports voice communication.

Example:

```
voice
```

---

## Text-to-Speech Capability

Supports audio output from translated content.

Example:

```
tts
```

---

## Subtitle Capability

Supports visual language output.

Example:

```
subtitle
```

---

# 21. Capability Exchange

Capability Exchange allows two OpenLSP Endpoints to share supported functions.

The exchange process:

```
CAPABILITY_REQUEST

↓

CAPABILITY_RESPONSE
```

---

# 21.1 Capability Request

A Device may request capability information from another Device.

Example:

```json
{
  "type": "CAPABILITY_REQUEST"
}
```

---

# 21.2 Capability Response

The receiving Device responds with supported capabilities.

Example:

```json
{
  "type": "CAPABILITY_RESPONSE",
  "capabilities": [
    "text",
    "voice",
    "tts"
  ]
}
```

---

# 22. Language Capability

Devices may announce supported languages.

Example:

```json
{
  "languages": [
    "zh-CN",
    "en-US"
  ]
}
```

Language capability allows devices to determine whether communication is possible.

---

# 23. Communication Selection

After capability exchange, OpenLSP implementations may select an appropriate communication method.

Example selection process:

```
Voice Available

↓

Use Voice Communication

↓

If unavailable

↓

Use Text Communication

↓

If unavailable

↓

Use Subtitle Communication
```

---

# 23.1 Selection Principle

OpenLSP does not require a single communication method.

The selected method depends on:

- Device capability
- User preference
- Network conditions
- Available processing resources

---

# 24. Capability Extension

Future versions of OpenLSP may define additional capabilities.

Examples:

```
image
video
ai-agent
sign-language
```

New capabilities should not break existing implementations.

Unknown capabilities should be safely ignored.

---

*End of Part 6*
---

# 25. Reference Implementation Guidelines

This section describes recommended approaches for implementing OpenLSP-compatible systems.

OpenLSP does not define a specific programming language, operating system, or hardware platform.

Implementations may use different technologies while maintaining protocol compatibility.

---

# 25.1 Recommended Architecture

A typical OpenLSP implementation may contain the following layers:

```
Application Layer

↓

OpenLSP Core

↓

Transport Adapter

↓

Device Capability Layer
```

---

## Application Layer

The Application Layer provides user-facing functions.

Examples:

- Mobile applications
- Wearable interfaces
- Translation terminals

Responsibilities include:

- User interaction
- Session control
- Communication display

---

## OpenLSP Core

The OpenLSP Core implements the protocol logic.

Responsibilities include:

- Discovery handling
- Handshake processing
- Session management
- Message processing
- Capability negotiation

The OpenLSP Core should remain independent from specific user interfaces.

---

## Transport Adapter

The Transport Adapter provides communication channels.

Possible implementations include:

- Bluetooth
- NFC
- Wi-Fi Direct
- Local network

The transport layer should be replaceable without changing the protocol logic.

---

## Device Capability Layer

The Device Capability Layer provides hardware and AI functions.

Examples:

- Speech recognition
- Translation models
- Text-to-speech
- Display systems

OpenLSP does not require a specific AI provider.

---

# 26. Minimum Compatible Implementation

A minimum OpenLSP-compatible implementation SHOULD support:

- Device Discovery
- Handshake
- Session Creation
- Message Exchange
- Session Termination

Additional capabilities may be implemented as extensions.

---

# 27. Optional Features

The following features are optional:

```
voice communication

text-to-speech

subtitle output

local AI processing

cloud AI processing

visual translation
```

Optional features should not affect basic interoperability.

---

# 28. Reference Workflow

A typical OpenLSP communication workflow:

```
Initialize

↓

Discover

↓

Handshake

↓

Create Session

↓

Exchange Messages

↓

Close Session
```

Each implementation may provide different user experiences while following the same protocol workflow.

---

# 29. SDK Design Direction

Future OpenLSP SDKs may provide simplified interfaces for developers.

Example:

```
OpenLSP.startSession()

OpenLSP.sendMessage()

OpenLSP.closeSession()
```

SDK implementations should provide access to core protocol functions while hiding unnecessary complexity.

---

# 30. Implementation Independence

OpenLSP encourages multiple independent implementations.

Compatible implementations may differ in:

- User interface
- AI models
- Hardware design
- Programming languages

Interoperability should be maintained through adherence to the OpenLSP specification.

---

*End of Part 7*
