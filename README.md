# hospital-medication-management-system
Software system for an Automated Dispensing Cabinet (ADC) and centralized Hospital Monitoring System.

## Overview

This repository contains the software engineering project for
MECHTRON/SFWRENG 3K04.

The project consists of two independently designed software systems:

### Part A — Automated Dispensing Cabinet (ADC)

The ADC software operates locally at the patient-care location and
is responsible for cabinet operation, medication access, inventory,
fault detection, event logging, operational modes, and communication
with external systems.

### Part B — Monitoring System

The Monitoring System is a centralized human-facing application used
to supervise multiple ADCs. It provides inventory supervision, alarm
management, historical information, reporting, cabinet-health
monitoring, request handling, and configuration distribution.

### Integration

The ADC and Monitoring System communicate through a team-defined
interface. Integration requirements and interface decisions are
documented in this repository.

## Repository Structure

- `adc/` — Part A: ADC
- `monitoring-system/` — Part B: Monitoring System
- `integration/` — ADC ↔ Monitoring interface
- `docs/` — Shared project documentation
- `DECISIONS.md` — Important project decisions and rationale

## Team

- Anushka Chauhan
- Team Member 2
- Team Member 3
- Team Member 4
