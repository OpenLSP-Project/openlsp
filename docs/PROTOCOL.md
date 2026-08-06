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
