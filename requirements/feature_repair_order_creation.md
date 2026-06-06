# Feature: Repair Order Creation

## User Story

As a service manager, I want to create a repair order for a vehicle, so that I can track repair work and customer requests.

## Acceptance Criteria

### AC1 - Successful Creation

Given a registered customer and a registered vehicle

When the service manager enters a problem description and creates a repair order

Then a new repair order should be created with status "New"

---

### AC2 - Missing Problem Description

Given a registered customer and a registered vehicle

When the service manager attempts to create a repair order without a problem description

Then the system should reject the request and display a validation error

---

### AC3 - Vehicle Not Found

Given a vehicle does not exist in the system

When the service manager attempts to create a repair order

Then the system should prevent creation of the repair order
