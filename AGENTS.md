# Multi-Agent Coordination Specification

## Assigned Roles
Maker:
timing-leak-detector

Checker:
constant-time-checker

## Coordination Protocol
- **Primary Agent**: side-channel-leakage-analyzer
- **Governance Standard**: OpenGAP Dual-Agent Control Framework v0.1.0
- **Consensus Threshold**: 100% agreement between Maker and Checker before state mutations.
- **Fail-safe Mode**: If verification fails, transaction rolls back and alerts human supervisor.
